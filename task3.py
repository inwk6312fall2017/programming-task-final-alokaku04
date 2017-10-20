
f=open('running-config.cfg','r')
new=open('new_file.cfg','a')

for line in f:
    y=line.replace("172","192")
    new.write(y)
    print(y)