f=open('running-config.cfg','r')
x=[]
for line in f:
    if "access" in line:
        line=line.strip()
        x.append(tuple(line.split("object")))
print(x)
d={}
for item in x:
    i=0
    while i<len(item):

            d[item[0]]=item[1]
    i+=1
