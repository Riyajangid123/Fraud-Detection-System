from src.components.DataIngestion import DataIngestion
from src.components.DataPreprocessing import DataPreprocessing
from src.components.model_trainer import ModelTrainer
from src.components.prediction_pipeline import PredictPipeline

class TrainPipeline:
    def run_pipeline(self):
        ingestion=DataIngestion()
        data=ingestion.ingest_data(r"C:\Users\DELL\OneDrive\Desktop\Credit_Card_Fraud_Detection_System\data\creditcard.csv")

        print("Data Ingestion Complete")

        preprocessing=DataPreprocessing()

        x,y,preprocessor=preprocessing.preprocess_data(data)

        print("Data Preprocessing Done")

        trainer=ModelTrainer()

        trainer.train_model(x,y,preprocessor)

        print("Model Training Done")

        actual_prediction=PredictPipeline()
        sample = data.drop(columns=["Class"]).iloc[0].to_dict()  # take first row
        result = actual_prediction.predict(sample)
        print(f"Prediction Result: {result}")

if __name__=="__main__":
    
    pipeline=TrainPipeline()
    pipeline.run_pipeline()
