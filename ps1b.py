#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:11:09 2018

@author: shuayb
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 08:28:50 2018

@author: shuayb
"""

#User Inputs
annual_salary = float(input('Enter your starting annual salary:​ ')) #Your salary for the whole year
portion_saved_perc = float(input('Enter the percent of your salary to save, as a decimal: ​')) #this is the percentage of what you wishes to save monthly
total_cost = float(input('Enter the cost of your dream home: ​'))    #total cost of the dream home
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

#Variables. All amounts in (#)
current_savings = 0  #the amount that you have saved so far,starting from 0
portion_down_payment = 0.25 * total_cost
current_savings = 0  #the amount that you have saved so far,starting from 0
r = 0.04 #annual rate
annual_return = (current_savings * r) / 12
monthly_salary = annual_salary / 12
portion_saved = portion_saved_perc * monthly_salary 
time = 0

#Iterations and Output
while (current_savings <= portion_down_payment):
    current_savings += (current_savings * r / 12) + portion_saved 
    time += 1
    if time % 6 == 0: 
        monthly_salary = (semi_annual_raise * monthly_salary) + monthly_salary 
        portion_saved = monthly_salary * portion_saved_perc
print('Number of months: %d'%time)





