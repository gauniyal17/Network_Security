import os
import sys
import numpy as np
import pandas as pd


"Defining common constant variable for training pipeline"


TARGET_COLUMN="Result"
PIPELINE_NAME: str="NetworkSecurity"
ARTIFACT_DIR: str="Artifacts"
FILE_NAME: str="phishingData.csv"

TRAIN_FILE_NAME: str= "train.csv"
TEST_FILE_NAME: str="test.csv"




"Data Ingestion related constant start with DATA_INGESTION VAR NAME... This should be hard coded bucause these are constants"
""
""

DATA_INGESTION_COLLECTION_NAME: str="NetworkData"
DATA_INGESTION_DATABASE_NAME: str="RAHUL_ML"
DATA_INGESTION_DIR_NAME: str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str="feature_store"
DATA_INGESTION_INGESTED_DIR: str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float=0.2