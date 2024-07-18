'''
Problem Statement:
Write a Python program to calculate wind chill index.
'''
print('\nCalculate Wind_chill_index.py\n')

#getting input for temperatue, and wind speed.
wind= float(input("Wind speed (at 10 meter height, in km/hr): "))
air_temperature= float(input("Speed of Air temperature (in degrees Celsius): "))

#calculate
index=  13.12 +(0.6215*air_temperature)-(11.37*(wind**(0.16)))+(0.3965*air_temperature*(wind**(0.16)))

#output
print(f"\n The wind chill index is {round(index,3)}." )
print()