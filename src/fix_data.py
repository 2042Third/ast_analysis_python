import csv

# import time



def fix_rows( fname):
  indx=0
  ec=0
  oufile=open("fixed_"+fname,"w")
  with open(fname, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for i in spamreader:
        print ("[{:.2f}%]-- Reading . . . ".format(indx/7062170), end='\r', flush=True)
        # print(i[3])
        i=[s.strip() for s in i]
        a = i[3].replace(" ","/",1)
        a = a.replace("\"","")
        b = a.split('/')
        # print("\n[%s]\n"%i[7].replace("\"",""))
        try:
          oufile.write("\"{}\", \"{}\", \"{}\", \"{}\", {}, {}, {}, {}\n".format("bigq",
            b[0],b[1],a,i[4],i[5],i[6],i[7].replace("\"","")))
        except:
          print("EXCEPT{}".format(ec))
          ec+=1
        indx+=1
  oufile.close()

    

def main():
  fl=input("File:")
  fix_rows(fl)

if __name__ == '__main__':
  main()