from datetime import time
import json
import os
import glob
from utils.utils import OutputData
from scripts.logging_config import logger
import google.generativeai as genai
import os
import pandas as pd
from utils.utils import OutputData
from scripts.logging_config import logger
import os
import pandas as pd
import time
from openai import OpenAI



class AIProcessor:
    @staticmethod
    def generate_report(scraper_data: OutputData):
        client = OpenAI()
        logger.info("Starting report generation process.")

        # Initialize the Gemini model
        # model = genai.GenerativeModel("gemini-1.5-flash")
        # genai.configure(api_key="AIzaSyAFHH8CKaqIy0O4qQHSxLbb7iIsLn6eydg")

        # Define directories
        new_services_directory = f"{scraper_data.directoryPath}/new_services/markdown"
        current_services_directory = f"{scraper_data.directoryPath}/current_services/markdown"

        



        # Process AI responses for both directories
        logger.info(1)
        new_services_ai_response = AIProcessor.services_ai_process(client, new_services_directory, "Newly Released Services Details")
        logger.info(2)
        logger.info(new_services_ai_response)
        current_services_ai_response = AIProcessor.services_ai_process(client, current_services_directory, "Current Services Details")
        logger.info(3)
        logger.info(current_services_ai_response)

        # Combine the responses
        new_content = new_services_ai_response + "\n" + current_services_ai_response
        
        logger.info(4)

        openai_report_response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "system", 
                               "content": "Compare the descriptions of the new services against the current services to determine any potential security impacts.\n For each current service, analyze whether new service functionalities, technologies, or dependencies might introduce security vulnerabilities, performance concerns, or dependencies that could impact stability.\n Focus on potential security risks, and generate a report summarizing the findings in a table format.\n The table should include:- Current Service Name - Potential Security Impact from New Services - Risk Level= High/Medium/Low - Recommendations for Mitigation"}, 
                               {"role": "user", "content": new_content}])

        # Generate report
        # full_response = model.generate_content([
        #     """
        #     Compare the descriptions of the new services against the current services to determine any potential security impacts.
        #     For each current service, analyze whether new service functionalities, technologies, or dependencies might introduce security
        #     vulnerabilities, performance concerns, or dependencies that could impact stability. Focus on potential security risks,
        #     and generate a report summarizing the findings in a table format.

        #     The table should include:
        #     - Current Service Name
        #     - Potential Security Impact from New Services
        #     - Risk Level (High/Medium/Low)
        #     - Recommendations for Mitigation
        #     """, new_content])
        logger.info(5)
        logger.info("main thing done")
        logger.info(openai_report_response.choices[0].message.content)
        return openai_report_response.choices[0].message.content

    @staticmethod
    def services_ai_process(client, directory_path, title_name):
        try:
            logger.info(f"Loading documents from {directory_path}.")
            responses = ''
            for file_path in glob.glob(os.path.join(directory_path, "*.md")):
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read the file content
                    content = file.read()
                

                openai_response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[{"role": "system", "content": f"You will be provided officially public available release notes of different services. Extract the service name and Extract all the security vulnerabilities included in this content related to this service.generate response using markdown. Add title as {title_name}"},
                                        {"role": "user", "content": content}
                            ])

                # response = model.generate_content([
                #     "These are officially public available release notes. Extract all the security vulnerabilities included in this content related to this service.",
                #     content
                # ])
                
                responses += str(openai_response.choices[0].message.content)
                
            logger.info("service ai done")
            return responses

        except Exception as e:
            logger.error(f"Error processing files in {directory_path}: {e}")
            return {}
