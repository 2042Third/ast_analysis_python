#coding=utf-8  
import ast
import subprocess
import sys
import ast_fund
import ast_test
import ast_call
import pdb
import os
import time
from pathlib import Path

#files counts
count_files = 0
count_exclusion = 0


#User options
verbosity = False


def general_dump(node):
  print(ast.dump(node,indent=2))

def find_all_file(visitor, fs, offset):

  for item in fs:
    if(os.path.isfile(offset+item)) and (".py" == item[-3:]):
      global count_files
      count_files=count_files+1
      if verbosity:
        print("-{}".format(offset+item))
      try:
        code = ast.parse(Path(offset+item , encoding="utf").read_text())
      except:
        if verbosity:
          print("ERROR: Python cannot compile AST for {}!".format(offset+item))
        global count_exclusion
        count_exclusion = 1+ count_exclusion 
        continue
      ast_node = code
      visitor.visiting_this(code,offset+item)

    elif os.path.isdir(offset+item):
      if verbosity:
        print(offset+item)
      new_fs = list()

      new_fs = os.listdir(offset+item)
      find_all_file(visitor, new_fs,offset+item+os.path.sep)

def clean_name(a):
  if a[-1]!=os.path.sep :
    return a+os.path.sep
  return a

def lib_check(fs):
  tSTART = time.time()
  oufile_name = "ast_analysis_data.csv"

  stats_file = "mining_stats.txt"

  visitor = ast_call.Analysis_Ast_call()
  visitor.clean_file_db(oufile_name);
  folder_name = clean_name(sys.argv[1])
  find_all_file(visitor, fs,folder_name)
  inp = ' '
  visitor.close_file_db()
  print("\nFinished search for "+str(count_files)+" files"+" ({:.02f}s)".format(time.time() - tSTART))

    # visitor.write_to_file(oufile_name)
  print("written to file \"{}\"".format(oufile_name))
  oufile=open(stats_file,"w")
  oufile.close()
  oufile= open(stats_file,"a")

  oufile.write("Directory: {}\n".format(folder_name))
  oufile.write("total files: {}\n".format(str(count_files)))
  oufile.write("error files: {}\n".format(str(count_exclusion)))
  oufile.write("Time taken: {:.02f} sec.\n".format(time.time() - tSTART))

  oufile.close()

if __name__ == '__main__':
  open_file =sys.argv[1]

  writing_file = False
  for inpts in sys.argv:
    if inpts[0] == '-':
      if inpts == "-v":
        verbosity = True
      elif inpts == "-w":
        writing_file = True

  fs = os.listdir(open_file)

  print(fs)
  lib_check(fs)

  

