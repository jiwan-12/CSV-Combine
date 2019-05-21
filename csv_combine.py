# combine csv file to single files #

import glob
count=0
fout=open("merged.csv","a")
print "combining all csv file to single..."
for files in glob.glob("*.csv"):    
    count=count+1
    if count==1:
        for line in open(files):
            fout.write(line)

    else:
        f = open(files)
        f.next() # skip the header
        for line in f:
            fout.write(line)
        f.close()
        
fout.close()
print"completed..."