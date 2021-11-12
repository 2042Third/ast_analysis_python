from google.cloud import bigquery

client = bigquery.Client()

dataset_id = "repo_python"
dataset_id_full = f"{client.project}.{dataset_id}"
dataset = bigquery.Dataset(dataset_id_full)

# new dataset created
# dataset = client.create_dataset(dataset)

# Configure query 
job_config = bigquery.QueryJobConfig()
job_config.destination = f"{dataset_id_full}.repo_py"

query = """
    select f.repo_path, f.content from `ast-analysis-python.repo_python.repo` as f
    where f.repo_path like "%.py"
    limit 2000000
    ;
"""
query_job = client.query(query, job_config=job_config)
query_job.result()  # Waits for the query to finish
