from scraper.scraper import Scraper
from utils.utils import InputData
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from scripts.logging_config import logger
app = FastAPI()


@app.post("/download-services-data")
async def download_services_data(input_data: InputData):
    logger.info("Download services data request received")
    scraper = Scraper()
    try:
        abc = scraper.download_services_html_doc(input_data)
        print(abc.requestId)
        print(abc.servicesDetails)
        print(abc.htmlDirectoryPath)
        print(abc.markdownDirectoryPath)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")

        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
    logger.info("Download completed successfully")
    return JSONResponse(content={"message": "Download successful"}, status_code=200)
