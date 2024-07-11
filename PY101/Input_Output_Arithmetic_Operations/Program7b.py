'''
Problem Statement:
Program to  Convert temperature in Fahrenheit to Celsius
'''
print('\nCalculate Fahrenheit_to_celsius.py\n')

#Getting input for temperature in ‘Fahrenheit’.
Fahrenheit= float(input("Enter temperature in Fahrenheit: "))

#Converting Fahrenheit to Celsius.
Celsius = ( Fahrenheit -32 ) * ( 5/9)

#output
print("\nThe temperature is {} Celsius.". format (Celsius))
print()