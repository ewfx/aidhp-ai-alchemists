import pandas as pd
from transformers import pipeline
import os

script_dir=os.path.dirname(os.path.abspath(__file__))

def preprocess_data():
    #Load datasets
    cust_profile = pd.read_csv(os.path.join(script_dir,r'..\..\data\cust_profile.csv'))
    social_media_sentiment = pd.read_csv(os.path.join(script_dir,r'..\..\data\social_media_sentiment.csv'))
    transaction_history = pd.read_csv(os.path.join(script_dir,r'..\..\data\transaction_history.csv'))

    #merge the datasets
    final_data = pd.merge(cust_profile,transaction_history,on='cust_id')
    final_data = pd.merge(final_data,social_media_sentiment,on='cust_id')

    final_data['timestamp'] = pd.to_datetime(final_data['timestamp'])
    final_data['purchase_date'] = pd.to_datetime(final_data['purchase_date'])

    #handle missing values
    final_data.fillna(method='ffill',inplace=True)

    sentiment_analyser = pipeline("sentiment-analysis")

    final_data['sentiment'] = final_data['content'].apply(lambda x: sentiment_analyser(x)[0]['label'])
    #save merged data
    final_data.to_csv(os.path.join(script_dir,r'..\..\data\final_data.csv'),index=False)