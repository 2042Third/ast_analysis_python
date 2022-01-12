import os
import csv
import random
import pandas as pd

class rand_rd(object):
  out_dir = ''
  bigq='../../bigq_out/'
  def __init__(self):
    super(rand_rd, self).__init__()
    self.out_dir = "random_read/"
    self.out_dir = os.path.join("./",self.out_dir)
    if not os.path.exists(self.out_dir):
      os.makedirs(self.out_dir)
    print("Output to %s" % self.out_dir)

  
  def get_content(self, fname):
    fs = os.listdir(self.bigq)
    fs = [self.bigq+i for i in fs]
    for bigf in fs:
      print("Looking for {} at {}".format(fname, bigf) )
      with open(bigf, newline='') as csvfile:
        rd = pd.read_csv("{}".format(bigf))
        for indx, t in rd.iterrows():
          if t[0].replace("/","").replace(" ","") == fname.replace("/","").replace(" ",""):
            return t[1]

  def gen_rand(self, f_size):
    for i in range(5):
      random.randint(0, f_size)
    return int(random.uniform(0, f_size))


  def ps_filter(self, a,b):
    return a in b

  def start(self, fname, fltr):
    indx=0
    ec=0
    gotten=1
    file_size = 0
    with open(fname, newline='') as csvfile:
      rands = csv.reader(csvfile, delimiter=',', quotechar='\"')
      for i in rands:
        file_size+=1
    while True:
      counter = 1
      with open(fname, newline='') as csvfile:
        rands = csv.reader(csvfile, delimiter=',', quotechar='\"')
        print(file_size)
        # quit()
        oufile=open((str(self.out_dir)+"tmp{}.py".format(str(gotten-1))),"w")
        stopper = self.gen_rand(file_size)
        print("[one new] {} {} {}".format(gotten, stopper , counter))
        counter = 1
        for i in rands:
          if counter%stopper==0:
            line_num = i[7]
            file_name = i[3].strip().replace("\"","")
            func_name = i[6].strip()
            print("\'%s\'"%file_name)
            print("\'%s\'"%func_name)
            if self.ps_filter(func_name,fltr):
              break;
            file_content = self.get_content(file_name)
            print("{} found {}\n".format(stopper,gotten))
            gotten=gotten+1
            try:
              oufile.write("# \'{}\' at line {}, file name \'{}\'\n".format(func_name,line_num, file_name))
              oufile.write(file_content)
            except:
              print("EXCEPT: \n{}".format(file_content))
            break
          counter=counter+1

        oufile.close()
      if gotten > 40:
        break

    

if __name__ == '__main__':
  random.seed(15829)
  a = rand_rd()
  fltr = ["self","open","mock"]
  fl=input("File:")
  a.start(fl, fltr)
  print("Reader closed.")
