DROP DATABASE astmine;
CREATE SCHEMA astmine;
USE astmine;

FLUSH privileges;

SHOW GLOBAL VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 'ON';
SHOW GLOBAL VARIABLES LIKE 'local_infile';

USE astmine;



CREATE TABLE `output` (
  `l1` VARCHAR(255) DEFAULT NULL,
  `l2` VARCHAR(255) DEFAULT NULL,
  `l3` VARCHAR(255) DEFAULT NULL,
  `fullpath` VARCHAR(511) DEFAULT NULL,
  `filename` VARCHAR(255) DEFAULT NULL, 
  `functype` VARCHAR(255) DEFAULT NULL,
  `funcname` VARCHAR(255) DEFAULT NULL,
  `linenumber` VARCHAR(255) DEFAULT NULL
);
-- ["SET "+part1[i]+" = (@var"+str(i+1)+" = \'Y\');\n" for i in range(len(part1))]
SET GLOBAL local_infile = 'ON';

LOAD data local INFILE 'C:/Users/18604/Desktop/research/ast_analysis/ast_analysis_data.csv' INTO TABLE output 
  FIELDS TERMINATED BY ', ' ENCLOSED BY '\"'
  LINES TERMINATED BY '\r\n' (l1,l2,l3,fullpath,filename,functype,funcname,linenumber);
update output
set output.l1 = trim(trailing "\'" from TRIM(LEADING "b\'" FROM output.l1)) 
,  output.l2 = trim(trailing "\'" from TRIM(LEADING "b\'" FROM output.l2)) 
,  output.l3 = trim(trailing "\'" from TRIM(LEADING "b\'" FROM output.l3)) 
,  output.fullpath = trim(trailing "\'" from TRIM(LEADING "b\'" FROM output.fullpath)) 
,  output.filename = trim(trailing "\'" from TRIM(LEADING "b\'" FROM output.filename)) 
,  output.functype = trim(trailing "\'" from TRIM(LEADING "b\'" FROM output.functype)) 
,  output.funcname = trim(trailing "\'" from TRIM(LEADING "b\'" FROM output.funcname)) 
,  output.linenumber = trim(trailing "\'" from TRIM(LEADING "b\'" FROM output.linenumber)) 
where output.l1 like "b\'%\'"
;
SHOW WARNINGS;
SELECT * FROM output;

-- create or replace table `func_dyn` (
-- `Organization` VARCHAR(255) DEFAULT null,
-- `DynCount` VARCHAR(255) DEFAULT null,
-- `FuncCount` VARCHAR(255) DEFAULT null
-- );
create or replace table `func_dyn_dec` (
`Organization` text DEFAULT null,
`DynCount` VARCHAR(255) DEFAULT null,
`FuncCount` VARCHAR(255) DEFAULT null,
`DecCount` VARCHAR(255) DEFAULT null
);

insert into func_dyn_dec (Organization,DynCount,FuncCount,DecCount) 
select output.l2,  coalesce(0),  coalesce(0),  coalesce(0) from output 
group by output.l2 ;

update  func_dyn_dec as t1,  (select l2, COUNT(*) as orgDEC from output where functype = "DEC" GROUP by l2) as t2
set t1.DecCount=t2.orgDEC
where t1.Organization = t2.l2;
update  func_dyn_dec as t1,  (select l2, COUNT(*) as orgFNL from output where functype = "FNL" GROUP by l2) as t2
set t1.FuncCount =t2.orgFNL
where t1.Organization = t2.l2;
update  func_dyn_dec as t1,  (select l2, COUNT(*) as orgDYN from output where functype = "DYN" GROUP by l2) as t2
set t1.DynCount =t2.orgDYN
where t1.Organization = t2.l2;



-- project-wise


create or replace table `func_dyn_dec_proj` (
`Project` text DEFAULT null,
`DynCount` VARCHAR(255) DEFAULT null,
`FuncCount` VARCHAR(255) DEFAULT null,
`DecCount` VARCHAR(255) DEFAULT null
);
insert into func_dyn_dec_proj (Project,DynCount,FuncCount,DecCount) 
select output.l3,  coalesce(0),  coalesce(0),  coalesce(0) from output 
group by output.l3 ;

update  func_dyn_dec_proj as t1,  (select l3, COUNT(*) as orgDEC from output where functype = "DEC" GROUP by l3) as t2
set t1.DecCount=t2.orgDEC
where t1.Project = t2.l3;
update  func_dyn_dec_proj as t1,  (select l3, COUNT(*) as orgFNL from output where functype = "FNL" GROUP by l3) as t2
set t1.FuncCount =t2.orgFNL
where t1.Project = t2.l3;
update  func_dyn_dec_proj as t1,  (select l3, COUNT(*) as orgDYN from output where functype = "DYN" GROUP by l3) as t2
set t1.DynCount =t2.orgDYN
where t1.Project = t2.l3;


-- write to file
-- organization frequency all 
SELECT *  FROM func_dyn_dec;
-- organization dyn only
select * from (select  * from func_dyn_dec  where DynCount>0 ) as org_dyn;
-- organization func only
select * from (select  * from func_dyn_dec  where FuncCount>0 ) as org_func;
-- organization dec only
select * from (select  * from func_dyn_dec  where DecCount>0 ) as org_dec;

-- project frequency all 
SELECT * FROM func_dyn_dec_proj;
-- project dyn only
select * from (select  * from func_dyn_dec_proj  where DynCount>0 ) as proj_dyn;
-- project func only
select * from (select  * from func_dyn_dec_proj  where FuncCount>0 ) as proj_func;
-- project dec only
select * from (select  * from func_dyn_dec_proj  where DecCount>0 ) as proj_dec;
 
select funcname , count(*) as freq from output 
where functype = "FNL" 
group by funcname
order by count(*) DESC;

select funcname , count(*) as freq from output 
where functype = "DEC" 
group by funcname
order by count(*) desc
limit 26;
select funcname , count(*) as freq from output 
where functype = "DYN" 
group by funcname
order by count(*) desc
;
select funcname , count(*) as freq from output  
group by funcname
order by count(*) desc
;

CREATE TABLE `foutput` (
  `l1` VARCHAR(255) DEFAULT NULL,
  `l2` VARCHAR(255) DEFAULT NULL,
  `l3` VARCHAR(255) DEFAULT NULL,
  `fullpath` VARCHAR(511) DEFAULT NULL,
  `filename` VARCHAR(255) DEFAULT NULL, 
  `functype` VARCHAR(255) DEFAULT NULL,
  `funcname` VARCHAR(255) DEFAULT NULL,
  `linenumber` VARCHAR(255) DEFAULT NULL
);
-- ["SET "+part1[i]+" = (@var"+str(i+1)+" = \'Y\');\n" for i in range(len(part1))]
SET GLOBAL local_infile = 'ON';

LOAD data local INFILE 'C:/Users/18604/Desktop/research/ast_analysis_data_per_file.csv' INTO TABLE foutput 
  FIELDS TERMINATED BY ',' ENCLOSED BY '\"'
  LINES TERMINATED BY '\r\n' (l1,l2,l3,fullpath,filename,functype,funcname,linenumber);
select * from foutput;
select functype , count(*) as freq
from foutput
group by functype
;

create or replace table `file_only` (
`filepath` text DEFAULT null,
`features` text DEFAULT null
);

insert into file_only(filepath,features) 
select fullpath, coalesce(output.functype,"") from output
group by fullpath;
