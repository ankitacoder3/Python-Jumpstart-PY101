'''
Problem Statement:
Given two timestamps of the same day: a number of hours, minutes and seconds for both of the timestamps.
The moment of the first timestamp happened before the moment of the second one. Calculate how many seconds passed between them.
'''
print('\nCalculate Seconds_between_timestamps.py\n')

#Getting input for the number of hours, minutes and seconds for timestamp 1, and timestamp 2.
timestamp1_hr= int(input("Enter no. of hours for timestamp_1: "))
timestamp1_min= int(input("Enter no. of minutes for timestamp_1: "))
timestamp1_sec= int(input("Enter no. of seconds for timestamp_1: "))
timestamp2_hr= int(input("Enter no. of hours for timestamp_2: "))
timestamp2_min= int(input("Enter no. of minutes for timestamp_2: "))
timestamp2_sec= int(input("Enter no. of seconds for timestamp_2: "))

#Converting all hours, minutes, seconds to seconds for both the timestamps.
timestamp1_total_sec = ( timestamp1_hr * 3600 ) +( timestamp1_min * 60) + timestamp1_sec
timestamp2_total_sec = ( timestamp2_hr * 3600 ) +( timestamp2_min * 60) + timestamp2_sec

#Calculate the difference
difference = timestamp1_total_sec - timestamp2_total_sec

if(difference<0):
    difference=difference*-1

#output
print( "\nThe number of seconds that passed between the two timestamps is {} seconds.".format (difference))
print()