import csv
indx=0
ec=0
oufile=open("new.csv","w")
oufile.write("{}, {}, {}, {}, {}, {}, {}\n".format("org",
            "Dyn","Func","Dec","With","Asc","Relatedness"))
relatedness=0
allcount=0
with open("organization_freq.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for i in csvreader:
        print ("[{:.2f}%]-- Reading . . . ".format(indx/32700), end='\r', flush=True)
        
        rlt=1
        if((int(i[1])+int(i[2])+int(i[3])+int(i[4]))!=0):
#             print(int(i[1])+int(i[2])+int(i[3])+int(i[4]))
            zeros=0
            for cter in range(4):
                # print(cter)
                if(int(i[cter+1])==0):
                    zeros=zeros+1
            # print(zeros)
            # break
            if zeros==3:
                rlt=0
        relatedness+=rlt
        allcount+=1      
        try:
          oufile.write("{}, {}, {}, {}, {}, {}, {}\n".format(i[0],i[1],i[2],i[3],i[4],i[5],rlt))
        except:
          print("EXCEPT{}".format(ec))
          ec+=1
        indx+=1
print("Relatedness: {}\n".format(relatedness/allcount))

print("Total: {}\n".format(allcount))
oufile.close()