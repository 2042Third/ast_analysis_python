DROP DATABASE astmine;
CREATE SCHEMA astmine;
USE astmine;

FLUSH privileges;

SHOW GLOBAL VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 'ON';
SHOW GLOBAL VARIABLES LIKE 'local_infile';

USE astmine;

create or replace table `statsonly` (
`l2` VARCHAR(255) DEFAULT NULL,
`l3` VARCHAR(255) DEFAULT NULL
);

create or replace table `orgf` (
`freq` VARCHAR(255) DEFAULT NULL
);

create or replace table `projf` (
`freq` VARCHAR(255) DEFAULT NULL
);

load data local infile 'C:/Users/18604/Desktop/research/ast_analysis_data.csv' into table statsonly 
  fields terminated by ', ' enclosed by '\"'
  lines terminated by '\n' (l2,l3);

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

LOAD data local INFILE 'C:/Users/18604/Desktop/research/fixed_ast_analysis_data_async.csv' INTO TABLE output 
  FIELDS TERMINATED BY ', ' ENCLOSED BY '\"'
  LINES TERMINATED BY '\r\n' (l1,l2,l3,fullpath,filename,functype,funcname,linenumber);
update output
set output.l1 = trim(trailing "\"\'" from TRIM(LEADING "b\'\"" FROM output.l1)) 
,  output.l2 = trim(trailing "\"\'" from TRIM(LEADING "b\'\"" FROM output.l2)) 
,  output.l3 = trim(trailing "\"\'" from TRIM(LEADING "b\'\"" FROM output.l3)) 
,  output.fullpath = trim(trailing "\"\'" from TRIM(LEADING "b\'\"" FROM output.fullpath)) 
,  output.filename = trim(trailing "\"\'" from TRIM(LEADING "b\'\"" FROM output.filename)) 
,  output.functype = trim(trailing "\"\'" from TRIM(LEADING "b\'\"" FROM output.functype)) 
,  output.funcname = trim(trailing "\"\'" from TRIM(LEADING "b\'\"" FROM output.funcname)) 
,  output.linenumber = trim(trailing "\"\'" from TRIM(LEADING "b\'\"" FROM output.linenumber)) 
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
`DecCount` VARCHAR(255) DEFAULT null,
`WithCount` VARCHAR(255) DEFAULT null,
`AsyncCount` VARCHAR(255) DEFAULT null
);

insert into func_dyn_dec (Organization,DynCount,FuncCount,DecCount,WithCount,AsyncCount) 
select output.l2,  coalesce(0),  coalesce(0),  coalesce(0),  coalesce(0),  coalesce(0) from output 
group by output.l2 ;

update  func_dyn_dec as t1,  (select l2, COUNT(*) as orgDEC from output where functype = "DEC" GROUP by l2) as t2
set t1.DecCount=coalesce(t2.orgDEC,0)
where t1.Organization = t2.l2;
update  func_dyn_dec as t1,  (select l2, COUNT(*) as orgFNL from output where functype = "FNL" GROUP by l2) as t2
set t1.FuncCount =coalesce(t2.orgFNL,0)
where t1.Organization = t2.l2;
update  func_dyn_dec as t1,  (select l2, COUNT(*) as orgDYN from output where functype = "DYN" GROUP by l2) as t2
set t1.DynCount =t2.orgDYN
where t1.Organization = t2.l2;
update  func_dyn_dec as t1,  (select l2, COUNT(*) as orgDYN from output where funcname = "with" GROUP by l2) as t2
set t1.WithCount =t2.orgDYN
where t1.Organization = t2.l2;
update  func_dyn_dec as t1,  (select l2, COUNT(*) as orgDYN from output where functype = "ASC" and not funcname = "with" GROUP by l2) as t2
set t1.AsyncCount =t2.orgDYN
where t1.Organization = t2.l2;



-- project-wise


create or replace table `func_dyn_dec_proj` (
`Project` text DEFAULT null,
`DynCount` VARCHAR(255) DEFAULT null,
`FuncCount` VARCHAR(255) DEFAULT null,
`DecCount` VARCHAR(255) DEFAULT null,
`WithCount` VARCHAR(255) DEFAULT null,
`AsyncCount` VARCHAR(255) DEFAULT null
);
insert into func_dyn_dec_proj (Project,DynCount,FuncCount,DecCount,WithCount,AsyncCount) 
select output.l3,  coalesce(0),  coalesce(0),  coalesce(0),  coalesce(0),  coalesce(0) from output 
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
update  func_dyn_dec_proj as t1,  (select l3, COUNT(*) as orgDYN from output where funcname = "with" GROUP by l3) as t2
set t1.WithCount =t2.orgDYN
where t1.Project = t2.l3;
update  func_dyn_dec_proj as t1,  (select l3, COUNT(*) as orgDYN from output where functype = "ASC" and not funcname = "with" GROUP by l3) as t2
set t1.AsyncCount =t2.orgDYN
where t1.Project = t2.l3;


