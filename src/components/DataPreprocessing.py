import pandas as pd
from sklearn.preprocessing import StandardScaler
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

class DataPreprocessing:
    def preprocess_data(self,data):

        x=data.drop("Class",axis=1)
        y=data["Class"]

        num_features=x.columns

        num_pipeline=Pipeline(steps=[("imputer",SimpleImputer(strategy="median")),
                                     ("scaler",StandardScaler())])
        
        preprocessor=ColumnTransformer([("num",num_pipeline,num_features)])

        return x,y,preprocessor


        
        