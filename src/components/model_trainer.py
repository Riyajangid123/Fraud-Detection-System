import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.pipeline import Pipeline
from sklearn.metrics import precision_score,recall_score,f1_score,roc_auc_score
from sklearn.model_selection import cross_val_score,StratifiedKFold
import mlflow
import mlflow.sklearn
from imblearn.over_sampling import SMOTE

class ModelTrainer:
    def train_model(self,x,y,preprocessor):

        mlflow.set_tracking_uri("file:./mlruns")

        mlflow.set_experiment("Fraud Detection")


        with mlflow.start_run():

            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
            
            model_pipeline = Pipeline(steps=[("preprocessor", preprocessor),("smote", SMOTE()),
                                             ("model", RandomForestClassifier(n_estimators=100,
                                                                              max_depth=4,
                                                                              n_jobs=-1,
                                                                              random_state=42
                                                                              ))])
            model_pipeline.fit(x_train, y_train)
            
            y_pred_default = model_pipeline.predict(x_test)
            precision = precision_score(y_test, y_pred_default)
            recall = recall_score(y_test, y_pred_default)
            f1 = f1_score(y_test, y_pred_default)


            fold = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

            cross = cross_val_score(
                model_pipeline,
                x_train,
                y_train,
                cv=fold,
                scoring="roc_auc",
                n_jobs=-1
            )
            y_prob = model_pipeline.predict_proba(x_test)[:, 1]

            best_f1 = 0
            best_threshold = 0

            for t in [0.3, 0.5, 0.7,0.8]:
                y_pred_t = (y_prob > t).astype(int)
                f1_t = f1_score(y_test, y_pred_t)

                print(f"\nThreshold {t}")
                print("Precision:", precision_score(y_test, y_pred_t))
                print("Recall:", recall_score(y_test, y_pred_t))

                if f1_t > best_f1:
                    best_f1 = f1_t
                    best_threshold = t
            y_prob = model_pipeline.predict_proba(x_test)[:, 1]
            roc_auc = roc_auc_score(y_test, y_prob)

            print(f"cross validation score-->{cross.mean()}")

            mlflow.log_param("model", "RandomForest")
            mlflow.log_param("n_estimators", 100)
            mlflow.log_param("max_depth", 4)
            mlflow.log_param("cv_folds", 3)
            mlflow.log_param("best_threshold", best_threshold)

            mlflow.log_metric("best_threshold", best_threshold)
            mlflow.log_metric("precision", precision)
            mlflow.log_metric("recall", recall)
            mlflow.log_metric("f1_score", f1)
            mlflow.log_metric("roc_auc_cv", cross.mean())
            mlflow.log_metric("roc_auc", roc_auc)
            mlflow.log_metric("best_f1", best_f1)

            mlflow.sklearn.log_model(model_pipeline, "model",registered_model_name="FraudDetectionModel")

            os.makedirs("models",exist_ok=True)

            joblib.dump(model_pipeline,"models/model.pkl")

            print("Model saved successfully")

            return model_pipeline


            


            