-- write to file
-- organization frequency all 
SELECT *  FROM func_dyn_dec;
-- organization dyn only
create or replace table `org_dyn` (`Organization` text DEFAULT null,`DynCount` VARCHAR(255) DEFAULT null,`FuncCount` VARCHAR(255) DEFAULT null,`DecCount` VARCHAR(255) DEFAULT null
,`WthCount` VARCHAR(255) DEFAULT null,`AscCount` VARCHAR(255) DEFAULT null);
 insert into org_dyn (Organization,DynCount,FuncCount,DecCount,WthCount,AscCount)  select * from (select  * from func_dyn_dec  where DynCount>0 ) as org_dyn;
-- organization func only
create or replace table `org_func` (`Organization` text DEFAULT null,`DynCount` VARCHAR(255) DEFAULT null,`FuncCount` VARCHAR(255) DEFAULT null,`DecCount` VARCHAR(255) DEFAULT null
,`WthCount` VARCHAR(255) DEFAULT null,`AscCount` VARCHAR(255) DEFAULT null);
 insert into org_func (Organization,DynCount,FuncCount,DecCount,WthCount,AscCount)  select * from (select  * from func_dyn_dec  where FuncCount>0 ) as org_func;
-- organization dec only
create or replace table `org_dec` (`Organization` text DEFAULT null,`DynCount` VARCHAR(255) DEFAULT null,`FuncCount` VARCHAR(255) DEFAULT null,`DecCount` VARCHAR(255) DEFAULT null
,`WthCount` VARCHAR(255) DEFAULT null,`AscCount` VARCHAR(255) DEFAULT null);
 insert into org_dec (Organization,DynCount,FuncCount,DecCount,WthCount,AscCount)  select * from (select  * from func_dyn_dec  where DecCount>0 ) as org_dec;
create or replace table `org_wth` (`Organization` text DEFAULT null,`DynCount` VARCHAR(255) DEFAULT null,`FuncCount` VARCHAR(255) DEFAULT null,`DecCount` VARCHAR(255) DEFAULT null
,`WthCount` VARCHAR(255) DEFAULT null,`AscCount` VARCHAR(255) DEFAULT null);
 insert into org_wth (Organization,DynCount,FuncCount,DecCount,WthCount,AscCount)  select * from (select  * from func_dyn_dec  where WithCount>0 ) as org_wth;
create or replace table `org_asc` (`Organization` text DEFAULT null,`DynCount` VARCHAR(255) DEFAULT null,`FuncCount` VARCHAR(255) DEFAULT null,`DecCount` VARCHAR(255) DEFAULT null
,`WthCount` VARCHAR(255) DEFAULT null,`AscCount` VARCHAR(255) DEFAULT null);
 insert into org_asc (Organization,DynCount,FuncCount,DecCount,WthCount,AscCount)  select * from (select  * from func_dyn_dec  where AsyncCount>0 ) as org_asc;

-- project frequency all 
SELECT * FROM func_dyn_dec_proj;
-- project dyn only
create or replace table `proj_dyn` (`Project` text DEFAULT null,`DynCount` VARCHAR(255) DEFAULT null,`FuncCount` VARCHAR(255) DEFAULT null,`DecCount` VARCHAR(255) DEFAULT null
,`WthCount` VARCHAR(255) DEFAULT null,`AscCount` VARCHAR(255) DEFAULT null);
 insert into proj_dyn (Project,DynCount,FuncCount,DecCount,WthCount,AscCount)  select * from (select  * from func_dyn_dec_proj  where DynCount>0 ) as proj_dyn;
-- project func only
create or replace table `proj_func` (`Project` text DEFAULT null,`DynCount` VARCHAR(255) DEFAULT null,`FuncCount` VARCHAR(255) DEFAULT null,`DecCount` VARCHAR(255) DEFAULT null
,`WthCount` VARCHAR(255) DEFAULT null,`AscCount` VARCHAR(255) DEFAULT null);
 insert into proj_func (Project,DynCount,FuncCount,DecCount,WthCount,AscCount)  select * from (select  * from func_dyn_dec_proj  where FuncCount>0 ) as proj_func;
-- project dec only
create or replace table `proj_dec` (`Project` text DEFAULT null,`DynCount` VARCHAR(255) DEFAULT null,`FuncCount` VARCHAR(255) DEFAULT null,`DecCount` VARCHAR(255) DEFAULT null
,`WthCount` VARCHAR(255) DEFAULT null,`AscCount` VARCHAR(255) DEFAULT null);
 insert into proj_dec (Project,DynCount,FuncCount,DecCount,WthCount,AscCount)  select * from (select  * from func_dyn_dec_proj  where DecCount>0 ) as proj_dec;
