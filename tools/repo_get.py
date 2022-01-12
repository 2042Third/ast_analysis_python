from google.cloud import bigquery

client = bigquery.Client()

dataset_id = "repo_python"
dataset_id_full = f"{client.project}.{dataset_id}"
dataset = bigquery.Dataset(dataset_id_full)

# new dataset created
# dataset = client.create_dataset(dataset)

# Configure query 
job_config = bigquery.QueryJobConfig()
job_config.destination = f"{dataset_id_full}.repo_py_limit"

query = """
    select f.f0_ as repo_path, c.content from `ast-analysis-python.astmine.py_list` as f 
join `bigquery-public-data.github_repos.contents` as c on f.id=c.id 
where f.f0_ like "%.py";
"""
query_job = client.query(query, job_config=job_config)
query_job.result()  # Waits for the query to finish
