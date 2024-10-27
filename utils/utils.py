from typing import Dict
from pydantic import BaseModel


class Services(BaseModel):
    serviceName: str
    serviceUrl: str
    versionNumber: str


class InputData(BaseModel):
    requestId: str
    servicesDetails: Dict[str, Services]
    currentServicesDetails: Dict[str, Services]


class OutputData(BaseModel):
    requestId: str
    servicesDetails: Dict[str, Services]
    currentServicesDetails: Dict[str, Services]
    directoryPath: str | None