create or replace table `proj_wth` (`Organization` text DEFAULT null,`DynCount` VARCHAR(255) DEFAULT null,`FuncCount` VARCHAR(255) DEFAULT null,`DecCount` VARCHAR(255) DEFAULT null
,`WthCount` VARCHAR(255) DEFAULT null,`AscCount` VARCHAR(255) DEFAULT null);
 insert into proj_wth (Organization,DynCount,FuncCount,DecCount,WthCount,AscCount)  select * from (select  * from func_dyn_dec  where WithCount>0 ) as proj_wth;
create or replace table `proj_asc` (`Organization` text DEFAULT null,`DynCount` VARCHAR(255) DEFAULT null,`FuncCount` VARCHAR(255) DEFAULT null,`DecCount` VARCHAR(255) DEFAULT null
,`WthCount` VARCHAR(255) DEFAULT null,`AscCount` VARCHAR(255) DEFAULT null);
 insert into proj_asc (Organization,DynCount,FuncCount,DecCount,WthCount,AscCount)  select * from (select  * from func_dyn_dec  where AsyncCount>0 ) as proj_asc;
create view p_dyn as
select * from proj_dyn ;
create view p_dfunc as
select * from proj_func ;

create or replace table `functional_frequency_rank` (`funcname` text DEFAULT null,`freq` int default 0);
insert into functional_frequency_rank(funcname,freq)
select funcname , count(*) as freq from output 
where functype = "FNL" 
group by funcname
order by count(*) DESC;
create or replace table `async_frequency_rank` (`funcname` text DEFAULT null,`freq` int default 0);
insert into async_frequency_rank(funcname,freq)
select funcname , count(*) as freq from output 
where functype = "ASC" and not funcname = "with"
group by funcname
order by count(*) DESC;


create or replace table `decorators_frequency_rank_full` (`funcname` text DEFAULT null,`freq` int default 0);
insert into decorators_frequency_rank_full(funcname,freq)
select funcname , count(*) as freq from output 
where functype = "DEC" 
group by funcname
order by count(*) desc;

create or replace table `dynamic_frequency_rank` (`funcname` text DEFAULT null,`freq` int default 0);
insert into dynamic_frequency_rank(funcname,freq)
select funcname , count(*) as freq from output 
where functype = "DYN" 
group by funcname
order by count(*) desc
;
create or replace table `all_frequency_rank` (`funcname` text DEFAULT null,`freq` int default 0);
insert into all_frequency_rank(funcname,freq)
select funcname , count(*) as freq from output  
group by funcname
order by count(*) desc
;



create or replace table `file_only` (
`filepath` VARCHAR(511) DEFAULT null,
`features` VARCHAR(511) DEFAULT null
);

insert into file_only(filepath,features) 
select fullpath, coalesce("") from output
group by fullpath;

-- select * from file_only;

create or replace table `fnl_only` (
`fullpath` VARCHAR(511) DEFAULT null
);
create or replace table `dyn_only` (
`fullpath` VARCHAR(511) DEFAULT null
);
create or replace table `dec_only` (
`fullpath` VARCHAR(511) DEFAULT null
);
create or replace table `wth_only` (
`fullpath` VARCHAR(511) DEFAULT null
);
create or replace table `asc_only` (
`fullpath` VARCHAR(511) DEFAULT null
);
insert into fnl_only(fullpath)
select fullpath from output where functype = "FNL" GROUP by fullpath;
insert into dyn_only(fullpath)
select fullpath from output where functype = "DYN" GROUP by fullpath;
insert into dec_only(fullpath)
select fullpath from output where functype = "DEC" GROUP by fullpath;
insert into dec_only(fullpath)
select fullpath from output where functype = "ASC" and not funcname = "with" GROUP by fullpath;
insert into dec_only(fullpath)
select fullpath from output where funcname = "with" GROUP by fullpath;

-- making these unique keys sped things up more than 30000%, or more.
alter table file_only add unique(filepath);
alter table fnl_only add unique(fullpath);
alter table dyn_only add unique(fullpath);
alter table dec_only add unique(fullpath);
alter table wth_only add unique(fullpath);
alter table asc_only add unique(fullpath);

update file_only as t1, fnl_only
set t1.features=" FNL"
where t1.filepath = fnl_only.fullpath;
update file_only as t1, dyn_only
set t1.features=concat( t1.features ," DYN")
where t1.filepath = dyn_only.fullpath;
update file_only as t1, dec_only
set t1.features=concat( t1.features ," DEC")
where t1.filepath = dec_only.fullpath;
update file_only as t1, wth_only
set t1.features=concat( t1.features ," WTH")
where t1.filepath = dec_only.fullpath;
update file_only as t1, asc_only
set t1.features=concat( t1.features ," ASC")
where t1.filepath = dec_only.fullpath;


select features, count(*) as freq from file_only as file_only_with_freq group by features order by count(*) DESC;

insert into orgf(freq)
select count(*) from statsonly group by l2;
insert into projf(freq)
select count(*) from statsonly group by l3;

select count(*) from orgf;
select count(*) from projf;


-- WITH/ASYNC PART

