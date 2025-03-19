import os,sys

card=sys.argv[1]

combinecommand="combineCards.py "

regions=["WW","1b","2b","SS"]
eras=["2022","2022EE","2023","2023BPix"]

for i in regions:
  for j in eras:
    os.system("cp "+card+"Template.txt "+card+"_"+i+"_"+j+".txt")
    os.system("sed -i 's/$REGION/"+i+"/g' "+card+"_"+i+"_"+j+".txt")
    os.system("sed -i 's/$ERA/"+j+"/g' "+card+"_"+i+"_"+j+".txt")
    if(i!="WW"):
      os.system("sed -i 's/bdtResponse/mll/g' "+card+"_"+i+"_"+j+".txt")
    if("2023" in j):
      os.system("sed -i 's/2022/2023/g' "+card+"_"+i+"_"+j+".txt")
      os.system("sed -i 's/1.014/1.013/g' "+card+"_"+i+"_"+j+".txt")
    combinecommand=combinecommand+card+"_"+i+"_"+j+".txt "

combinecommand=combinecommand+"> "+card+"_combined.txt"

os.system(combinecommand)
