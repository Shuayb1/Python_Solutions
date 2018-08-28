
#Part C: Finding the right amount to save away

#Users Input
annual_salary = float(input("Enter your annual salary:"))
#Starting salary
original_salary = annual_salary
#Total cost of the house
total_cost = 1000000
#Semi(every six months) annual raise
semi_annual_raise = 0.07
#Portion saved for payment of the house
portion_down_payment = 0.25
#Starting savings
current_savings = 0
#Interest rate
interest_rate = 0.04
#Steps in bisection search
steps = 0
#The three years required to save for the house
required_months = 0

#Guess
high = 10000
low = 0
guess = (high+low) / 2.0

#Savings within this range
difference = 101



while difference > 100:
  annual_salary = original_salary
  monthly_salary = annual_salary / 12
  current_savings = 0
  required_months = 0

  while required_months < 36:
    if required_months % 6 == 0 and required_months != 0:
      annual_salary = annual_salary + (annual_salary * semi_annual_raise)
      monthly_salary = annual_salary / 12

    current_savings = current_savings + current_savings * interest_rate / 12
    current_savings = current_savings + (monthly_salary * (guess / 100))
    required_months = required_months + 1


  difference = abs(current_savings - (total_cost * portion_down_payment))

  if current_savings > total_cost * portion_down_payment:
    high = guess
  else:
    low = guess

  guess = (high+low) / 2.0
  steps = steps + 1

if guess <= 100:

  print ("Best savings rate: ", guess / 100  )
  print ("Steps in bisection search:", steps )
else:
    print ("It is not possible to pay the down payment in three years " )