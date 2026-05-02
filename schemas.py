from pydantic import BaseModel

class InputData(BaseModel):
    temperature: float
    humidity: float
    hour: float
    