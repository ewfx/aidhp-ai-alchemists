import uvicorn
from api.app import app
from data_process.data_processing import preprocess_data;

if __name__ == "__main__" :
    preprocess_data()
    uvicorn.run(app,host="0.0.0.0",port=8080)