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


print(max(t))

print(t)
print(l)