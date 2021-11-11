SELECT 
 concat(f.repo_name, ' ', f.path) as repo_path, c.content
FROM `bigquery-public-data.github_repos.sample_files` as f , astmine.pylist as pl
JOIN `bigquery-public-data.github_repos.sample_contents` as c on f.id = c.id and pl.repo_name = f.repo_name

;