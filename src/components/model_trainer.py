import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,

)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path= os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config= ModelTrainerConfig()

    def initiate_model_trainer(self,train_array, test_arrray):
        try:
            X_train, y_train, X_test, y_test= (
                train_array[:, :-1],
                train_array[:, -1],
                test_arrray[:, :-1],
                test_arrray[:, -1]
            )
            models= {
                "RandomForestRegressor": RandomForestRegressor(),
                "DecisionTreeRegressor": DecisionTreeRegressor(),
                "XGBRegressor": XGBRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "KNeighborsRegressor": KNeighborsRegressor(),
                "AdaBoostRegressor": AdaBoostRegressor()
                
            }

                        # ✅ Define hyperparameters
            params = {
                "RandomForestRegressor": {
                    "n_estimators": [50, 100, 200],
                    "max_depth": [None, 10, 20],
                    "min_samples_split": [2, 5, 10]
                },
                "DecisionTreeRegressor": {
                    "max_depth": [None, 10, 20, 30],
                    "min_samples_split": [2, 5, 10]
                },
                "XGBRegressor": {
                    "n_estimators": [50, 100, 200],
                    "learning_rate": [0.01, 0.1, 0.2],
                    "max_depth": [3, 6, 9]
                },
                "GradientBoostingRegressor": {
                    "n_estimators": [50, 100, 200],
                    "learning_rate": [0.01, 0.1, 0.2],
                    "max_depth": [3, 6, 9]
                },
                "KNeighborsRegressor": {
                    "n_neighbors": [3, 5, 7, 10],
                    "weights": ["uniform", "distance"],
                    "metric": ["euclidean", "manhattan"]
                },
                "AdaBoostRegressor": {
                    "n_estimators": [50, 100, 200],
                    "learning_rate": [0.01, 0.1, 1.0]
                },
                
            }
            model_report:dict= evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models, param=params)

            # To get the best model score from the dictionary
            best_model_score= max(sorted(model_report.values()))


            # To get the best model name from the dictionary
            best_model_name= list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model= models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info("Best found model on both  traning and testing dataset")

            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj= best_model)

            predicted= best_model.predict(X_test)

            r2_square= r2_score(y_test, predicted)
            return r2_square

            
        except Exception as e:
            raise CustomException(e, sys)

