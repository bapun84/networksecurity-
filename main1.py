import mlflow
mlflow.set_tracking_uri("https://dagshub.com/bapun84/networksecurity-.mlflow")
with mlflow.start_run() as run:
    print("MLflow connected successfully!")
