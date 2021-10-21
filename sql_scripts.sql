USE astmine;
SELECT * FROM output;
select funcname, COUNT(*) 
from output 
where funcname = "getattr"
;
select *, COUNT(*) from output;
SELECT  *,   COUNT(fullpath) FROM   output where funcname = "eval" GROUP by fullpath;
-- select * from output where fullpath = "gnofract4d-4.3/fract4d_compiler/codegen.py" ;
-- select filename, COUNT(*) as fileOccurence from output GROUP by filename;
select functype, COUNT(*) as projectOccurence from output GROUP by functype;
select fullpath,functype, l2, COUNT(*) as organizationOccurence from output GROUP by l2;

--create a table displaying the frequency of each type
select t1.l2, coalesce(t1.orgFNL,0) as "Functional", coalesce(t2.orgDYN,0) as "Dynamic" from
(select l2, COUNT(*) as orgFNL from output where functype = "FNL" GROUP by l2) as t1
left join
(select l2, COUNT(*) as orgDYN from output where functype = "DYN" GROUP by l2) as t2
on t1.l2 = t2.l2;
--IF(OR(OR(AND(B:B=0,C:C=0),AND(C:C=0,D:D=0)),AND(B:B=0,D:D=0)),0,1)


USE astmine;

-- select  COUNT(*) as total from func_dyn_dec as fdd;
-- select COUNT(*) as once  from func_dyn_dec as fdd where DynCount="1";
-- select  COUNT(*) as gtt_once from func_dyn_dec as fdd where DynCount>"1"; 

-- DECLARE @gttonce int;
SET @gttonce=(select  COUNT(*) as gtt_once from func_dyn_dec as fdd where DynCount>"1");
select @gttonce;
