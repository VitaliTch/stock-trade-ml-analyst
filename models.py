"""
Classes to persist stock trades data into MongoDB database.
@author Vitali Tchalov
"""
from dataclasses import dataclass
import uuid
#from typing import Optional
#from pydantic import BaseModel, Field

@dataclass
class TradeBarMetadata(dict):
  stock_sym: str

#class TradeBar(BaseModel):
@dataclass
class TradeBar(dict):
  """
  def __init__(self, bar_time, open, high, low, close, interval):
    self. =
    self. =
    self. =
    self. =
    self. =
    self.interval = interval
    """
  metadata: TradeBarMetadata
  # For entities to be inserted to MongoDB, the id should be left null to let DB to generate it.
  #id: str = Field(default_factory=uuid.uuid4, alias="_id")
  #id: str
  #bar_time: str Field(...)
  bar_time: str
  #open: str = Field(...)
  open: str
  #high: str = Field(...)
  #high: str
  #low: str = Field(...)
  #low: str
  #close: str = Field(...)
  #close: str
  interval: str

  
