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