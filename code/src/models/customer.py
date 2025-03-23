import pandas as pd
from fastapi import HTTPException

class Customer:
    def __init__(self,csv_path):
        self.csv_path = csv_path
    def load_customer_data(self,cust_id):
        try:
            df = pd.read_csv(self.csv_path)
            customer_data = df[df['cust_id']==cust_id].iloc[0]
            return customer_data.to_string()
        except Exception as e:
            raise HTTPException(status_code=404,detail=f"Customer ID {cust_id} not found")