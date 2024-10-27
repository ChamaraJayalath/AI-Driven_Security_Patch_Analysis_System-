from ai_processor.ai_processor import AIProcessor
from scraper.scraper import Scraper
from utils.utils import InputData, OutputData
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from scripts.logging_config import logger
app = FastAPI()


@app.post("/download-services-data")
async def download_services_data(input_data: InputData):
    logger.info("Download services data request received")
    scraper = Scraper()
    ai_processor = AIProcessor()
    try:
        output_data = scraper.download_services_html_doc(input_data)
        response_data = OutputData(
            requestId=output_data.requestId,
            servicesDetails=output_data.servicesDetails,
            currentServicesDetails=output_data.currentServicesDetails,
            directoryPath=output_data.directoryPath,
        ).model_dump()
        ai_response = ai_processor.generate_report(output_data)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")

        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
    logger.info("Download completed successfully")
    return JSONResponse(content=ai_response, status_code=200)
