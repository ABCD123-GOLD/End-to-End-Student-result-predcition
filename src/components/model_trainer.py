import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingRegressor,
    RandomForestRegressor,

)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model


@dataclass
class ModelTrainerConfig:
    trained_model_file_path= os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config= ModelTrainerConfig()

    def initiate_model_trainer(self,train_array, test_arrray, preprocessor_path):
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
                "CatBoostRegressor": CatBoostRegressor(verbose=False),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "KNeighborsRegressor": KNeighborsRegressor(),
                "AdaBoostClassifier": AdaBoostClassifier(),
                "Linear Regression": LinearRegression()
                
            }
            model_report= evaluate_model(x_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models)

            # To get the best model score from the dictionary
            best_model_score= max(sorted(model_report.values()))

            # To get the best model name from the dictionary
            best_model_name= list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model= models[best_model_name]
            

            



        except:
            pass

