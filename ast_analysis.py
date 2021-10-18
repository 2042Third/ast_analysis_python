import ast
import subprocess
import sys
import ast_fund
import ast_test
import ast_call
import pdb
import time

#files counts
count_files = 0
count_exclusion = 0


#User options
verbosity = False


def general_dump(node):
  print(ast.dump(node,indent=2))

def find_all_file(visitor, fs, offset):
   for item in fs:
    if ".py" == item[-3:]:
      global count_files
      count_files=count_files+1
      if verbosity:
        print("-{}".format(offset+item))
      
      p = subprocess.Popen(["cat", offset+item ],stdin=subprocess.PIPE 
                                                              ,stdout=subprocess.PIPE,
                                                              universal_newlines=True)
      #print(p.stdout.read())
      try:
        code = ast.parse(p.stdout.read())
      except:
        if verbosity:
          print("ERROR: Python cannot compile AST for {}!".format(offset+item))
        global count_exclusion
        count_exclusion = 1+ count_exclusion 
        continue
      ast_node = code
      visitor.visiting_this(code,offset+item)
    
      p.terminate()
    elif not "." in item and not len(item) == 0:
      if verbosity:
        print(offset+item)
      new_fs = list()
      fol = subprocess.Popen(["ls",offset+item],stdin=subprocess.PIPE 
                                                          ,stdout=subprocess.PIPE,
                                                           universal_newlines=True)
      all_fi = fol.stdout.read()
      new_fs = all_fi.split("\n")
      find_all_file(visitor, new_fs,offset+item+'/')

def lib_check(fs):
  tSTART = time.time()
  oufile_name = "ast_analysis_data.csv"

  visitor = ast_call.Analysis_Ast_call()
  visitor.clean_file_db(oufile_name);
  find_all_file(visitor, fs,sys.argv[1])
  inp = ' '
  visitor.close_file_db()
  print("\nFinished search for "+str(count_files)+" files"+" ({:.02f}s)".format(time.time() - tSTART))
  if writing_file:
    # visitor.write_to_file(oufile_name)
    print("written to file \"{}\"".format(oufile_name))
  else:
    while len(inp)!= 0 or inp=="n":
      inp = input("dump? (full_dump/call/getattr/setattr/.../dyna) ")
      if inp == 'full_dump':
        general_dump(code)
      elif inp == 'sbc':
        print(visitor.get_subscript_count())
      elif inp == 'call':
        print(visitor.get_call_count())
      elif inp == 'name':
        print(visitor.get_name_count())
      elif inp == "getattr":
        print(visitor.get_getattr_count())
      elif inp == "delattr":
        print(visitor.get_delattr_count())
      elif inp == "setattr":
        print(visitor.get_setattr_count())
      elif inp == "hasattr":
        print(visitor.get_hasattr_count())
      elif inp == "eval_env":
        inp2 = 'Na'
        while len(inp2) != 0 :
          inp2 = input("Which dynamic feature: ")
          for i in visitor.get_eval_env(inp2):
              print(i)
      elif inp == "WT":
        oufile_name = "ast_analysis.json"
        visitor.write_to_file(oufile_name)
        print("written to file \"{}\"".format(oufile_name))
      elif inp == "dyna":
        print("hasattr {}".format(visitor.get_hasattr_count()))
        print("getattr {}".format(visitor.get_getattr_count()))
        print("delattr {}".format(visitor.get_delattr_count()))
        print("setattr {}".format(visitor.get_setattr_count()))
        print("eval {}".format(visitor.get_eval_count()))
        print("exec {}".format(visitor.get_exec_count()))
      elif inp == "err":
        print("AST error for {} files".format(count_exclusion))
if __name__ == '__main__':
  open_file =sys.argv[1]
  fol = subprocess.Popen(["ls",open_file],stdin=subprocess.PIPE 
                                                          ,stdout=subprocess.PIPE,
                                                          universal_newlines=True)
  
  all_files = fol.stdout.read()
  writing_file = False
  for inpts in sys.argv:
    if inpts[0] == '-':
      if inpts == "-v":
        verbosity = True
      elif inpts == "-w":
        writing_file = True
  fs = all_files.split("\n")

  print(fs)
  lib_check(fs)

  
  fol.terminate()

