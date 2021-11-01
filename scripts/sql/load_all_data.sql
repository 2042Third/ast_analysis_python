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
	LINES TERMINATED BY '\n' (l1,l2,l3,fullpath,filename,functype,funcname,linenumber);

SHOW WARNINGS;
SELECT * FROM output;

create table `func_dyn` (
`Organization` VARCHAR(255) DEFAULT null,
`DynCount` VARCHAR(255) DEFAULT null,
`FuncCount` VARCHAR(255) DEFAULT null
);
create table `func_dyn_dec` (
`Organization` VARCHAR(255) DEFAULT null,
`DynCount` VARCHAR(255) DEFAULT null,
`FuncCount` VARCHAR(255) DEFAULT null,
`DecCount` VARCHAR(255) DEFAULT null
);
insert into func_dyn (Organization,DynCount,FuncCount) select t1.l2,  coalesce(t2.orgDYN,0) as "Dynamic", coalesce(t1.orgFNL,0) as "Functional" from
(select l2, COUNT(*) as orgFNL from output where functype = "FNL" GROUP by l2) as t1
left join
(select l2, COUNT(*) as orgDYN from output where functype = "DYN" GROUP by l2) as t2
on t1.l2 = t2.l2;
-- select * from func_dyn;
insert into func_dyn_dec (Organization,DynCount,FuncCount,DecCount) select t1.Organization, t1.DynCount, t1.FuncCount, coalesce(t2.orgDEC,0) as "DecCount"
from func_dyn as t1
left join
(select l2, COUNT(*) as orgDEC from output where functype = "DEC" GROUP by l2) as t2
on t1.Organization = t2.l2;
select * from func_dyn_dec;

select funcname , count(*) from output where functype = "DYN" group by funcname;

-- project-wise

create table `func_dyn_proj` (
`Project` VARCHAR(255) DEFAULT null,
`DynCount` VARCHAR(255) DEFAULT null,
`FuncCount` VARCHAR(255) DEFAULT null
);
create table `func_dyn_dec_proj` (
`Project` VARCHAR(255) DEFAULT null,
`DynCount` VARCHAR(255) DEFAULT null,
`FuncCount` VARCHAR(255) DEFAULT null,
`DecCount` VARCHAR(255) DEFAULT null
);
insert into func_dyn_proj (Project,DynCount,FuncCount) select t1.l3,  coalesce(t2.projDYN,0) as "Dynamic", coalesce(t1.projFNL,0) as "Functional" from
(select l3, COUNT(*) as projFNL from output where functype = "FNL" GROUP by l3) as t1
left join
(select l3, COUNT(*) as projDYN from output where functype = "DYN" GROUP by l3) as t2
on t1.l3 = t2.l3;
-- select * from func_dyn;
insert into func_dyn_dec_proj (Project,DynCount,FuncCount,DecCount) select t1.Project, t1.DynCount, t1.FuncCount, coalesce(t2.projDEC,0) as "DecCount"
from func_dyn_proj as t1
left join
(select l3, COUNT(*) as projDEC from output where functype = "DEC" GROUP by l3) as t2
on t1.Project = t2.l3;
select * from func_dyn_dec;

select funcname , count(*) from output where functype = "DYN" group by funcname;

-- write to file
-- organization frequency all 
SELECT * INTO OUTFILE 'C:/Users/18604/Desktop/research/ast_analysis/outputs/organization/organization_freq.csv'
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  FROM func_dyn_dec;
-- organization dyn only
select * from func_dyn_dec where DynCount>0;
-- organization func only
select * from func_dyn_dec where FuncCount>0;
-- organization dec only
select * from func_dyn_dec where DecCount>0;  
-- project frequency all 
SELECT * INTO OUTFILE 'C:/Users/18604/Desktop/research/ast_analysis/outputs/project/project_freq.csv'
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  FROM func_dyn_dec_proj;
-- project dyn only
select * from func_dyn_dec_proj where DynCount>0;
-- project func only
select * from func_dyn_dec_proj where FuncCount>0;
-- project dec only
select * from func_dyn_dec_proj where DecCount>0;  
 