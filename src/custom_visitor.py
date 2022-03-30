#-*-coding:UTF-8-*-
import ast
import codecs
global mutex_lock
import os

class Target_Visitor(ast.NodeVisitor):
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
  async_function="ASC"# async
  with_attr_type="with_attribute"
  with_name_type="with_name"
  target_list_dynamic = ["getattr","setattr","delattr","hasattr","eval","exec"]
  target_list_functional = []
  target_list_decorators = []

  def _init_(self):
    self.count = 0
    self.subscrip_count = 0
    self.name_count = 0


  # a = func name
  # b = line number
  def log_current(self, a, b,func_type):
    tmp_l = self.get_current_line(self.current_name,func_type,a,b)
    # print(tmp_l)
    try:
      self.outfile.write(", ".join(tmp_l)+"\n")
    except: # Handles different languages
      self.outfile.write(", ".join([str(bytes(i, 'utf-8')) for i in tmp_l])+"\n")

  def log_stat(self, a):
    tmp_l = a.split(" ")[0]
    tmp_l = tmp_l.split("/")
    # print(tmp_l)
    self.outfile.write(", ".join(tmp_l)+"\n")
    

  
  # regex_resolve_level
  def rrl(self, f_path,level):
    lvls = f_path.split('/')
    # lvls = f_path.split(os.path.sep)
    if(level<=0):
      return lvls[-1]
    elif(len(lvls)>=level):
      return lvls[level-1]
    else:
      return ""
  
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

# visits defs

  def visit_With(self, node):
    for i in node.items:
      if isinstance(i.context_expr, ast.Call): # recur only on ast.Call
        self.visit(i.context_expr)

  # Can only be reached if it is from an ast.Call
  def visit_Name(self, node):
    self.count+=1
    print("\r\"With\" %s observed, recorded construct type \"Name\", value=\"%s\"" % (self.count,node.id), end='')
    self.log_current(node.id,node.lineno,self.with_name_type)

  # Can only be reached if it is from an ast.Call
  def visit_Attribute(self, node):
    self.count+=1
    print("\r\"With\" %s observed, recorded construct type \"Attribute\", value=\"%s\"" % (self.count,node.id), end='')
    self.log_current(node.attr,node.lineno,self.with_attr_type)
    self.visit(node.value)


  def visiting_this(self, node, name ):
    self.current_name = name
    self.visit(node) # always a With construct



  # def visit_Open(self, node):
  #   # print("[target] Open")
  #   self.log_current("with",node.lineno,self.async_function)
