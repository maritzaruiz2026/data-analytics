import random
import math
import statistics

vals_1_100 = range(1,100) 
vals_sample = random.sample(vals_1_100, 75) 
vals_choices = random.choices(vals_1_100, k = 200) 
radius = random.randint(3,10) 
pi = math.pi

###First module
print(f'_Experimenting with a subset of integers 1-100:')
sum_vals_1_100 = sum(vals_sample)
print(f'Sum of 75 sample values from 1 to 100: {sum_vals_1_100:.2f}')
avg_sample_val = statistics.mean(vals_sample)
print(f'Average of 75 sample values: {avg_sample_val:.2f}')
med_sample_val = statistics.median(vals_sample)
print(f'Median of 75 sample values: {med_sample_val:.2f}')
print('\n') 
##I used vals_sample for all of my variables since it asked to aum, avg and find the median of 75 sample values
##vals_sample randomizes val_1_100 annd limits it to 75 outputs
##Whatever I renamed a variable to I ensured I entered into the f-string and also rounded it to the nearest tenth decimal (some answers were extremely long)

###Second module
print(f'_Experimenting with a superset of 200 values, integers 1-100:')
avg_vals_choices = statistics.mean(vals_choices)
print(f'Average of 200 values: {avg_vals_choices:.2f}')
med_vals_choices = statistics.median(vals_choices)
print(f'Median of 75 sample values: {med_vals_choices:.2f}')
mode_vals_choices = statistics.mode(vals_choices)
print(f'Median of 75 sample values: {mode_vals_choices:.2f}')
dev_vals_choices = statistics.stdev(vals_choices)
print(f'Standard deviation of 200 values: {dev_vals_choices:.2f}')
print('\n')
##Similar to the first module, I used vals_choices here because it allowed 200 random outputs from 1-100
##Copied and pasted new variable name within the statistics function needed to calculate the answer

###Third module
circle_area = pi * (radius ** 2)
print(f'_Modeling a random circle:')
print(f'Radius = {radius}, area = {math.ceil(circle_area)} (rounded up to the nearest integer)')
print(f'Radius = {radius}, area = {math.floor(circle_area)} (rounded down to the nearest integer)')
##For this one I created a variable that calculated the area of a circle with the variable radius already given to us
##I used the math functions ceil and floor to either round up or down an integer