#!/usr/bin/python3
"""
Parses and loads stock trades data from JSON files into MongoDB documents.
@author Vitali Tchalov
"""
import sys
import os
import json
from models import TradeBar, TradeBarMetadata

def main():
  if len(sys.argv) > 1:
    source_dir = sys.argv[1]
  else:
    source_dir = input("Enter the source directory: ")
  
  with os.scandir(source_dir) as dir_items:
    for item in dir_items:
        print(item)
        
  try:
    with open("./data/SPY-2023/json-tester.json", mode="r") as f:
      data = json.load(f)
      # print(json.dumps(data, indent=2)) # outputs the entire JSON file formatted
      print(json.dumps(data["Meta Data"], indent=2))
      print(json.dumps(data["Time Series (1min)"], indent=2))
      
      metadata = TradeBarMetadata(data["Meta Data"]["2. Symbol"])
      
      for xmin in data["Time Series (1min)"]:
        #print(xmin)
        #print(data["Time Series (1min)"][xmin]["1. open"])
        bar = TradeBar(
                  metadata,
                  data["Time Series (1min)"][xmin],
                  data["Time Series (1min)"][xmin]["2. high"],
                  '1m')
        print(json.dumps(bar, indent=2))
  finally:
        f.close()

if __name__ == '__main__':
    main()
