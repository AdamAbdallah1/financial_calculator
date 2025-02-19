adminuser = "Admin"
adminpass = "Admin123"

def calc_salary():
    # Asking for salary and moth
    salary = float(input("Enter your salary: "))
    month = input("Enter the name of the month: ")

    # Asking for percentages of salary allocated to savings rent and electricity
    savings_per = float(input("Enter the percentage of savings: "))
    rent_per = float(input("Enter the percentage of rent: "))
    electricity_per = float(input("Enter the Percentage of electricity: "))

    # Calculating the amount for savings, rent, electricity and storing them in a dictionary
    finance_data = {
        "salary": salary,
        "month": month,
        savings_per: (savings_per / 100) * salary,
        rent_per: (rent_per / 100) * salary,
        electricity_per: (electricity_per / 100) * salary
    }
    finance_data["total_expenses"] = finance_data["savings"] + finance_data["rent"] + finance_data["electricity"]


    # Calculating the total expenses and reminder
    total_exp = savings + rent + electricity
    reminder = salary - total_exp

    # Estimate yearly rent and electricity costs
    yearly_rent = rent * 12
    yearly_electricity = electricity * 12

    # Calculating salary raised by 2 
    salary_squar = salary ** 2

    # Assume Nabiha saves an additional random amount each month
    additional_savings = float(input("Enter any additional savings amount: "))
    if savings != 0:
        saving_div = additional_savings / savings
    else:  
        0

    # Printing the results in a readable format
    print(f"""
        [+] Financial information for {month}
            [*] Salary: ${salary}
            [*] Amount of Savings: ${savings}
            [*] Amount of Rents: ${rent}
            [*] Amount of Electricity: ${electricity}
            [*] Total Expenses of savings + rent + electricity: ${total_exp}
            [*] Remaining amount after expenses: ${reminder}
            [*] Estimated yearly rent: ${yearly_rent}
            [*] Estimated yearly electricity: ${yearly_electricity}
            [*] Salary raised to power of 2: ${salary_squar}
            [*] Additional savings amount {additional_savings} divided by savings: {saving_div}
        """)

username = input("Enter your username: ")
password = input("Enter your password: ")
if username == adminuser and password == adminpass:
    print("Welcome Back!")
    calc_salary()
else:
    print("Access Denied!")