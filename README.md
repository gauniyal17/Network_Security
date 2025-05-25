Hey this is my network security project to catch phishing data




📁 Project Folder Structure Overview
This section explains the purpose of each key file and folder used in this machine learning project.

1. logging/
Handles centralized logging throughout the project.

Purpose: Captures logs for debugging, monitoring, and error tracking.

Typical Use: Records info/warning/error messages during pipeline execution.

2. exception/
Custom exception handling module.

Purpose: Defines a custom exception class to manage and raise descriptive error messages in the project.

Typical Use: Helps in pinpointing exact error sources during execution.

3. push_data.py
Handles data insertion into MongoDB.

Purpose: Pushes raw or preprocessed data into a MongoDB collection for storage and further use.

Typical Use: Acts as a bridge between raw data sources and the training pipeline.

4. training_pipeline/
Contains pipeline logic and core constants for model training.

Purpose: Orchestrates the entire training pipeline and defines key configuration constants used throughout the project.

✔️ Key File: __init__.py



5. config_entity/
Defines configuration entities for various pipeline components.

Purpose: Stores configurations as data classes (like for data ingestion, model training, evaluation, etc.).

Typical Use: Makes the code modular and easy to manage by separating logic from configuration.