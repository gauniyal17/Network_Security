ETL pipeline  [Extract transform Load]
source--------transformation----------destination


Source?--- place where data is coming eg my local storage, api's, s3 bucket

transformation?-----doing some basic cleaning a preprocessing before pushing data to destination eg converting to JSON

destination?-------Our final push destination of data like mongodb database, mysql, aws dynamodb, s3 buckets



![Alt Text](./images/my_image.png)



Data ingestion Architecture


1-Data ingestion config???=------ Basic info like where my data needs to be stored, steps to perform feature eng. training/testing file path.. etc.


2-Get data from mongo db - 


3- data ingestion artifact-- output of data ingestion config. we'll create ingested folder that create train test split.

4- dropping the unnecessary cols
