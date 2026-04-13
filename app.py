import pandas as pd
from fastapi import FastAPI
from typing import Annotated, Literal
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from churn_prediction.pipeline.prediction_pipeline import PredictionPipeline


app = FastAPI(title="Churn Prediction")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
      tenure: Annotated[int, Field(..., description="Enter the value of tenure", ge=0, example=12)]
      MonthlyCharges: Annotated[float, Field(..., description="Enter the monthly charges paid by the customers", ge=0, example=65.5)]
      TotalCharges: Annotated[float, Field(..., description="Total charges paid by the customers", ge=0, example=2283.3)]
      TechSupport: Annotated[Literal['yes', 'no', 'no internet service'], Field(..., description="Tech support used by the customers", example="yes")]
      Contract: Annotated[Literal['month-to-month', 'one year', 'two year'], Field(..., description="Contract done by the customers", example="month-to-month")]
      Partner: Annotated[Literal['yes', 'no'], Field(..., description="Whether the customer has a partner", example="yes")]
      OnlineSecurity: Annotated[Literal['yes', 'no', 'no internet service'], Field(..., description="Online security service used by the customer", example="no")]
      InternetService: Annotated[Literal['DSL', 'Fiber optic', 'No'], Field(..., description="Type of internet service", example="Fiber optic")]

predict_pipe = PredictionPipeline()

@app.get("/")
async def home():
      return {'message': "Welcome to telco customer churn prediction"}

@app.get("/train")
async def train_model():
      pass

@app.post("/predict")
async def predict_churn(UserInput: Input):
      data = pd.DataFrame([{
            'tenuer': UserInput.tenure,
            'MonthlyCharges': UserInput.MonthlyCharges,
            'TotalCharges': UserInput.TotalCharges,
            'TechSupport': UserInput.TechSupport,
            'Contract': UserInput.Contract,
            'Partner': UserInput.Partner,
            'OnlineSecurity': UserInput.OnlineSecurity,
            'InternetService': UserInput.InternetService
      }])
      prediction = predict_pipe.predict_churn(data)

      return {
            "prediction": prediction,
            "status": 200
      }