print(" *** Wind classification ***")
wind = input("Enter wind speed (km/h) : ")

if float(wind) <= 51.99 : print("Wind classification is Breeze.")
elif float(wind) <= 55.99 : print("Wind classification is Depression.")
elif float(wind) <= 101.99 : print("Wind classification is Tropical Storm.")
elif float(wind) <= 208.99 : print("Wind classification is Typhoon.")
else : print("Wind classification is Super Typhoon.") 
