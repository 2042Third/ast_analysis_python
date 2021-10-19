import ast
# from multicore_ast_analysis import *
#import threading
global mutex_lock

class Analysis_Ast_call(ast.NodeVisitor):
  count = 1
  subscrip_count = 1
  name_count = 1
  getattr_c = 0
  setattr_c = 0
  delattr_c = 0
  hasattr_c = 0
  eval_c = 0
  exec_c = 0
  eval_env = {}
  current_name=""
  outfile_name =""
  outfile=""
  dynamic_function="DYN"# dynamic
  functional_function="FNL"# functional
  decorator_function="DEC"# decorator
  target_list_dynamic = ["getattr","setattr","delattr","hasattr","eval","exec"]
  target_list_functional = []
  target_list_decorators = []

  # global mutex_lock 
  def _init_(self):
    self.count = 0
    self.subscrip_count = 0
    self.name_count = 0
 # def adding(self, a):

  def get_call_count(self):
    return self.count

  def get_getattr_count(self):
    return self.getattr_c 
  def get_setattr_count(self):
    return self.setattr_c 
  def get_delattr_count(self):
    return self.delattr_c 
  def get_hasattr_count(self):
    return self.hasattr_c 
  def get_eval_count(self):
    return self.eval_c
  def get_exec_count(self):
    return self.exec_c
  def get_eval_env(self, name):
    return self.eval_env[name]

  def get_subscript_count(self):
    return self.subscrip_count

  def get_name_count(self):
    return self.name_count

  def c_init_env(self, name, file_name):
    if (name in self.eval_env ):
      if (not file_name in self.eval_env[name] ):
        self.eval_env[name][file_name] = []
      return
    else:
      self.eval_env[name] = {} 
      self.eval_env[name][file_name] = []
      return 

  def visiting_this(self, node, name ):
    self.current_name = name
    self.visit(node)

  # a = func name
  # b = line number
  def log_current(self, a, b,func_type):
    tmp_l = self.get_current_line(self.current_name,func_type,a,b)
    self.outfile.write(", ".join(tmp_l)+"\n")

  
  # regex_resolve_level
  def rrl(self, f_path,level):
    lvls = f_path.split("/")
    if(level<=0):
      return lvls[-1]
    elif(len(lvls)>=level):
      return lvls[level-1]
    else:
      return ""

  def visit_Call(self, node):
    if isinstance(node.func, ast.Name):
      if(node.func.id in self.target_list_dynamic):
        self.log_current(node.func.id,node.lineno,self.dynamic_function)
    for i in node.args:
      if isinstance(i, ast.Name):
        if(i.id in self.target_list_dynamic):
          self.log_current(i.id,node.lineno,self.dynamic_function)
    self.generic_visit(node)

  def visit_FunctionDef(self, node):
    for i in node.decorator_list:
      if isinstance(i, ast.Name):
        self.log_current(i.id,node.lineno,self.decorator_function)

    self.generic_visit(node)

  def visit_AsyncFunctionDef(self, node):
    for i in node.decorator_list:
      if isinstance(i, ast.Name):
        self.log_current(i.id,node.lineno,self.decorator_function)

    self.generic_visit(node)

  def visit_ClassDef(self, node):
    for i in node.decorator_list:
      if isinstance(i, ast.Name):
        self.log_current(i.id,node.lineno,self.decorator_function)

    self.generic_visit(node)

  def visit_Lambda(self, node):
    self.log_current("lambda",node.lineno,self.functional_function)
    self.generic_visit(node)

  def visit_SetComp(self, node):
    self.log_current("setComp",node.lineno,self.functional_function)
    self.generic_visit(node)

  def visit_DictComp(self, node):
    self.log_current("dictComp",node.lineno,self.functional_function)
    self.generic_visit(node)

  def visit_Yield(self, node):
    self.log_current("yield",node.lineno,self.functional_function)
    self.generic_visit(node)

  def visit_YieldFrom(self, node):
    self.log_current("yieldFrom",node.lineno,self.functional_function)
    self.generic_visit(node)


  def visit_ListComp(self, node):
    self.log_current("listComp",node.lineno,self.functional_function)
    self.generic_visit(node)

  def visit_Name(self, node):
    self.generic_visit(node)

  def visit_Subscript(self,node):
    self.subscrip_count = self.subscrip_count+1
    # mutex_lock.release()
    self.generic_visit(node)
  def write_to_file(self,oufile_name):
    oufile=open(oufile_name,"w")
    oufile.write("{\n")
    for key in self.eval_env:
      oufile.write("\"{}\"".format(key))
      oufile.write(":{\n")
      
      i=0
      for keys in self.eval_env[key]:
        # print(self.eval_env[key][keys])

        if i != 0:
          oufile.write(",\n\t{:>20}:{}".format("\""+keys+"\"",self.eval_env[key][keys]))
        else:
          oufile.write("\t{:>20}:{}".format("\""+keys+"\"",self.eval_env[key][keys]))
        i+=1
      oufile.write("\t},\n")

    oufile.write("}\n")
    oufile.close()
  def get_current_line(self,fpath,func_type,func_name,lineno):
    tmp=list()
    tmp.append(self.rrl(fpath,1)) # path level 1
    tmp.append(self.rrl(fpath,2)) # path level 2
    tmp.append(self.rrl(fpath,3)) # path level 3
    tmp.append(fpath) # full path
    tmp.append(self.rrl(fpath,-1)) # file name 
    tmp.append(func_type)
    tmp.append(func_name)
    tmp.append(str(lineno)) # line number
    out_tmp=["\""+x+"\"" for x in tmp]
    return out_tmp
  def clean_file_db(self,oufile_name):
    oufile=open(oufile_name,"w")
    oufile.close()
    self.outfile_name=oufile_name
    self.outfile = open(oufile_name,"a")
  def close_file_db(self):
    self.outfile.close()