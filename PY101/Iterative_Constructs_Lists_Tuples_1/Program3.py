'''
Problem Statement:
Generate heart rate randomly between 50 to 120 at time interval of 3 hours for 24 hours.
(i) If heart rate is between 50-65 print as bradycardia(lower heart rate) if greater than 100 print as tachycardia(higher heart rate). Else print as normal.
(ii) Count number of Bradycardia and tachycardia if any of this is greater than 3 display as risk.
(iii) Print the maximum heart rate and minimum heart rate
'''
print('\nCalculate Heart_rate.py\n')

#getting the random heartbeat
import random
heart_bt = [ random.randrange (50,120) for i in range(1, 24, 3) ]
print(f"The heartbeats are as follows: {heart_bt} ")

#Processing
print("\nProcessing heartbeats...")

#for bradycardia and tachycardia the count variables are, respectively.
b_count = 0
t_count = 0

#define max and min
max = 200
min = 0

#using the for loop, and if conditions.
for x in heart_bt:

    #bradycardia
    if x in range(50, 66):
        print(f"\tBradycardia occurs at {x}")
        b_count +=1
        
    #tachycardia
    elif x >100:
        print(f"\tTachycardia occurs at {x}")
        t_count +=1

    #normal
    else :
        print(f"\tThe heartbeat is normal at {x}")
        t_count +=1

    # getting min and max values
    if x< max:
        max = x
    if x> min:
        min= x

#final result or state
if b_count>3 or t_count>3 :
    print("\tHeart is at RISK!")

print(f"\nThe  maximum heart rate is {max}, and the minimum heart rate is {min}.")
print()