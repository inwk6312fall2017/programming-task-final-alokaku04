from weather import Weather

weather = Weather()
location = weather.lookup_by_location(input("Enter the Location "))
condition = location.condition()
print(condition['text'])
for forecasts in location.forecast():
    print(forecasts['date'])

    print("The Highest temprature in 5 days is ", forecasts['high'])
