f=open('running-config.cfg','r')
for line in f:
    if "access" in line:
        print (line)