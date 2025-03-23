from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from services.recommendation_service import RecommendationService
import autogen
import os
from typing import List

script_dir=os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

config_list = autogen.config_list_from_json(os.path.join(script_dir,r"..\OAI_CONFIG_LIST.json"))
cust_data = os.path.join(script_dir,r"..\..\data\final_data.csv")

recommendation_service = RecommendationService(csv_path=cust_data,config_list=config_list)

class User(BaseModel):
    cust_id:str

class RecommendationsResponse(BaseModel):
    recommendations: List[str]

@app.post("/get-recommendations",response_model=RecommendationsResponse)
async def get_recommendations(request:User):
    cust_id = request.cust_id
    recommendations = recommendation_service.get_recommendations(cust_id=cust_id)
    if recommendations:
         recommendations_list = recommendations.strip().split("\n")[1:]
         recommendations_list = [rec.strip() for rec in recommendations_list if rec.strip()]
    else:
        raise HTTPException(status_code=500, detail="Failed to generate recommendations.")
    return {"recommendations":recommendations_list}