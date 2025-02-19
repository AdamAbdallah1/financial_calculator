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
        "month": month.lower(),
        "savings": (savings_per / 100) * salary,
        "rent": (rent_per / 100) * salary,
        "electricity": (electricity_per / 100) * salary
    }
    
    # Calculating the total expenses and reminder and storing them in the dictionary
    finance_data["total_expenses"] = finance_data["savings"] + finance_data["rent"] + finance_data["electricity"]
    finance_data["reminder"] = finance_data["salary"] - finance_data["total_expenses"]

    # Estimate yearly rent and electricity costs
    finance_data["yearly_rent"] = finance_data["rent"] * 12
    finance_data["yearly_electricity"] = finance_data["electricity"] * 12
    
    # Calculating salary raised by 2 
    finance_data["salary_squar"] = finance_data["salary"] ** 2

    # Assume Nabiha saves an additional random amount each month
    additional_savings = float(input("Enter any additional savings amount: "))
    finance_data["additional_savings"] = additional_savings
    if finance_data["savings"] != 0:
        finance_data["saving_div"] = additional_savings / finance_data["savings"]
    else:  
        0

    # Printing the results in a readable format
    print(f"""
        [+] Financial information for {finance_data["month"]}
            [*] Salary: ${finance_data["salary"]}
            [*] Amount of Savings: ${finance_data["savings"]}
            [*] Amount of Rents: ${finance_data["rent"]}
            [*] Amount of Electricity: ${finance_data["electricity"]}
            [*] Total Expenses of savings + rent + electricity: ${finance_data["total_expenses"]}
            [*] Remaining amount after expenses: ${finance_data["reminder"]}
            [*] Estimated yearly rent: ${finance_data["yearly_rent"]}
            [*] Estimated yearly electricity: ${finance_data["yearly_electricity"]}
            [*] Salary raised to power of 2: ${finance_data["salary_squar"]}
            [*] Additional savings amount {finance_data['additional_savings']} divided by savings: {finance_data['saving_div']}
        """)

username = input("Enter your username: ")
password = input("Enter your password: ")
calc = False

if username == adminuser and password == adminpass:
    print("Welcome Back!")
    while True:
        calc = input("Do you want to calculate salary? (y/n): ")
        if calc == "y":
            calc_salary()
        elif calc == "n":
            break
        else:
            print("Invalid input!")
            continue
else:
    print("Access Denied!")