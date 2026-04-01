import os
import mlflow

# Use your Databricks profile
os.environ["DATABRICKS_CONFIG_PROFILE"] = "Genevio"

# Tell MLflow to use Databricks
mlflow.set_tracking_uri("databricks")

# 🔥 IMPORTANT: Use full path with your username
mlflow.set_experiment("/Users/genevior98@gmail.com/test_experiment")

with mlflow.start_run():
    mlflow.log_param("param1", 10)
    mlflow.log_metric("accuracy", 0.95)

print("MLflow test completed!")