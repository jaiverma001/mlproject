##all the code that re used to read the file after rading the data we may do dtaa validation dta transforation
import os
import  sys
from src.exception import customException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
@dataclass
class dataIngestionconfig:
    train_data_path: str=os.path.join('artifact','train.csv')
    test_data_path: str=os.path.join('artifact','test.csv')
    raw_data_path: str=os.path.join('artifact','data.csv')
class dataingestion:
    def __init__(self):
        self.ingestion_config = dataIngestionconfig()
    def initate_data_ingestion(self):
        logging.info("entered the data inegstionmethod pr componenet")
        try:
            df = pd.read_csv("notebook copy/data/stud.csv")
            logging.info("we have exported the data in the data frame")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("ingestion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path ##this wil give us al the inforamtion of the data transformation
            )

        except Exception as e:
            raise customException(e,sys)
if __name__ == "__main__":
    obj = dataingestion()
    obj.initate_data_ingestion()           
