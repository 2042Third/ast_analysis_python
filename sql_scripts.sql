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