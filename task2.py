from weather import Weather

weather = Weather()
location = weather.lookup_by_location("Halifax" )
condition = location.condition()
print(condition['text'])
t=[]
l=[]
for forecasts in location.forecast():
        t.append (int(forecasts['high']))
        l.append(int(forecasts['low']))

p=t[:5]
q=l[:5]
x=[]
print("max_temp=", max(p))
print("min_temp=" ,min(q))
for forecasts in location.forecast():

    x.append(forecasts['date'])
print("max temp day=",x[4] ,"             ","min temp day=", x[2],"            ", "its going to rain=",x[2])
