f=open('running-config.cfg','r')

for line in f:
    if "access" in line:
        line=line.strip()


        x=(tuple(line.split("object")))
d={}
i=0
while i<len(x):
    if "access" in x[i]:
        d[x[i]]=x[i+1]
        print(d)
    i+=1
