import os
from datetime import datetime
from typing import Type
from markdownify import markdownify as md
import requests
from bs4 import BeautifulSoup
from utils.utils import InputData, OutputData
from fastapi import HTTPException
from scripts.logging_config import logger


class Scraper:
    @staticmethod
    def download_services_html_doc(input_data: InputData):
        current_time = datetime.strftime(datetime.now(), "%Y%m%d-%H:%M:%S:%f")
        directory_name = f"downloaded_services/{current_time}"

        # Create main and subdirectories for "new_services" and "current_services"
        new_services_dir, current_services_dir = make_subdirectories(directory_name, "new_services", "current_services")

        logger.info(f"New services directory: {new_services_dir}, Current services directory: {current_services_dir}")

        # Loop through each type of services directory
        for i, service_dir in enumerate([new_services_dir, current_services_dir]):
            directory_name_for_html, directory_name_for_markdown = make_subdirectories(service_dir, "html", "markdown")

            # Select the appropriate service details based on the directory type
            if i == 0:
                service_type = input_data.servicesDetails.values()
            else:
                service_type = input_data.currentServicesDetails.values()

            for service in service_type:
                try:
                    logger.info(f"Attempting to download from {service.serviceUrl}...")
                    response = requests.get(service.serviceUrl, timeout=10)
                    response.raise_for_status()
                    logger.info(f"Successfully downloaded from {service.serviceUrl}")

                    service_name = service.serviceName
                    html_content = response.content
                    soup = BeautifulSoup(html_content, 'html.parser')

                    # Save HTML content
                    with open(f"{directory_name_for_html}/{service_name}.html", 'w', encoding='utf-8') as file:
                        file.write(soup.prettify())
                    logger.info(f"Saved HTML content for {service_name} to {service_name}.html")

                    # Convert HTML to Markdown and save
                    markdown_content = convert_html_to_markdown(html_content)
                    markdown_file_path = f"{directory_name_for_markdown}/{service_name}.md"
                    with open(markdown_file_path, 'w', encoding='utf-8') as md_file:
                        md_file.write(markdown_content)
                    logger.info(f"Saved Markdown content for {service_name} to {markdown_file_path}")
                except requests.exceptions.RequestException as e:
                    logger.error(f"Error downloading from {service.serviceUrl}: {str(e)}")
                    raise HTTPException(status_code=500, detail=f"Error downloading from {service.serviceUrl}: {str(e)}")

        return output_util_transformer(input_data, directory_name)


def convert_html_to_markdown(html_content: bytes) -> str:
    return md(html_content.decode('utf-8'))


def create_directory(directory_name):
    """Create a folder"""
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        logger.info("Main Folder Created.")
    return directory_name


def make_subdirectories(directory, subname1, subname2):
    """Create subfolders for HTML and Markdown files."""
    html_directory = os.path.join(directory, subname1)
    markdown_directory = os.path.join(directory, subname2)

    create_directory(html_directory)
    create_directory(markdown_directory)

    logger.info("SUB FOLDERS CREATED")
    return html_directory, markdown_directory


def output_util_transformer(input_data: InputData, directory_name: str) -> OutputData:
    # Instantiate OutputData with necessary attributes
    output_data = OutputData(
        requestId=input_data.requestId,
        servicesDetails=input_data.servicesDetails,
        currentServicesDetails=input_data.currentServicesDetails,
        directoryPath=directory_name
    )
    return output_data


