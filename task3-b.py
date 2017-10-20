f=open('running-config.cfg','r')
for line in f:
    if "access" in line:
        line=line.strip()
        x=tuple(line.split("object"))
        print(x)
