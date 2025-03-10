from enum import Enum
from pydantic import BaseModel
import pandas as pd

# Definición de los distintos tipos de eventos


class Event(str, Enum):
    DATA: "DATA"
    SIGNAL: "SIGNAL"


class BaseEvent(BaseModel):
    event_type: Event

    class Config:
        arbitrary_types_allowed = True


class DataEvent(BaseEvent):
    event_type: Event = Event.DATA
    symbol: str
    data: pd.Series
