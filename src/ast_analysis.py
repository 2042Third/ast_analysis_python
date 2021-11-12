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
import pandas as pd
from pathlib import Path

#files counts
count_files = 0
count_exclusion = 0


#User options
verbosity = False
all_files_in_repo=['../bigq_out/data-000000000000.csv','../bigq_out/data-000000000001.csv','../bigq_out/data-000000000002.csv','../bigq_out/data-000000000003.csv','../bigq_out/data-000000000004.csv','../bigq_out/data-000000000005.csv','../bigq_out/data-000000000006.csv','../bigq_out/data-000000000007.csv','../bigq_out/data-000000000008.csv','../bigq_out/data-000000000009.csv','../bigq_out/data-000000000010.csv','../bigq_out/data-000000000011.csv','../bigq_out/data-000000000012.csv','../bigq_out/data-000000000013.csv','../bigq_out/data-000000000014.csv','../bigq_out/data-000000000015.csv','../bigq_out/data-000000000016.csv','../bigq_out/data-000000000016.csv']


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
      try:
        visitor.visiting_this(code,offset+item)
      except:
        continue

    elif os.path.isdir(offset+item):
      if verbosity:
        print(offset+item)
      new_fs = list()

      new_fs = os.listdir(offset+item)
      try:
        find_all_file(visitor, new_fs,offset+item+os.path.sep)
      except:
        continue


def read_all_file(visitor, fs, offset):
  # global all_files_in_repo
  # trainxor = rd[[0]]
  for data_full_csv in fs:
    rd = pd.read_csv("../bigq_out/{}".format(data_full_csv))
    for indx, file_pair in rd.iterrows():
      # print(file_pair[0])
      global count_files
      count_files=count_files+1
      if verbosity and int(count_files/1000)==count_files/1000:
        global count_exclusion
        print("[{} from \"{}\", {} excluded]{}".format(indx,count_files,count_exclusion,data_full_csv))
      try:
        code = ast.parse(file_pair[1])
      except:
        # if verbosity:
        #   print("ERROR: Python cannot compile AST for {}!".format(data_full_csv))
        # global count_exclusion
        count_exclusion = 1+ count_exclusion 
        continue
      ast_node = code
      try:
        visitor.visiting_this(code,file_pair[0])
      except:
        continue

  

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
  read_all_file(visitor, fs,folder_name)
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

  

