from models.customer import Customer
from models.recommendation import RecommendationEngine
from fastapi import HTTPException

class RecommendationService:
    def __init__(self,csv_path,config_list):
        self.customer_model = Customer(csv_path)
        self.recommendation_engine = RecommendationEngine(config_list)
    
    def get_recommendations(self,cust_id):
        customer_data = self.customer_model.load_customer_data(cust_id)
        recommendations = self.recommendation_engine.generate_recommendations(cust_id,customer_data)
        if not recommendations:
            raise HTTPException(status_code=500,detail="Failed to generate recommendations.")
        return recommendations