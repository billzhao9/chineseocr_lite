# This script allows to simulate Cerebrium serverless in local for test purpose
# Author: @chaignc
# run me with
# uvicorn cerebrium_local:app
  
from fastapi import FastAPI
from mainlocal import predict
import logging
import time

app = FastAPI()
logger = logging.basicConfig(level=logging.INFO)

# Define the predict endpoint
@app.post("/predict")
def predict_route(input_data: dict):
    global logger
    
    start_time = time.time()
    result = predict(input_data, "local", logger, binaries=None)
    end_time = time.time()
    run_time_ms = round((end_time - start_time) * 1000, 2)
    return {"result": result, "run_time_ms": run_time_ms}