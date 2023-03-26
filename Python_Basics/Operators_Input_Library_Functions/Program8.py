'''
Problem Statement:
If person leave house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
what time do the person get home for breakfast?

'''

#Calculation for easy pace and tempo pace, both the speeds are in seconds.
Easy_pace=((8*60)+15 )
Tempo_pace=((7*60)+12)

#Calculate total number of seconds and convert it to minute.
Total_seconds =(2*Easy_pace)+(3*Tempo_pace)
Total_min =Total_seconds//60

#Convert initial time (when he left house) to minutes.
initial_time=(6*60)+52

#Add  
Total_time= Total_min + initial_time

#Convert it to hr-min format
hr= Total_time//60
min= Total_time% 60

#output
print("He left home at 6:52.")
print("After {} minutes,he will reach home.". format (Total_min))
print("The time he will reach home for breakfast is {}:{}.". format (hr, min))
