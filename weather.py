temperature = 75
forecast = "rainy"

raining = forecast == "rainy"
if raining:
    print("it's raining stay inside")

if (temperature < 80 and temperature > 60) and forecast != "rainy":
    print("go outside")
else:
    print("stay inside")