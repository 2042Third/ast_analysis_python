import os
import csv
import random
import pandas as pd

def get_content( fname, source):
  fs = os.listdir(source)
  fs = [source+i for i in fs]
  for bigf in fs:
    print("Looking for {}...at {}".format(fname, bigf) )
    with open(bigf, newline='') as csvfile:
      rd = pd.read_csv("{}".format(bigf))
      for indx, t in rd.iterrows():
        if t[0].replace("/","").replace(" ","") == fname.replace("/","").replace(" ",""):
          return t[1]

def file_rd(a):
  out_dir = "./random_read/"
  bigq= "../../bigq_out/"
  if not os.path.exists(out_dir):
      os.makedirs(out_dir)

  content = get_content(a,bigq)
  oufile=open((str(out_dir)+a.replace('/', '-')),"w",encoding='utf8')
  oufile.write(content)
  oufile.close()
  print("File %s written to %s" % (a.replace('/', '-'), out_dir))


if __name__ == '__main__':
  fl=input("File:")
  a = file_rd(fl )
