# Asking for salary and moth
salary = float(input("Enter your salary: "))
month = input("Enter the name of the month: ")

# Asking for percentages of salary allocated to savings rent and electricity
savings_per = float(input("Enter the percentage of savings: "))
rent_per = float(input("Enter the percentage of rent: "))
electricity_per = float(input("Enter the Percentage of electricity: "))

# Calculating the amount for savings, rent, electricity
savings = (savings_per / 100) * salary
rent = (rent_per / 100) * salary
electricity = (electricity_per / 100) * salary

# Calculating the total expenses and reminder
total_exp = savings + rent + electricity
reminder = salary - total_exp

# Estimate yearly rent and electricity costs
yearly_rent = rent * 12
yearly_electricity = electricity * 12
