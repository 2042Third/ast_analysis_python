create table if not exists `astmine.repo_python` (
`fullpath` STRING,
`content` STRING
);
insert into `ast-analysis-python.astmine.repo_python`
SELECT 
 concat(f.repo_name, ' ', f.path) as repo_path, c.content
FROM `bigquery-public-data.github_repos.files` as f
JOIN `bigquery-public-data.github_repos.contents` as c on f.id = c.id;



-- correction

select concat(f.repo_path, ' ', f.path) as repo_path, r.content 
from `ast-analysis-python.repo_python.repo` as r and `bigquery-public-data.github_repos.files` as f
where f.repo_path in ast-analysis-python.astmine.pythonlist and f.repo_name like r.repo_path;


-- correction
select concat(f.repo_name, ' ', f.path) as repo_path, r.content 
from `bigquery-public-data.github_repos.contents` as r, `bigquery-public-data.github_repos.files` as f
where f.repo_name in (
    select rl.repo_name from `ast-analysis-python.astmine.pythonlist` as rl
 ) and f.id like r.id;