import csv
indx=0
ec=0
incs=5
oufile=open("new.csv","w")
relatedness=0
allcount=0
with open("organization_freq.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
    for i in csvreader:
        print ("[{:.2f}%]-- Reading . . . ".format((indx/32700)*100), end='\r', flush=True)
        rlt=1
        accum=0
        for cter in range(incs):
            accum+=int(i[cter+1])
        if((accum)!=0):
            zeros=0
            for cter in range(incs):
                if(int(i[cter+1])==0):
                    zeros=zeros+1
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
print("\nRelatedness: {:.4f}".format(relatedness/allcount), flush=True)

print("Total: {}".format(allcount))
oufile.close()