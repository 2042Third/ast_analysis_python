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
  def visit_Call(self, node):
    # global mutex_lock
    # mutex_lock.acquire()
    if isinstance(node.func, ast.Name):
      if("getattr" == node.func.id):
        self.getattr_c = self.getattr_c + 1
        self.c_init_env("getattr",self.current_name)
        self.eval_env["getattr"][self.current_name].append(node.lineno)
      elif("setattr" == node.func.id):
        self.setattr_c = self.setattr_c + 1
        self.c_init_env("setattr",self.current_name)
        self.eval_env["setattr"][self.current_name].append(node.lineno)
      elif("delattr" == node.func.id):
        self.delattr_c = self.delattr_c + 1
        self.c_init_env("delattr",self.current_name)
        self.eval_env["delattr"][self.current_name].append(node.lineno)
      elif("hasattr" == node.func.id):
        self.hasattr_c = self.hasattr_c + 1
        self.c_init_env("hasattr",self.current_name)
        self.eval_env["hasattr"][self.current_name].append(node.lineno)
      elif("eval" == node.func.id):
        self.eval_c = self.eval_c + 1
        self.c_init_env("eval",self.current_name)
        self.eval_env["eval"][self.current_name].append(node.lineno)
      elif("exec" == node.func.id):
        self.exec_c = self.exec_c + 1
        self.c_init_env("exec",self.current_name)
        self.eval_env["exec"][self.current_name].append(node.lineno)
    # mutex_lock.release()
    for i in node.args:
      if isinstance(i, ast.Name):
        # mutex_lock.acquire()
        if("getattr" == i.id):
          self.getattr_c = self.getattr_c + 1
          self.c_init_env("getattr",self.current_name)
          self.eval_env["getattr"][self.current_name].append(node.lineno)
        elif("setattr" == i.id):
          self.setattr_c = self.setattr_c + 1
          self.c_init_env("setattr",self.current_name)
          self.eval_env["setattr"][self.current_name].append(node.lineno)
        elif("delattr" == i.id):
          self.delattr_c = self.delattr_c + 1
          self.c_init_env("delattr",self.current_name)
          self.eval_env["delattr"][self.current_name].append(node.lineno)
        elif("hasattr" == i.id):
          self.hasattr_c = self.hasattr_c + 1
          self.c_init_env("hasattr",self.current_name)
          self.eval_env["hasattr"][self.current_name].append(node.lineno)
        elif("eval" == i.id):
          self.eval_c = self.eval_c + 1
          self.c_init_env("eval",self.current_name)
          self.eval_env["eval"][self.current_name].append(node.lineno)
        elif("exec" == i.id):
          self.exec_c = self.exec_c + 1
          self.c_init_env("exec",self.current_name)
          self.eval_env["exec"][self.current_name].append(node.lineno)
        # mutex_lock.release()


    if isinstance(node, ast.Name):
      self.name_count = self.name_count+1
    
    self.count=self.count+1
    self.generic_visit(node)

  def visit_Name(self, node):
    # global mutex_lock
    # mutex_lock.acquire()
    self.name_count = self.name_count+1
    # mutex_lock.release()
    self.generic_visit(node)

  def visit_Subscript(self,node):
    # global mutex_lock
    # mutex_lock.acquire()
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