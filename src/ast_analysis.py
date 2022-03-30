#coding=utf-8  
import ast
import subprocess
import sys
import ast_fund
import ast_custom
import ast_test
import ast_call
import pdb
import os
import time
import pandas as pd
from pathlib import Path

#files counts
count_files = 0
count_exclusion = 0


#User options
verbosity = False
stats_only = False
all_files_in_repo=['../bigq_out/data-000000000000.csv','../bigq_out/data-000000000001.csv','../bigq_out/data-000000000002.csv','../bigq_out/data-000000000003.csv','../bigq_out/data-000000000004.csv','../bigq_out/data-000000000005.csv','../bigq_out/data-000000000006.csv','../bigq_out/data-000000000007.csv','../bigq_out/data-000000000008.csv','../bigq_out/data-000000000009.csv','../bigq_out/data-000000000010.csv','../bigq_out/data-000000000011.csv','../bigq_out/data-000000000012.csv','../bigq_out/data-000000000013.csv','../bigq_out/data-000000000014.csv','../bigq_out/data-000000000015.csv','../bigq_out/data-000000000016.csv','../bigq_out/data-000000000016.csv']


def general_dump(node):
  print(ast.dump(node,indent=2))

def find_all_file(visitor, fs, offset):

  for item in fs:

    # print("Dir: %s" % offset+item)
    if(os.path.isfile(offset+item)) and (".py" == item[-3:]):
      global count_files
      count_files=count_files+1

      try:
        code = ast.parse(Path(offset+item , encoding="utf").read_text())
      except:
        # if verbosity:
        #   print("ERROR: Python cannot compile AST for {}!".format(offset+item))
        global count_exclusion
        count_exclusion = 1+ count_exclusion 
        continue

      if verbosity and int(count_files/1000)==count_files/1000:
          # global count_exclusion
          print("[read {} , {} excluded] {}".format(count_files,count_exclusion,offset+item))
      ast_node = code

      try:
        visitor.visiting_this(code,offset+item)
      except:
        continue

    elif os.path.isdir(offset+item):
      # if verbosity:
      #   print(offset+item)
      new_fs = list()
      new_fs = os.listdir(offset+item)
      try:
        find_all_file(visitor, new_fs,offset+item+os.path.sep)
      except:
        continue


def read_all_file(visitor, fs, offset):
  for data_full_csv in fs:
    rd = pd.read_csv("{}".format(data_full_csv))
    for indx, file_pair in rd.iterrows():
      global count_files
      count_files=count_files+1
      if verbosity and int(count_files/1000)==count_files/1000:
        global count_exclusion
        print("[{} from \"{}\", {} excluded]{}".format(indx,count_files,count_exclusion,data_full_csv))
      try:
        code = ast.parse(file_pair[1])
      except:
        count_exclusion = 1+ count_exclusion 
        continue
      ast_node = code
      try:
        visitor.visiting_this(code,file_pair[0])
      except:
        continue

def read_all_stats(visitor, fs, offset):
  for data_full_csv in fs:
    rd = pd.read_csv("../bigq_out/{}".format(data_full_csv))
    for indx, file_pair in rd.iterrows():
      global count_files
      count_files=count_files+1
      if verbosity and int(count_files/1000)==count_files/1000:
        global count_exclusion
        print("[{} from \"{}\", {:.2f}% progress ]".format(indx,count_files,100*(count_files/3844561))
          , end='\r', flush=True)
      visitor.log_stat(file_pair[0])



      
 

def clean_name(a):
  if a[-1]!=os.path.sep :
    return a+os.path.sep
  return a

def lib_check(fs):
  tSTART = time.time()

  oufile_name = "ast_with.csv"
  # oufile_name = "ast_analysis_data.csv"

  if stats_only:
    oufile_name = "ast_full_stats.csv"

  stats_file = "mining_stats.txt"

  visitor = ast_custom.Custom_Visitor() # custom only
  visitor._init_() # custom only
  # visitor = ast_call.Analysis_Ast_call()
  visitor.clean_file_db(oufile_name);
  folder_name = clean_name(sys.argv[1])
  if stats_only:
    read_all_stats(visitor, fs,folder_name)
  else:
    # find_all_file(visitor, fs,'') # files with folders
    read_all_file(visitor, fs,folder_name) # csv
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
  if open_file[-1] != '/' or open_file[-1] != '\\':
    open_file=open_file+'/'
  writing_file = False
  for inpts in sys.argv:
    if inpts[0] == '-':
      if inpts == "-v":
        verbosity = True
      elif inpts == "-w":
        writing_file = True
      # elif inpts == "-S":
      #   stats_only = True

  fs = os.listdir(open_file)
  if not stats_only:
    fs = [open_file+i for i in fs]
  print(fs)
  # quit()
  lib_check(fs)

  

