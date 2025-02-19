adminuser = "Admin"
adminpass = "Admin123"
finance_data = {}

def calc_salary():
    # Initialize finance_data as a global variable
    global finance_data 
    # Asking for salary and moth
    salary = float(input("Enter your salary: "))
    month = input("Enter the name of the month: ").lower()

    # Asking for percentages of salary allocated to savings rent and electricity
    savings_per = float(input("Enter the percentage of savings: "))
    rent_per = float(input("Enter the percentage of rent: "))
    electricity_per = float(input("Enter the Percentage of electricity: "))

    # Calculating the amount for savings, rent, electricity and storing them in a dictionary
    finance_data[month] = {
        "salary": salary,
        "month": month.lower(),
        "savings": (savings_per / 100) * salary,
        "rent": (rent_per / 100) * salary,
        "electricity": (electricity_per / 100) * salary
    }
    
    # Calculating the total expenses and reminder and storing them in the dictionary
    finance_data[month]["total_expenses"] = (
        finance_data[month]["savings"] + finance_data[month]["rent"] + finance_data[month]["electricity"]
    )
    finance_data[month]["reminder"] = finance_data[month]["salary"] - finance_data[month]["total_expenses"]

    # Estimate yearly rent and electricity costs
    finance_data[month]["yearly_rent"] = finance_data[month]["rent"] * 12
    finance_data[month]["yearly_electricity"] = finance_data[month]["electricity"] * 12
    
    # Calculating salary raised by 2 
    finance_data[month]["salary_squar"] = finance_data[month]["salary"] ** 2

    # Assume Nabiha saves an additional random amount each month
    additional_savings = float(input("Enter any additional savings amount: "))
    finance_data[month]["additional_savings"] = additional_savings
    if finance_data[month]["savings"] != 0:
        finance_data[month]["saving_div"] = additional_savings / finance_data[month]["savings"]
    else:  
        0

    # Printing the results in a readable format
    print(f"""
        [+] Financial information for {finance_data[month]["month"]}
            [*] Salary: ${finance_data[month]["salary"]}
            [*] Amount of Savings: ${finance_data[month]["savings"]}
            [*] Amount of Rents: ${finance_data[month]["rent"]}
            [*] Amount of Electricity: ${finance_data[month]["electricity"]}
            [*] Total Expenses of savings + rent + electricity: ${finance_data[month]["total_expenses"]}
            [*] Remaining amount after expenses: ${finance_data[month]["reminder"]}
            [*] Estimated yearly rent: ${finance_data[month]["yearly_rent"]}
            [*] Estimated yearly electricity: ${finance_data[month]["yearly_electricity"]}
            [*] Salary raised to power of 2: ${finance_data[month]["salary_squar"]}
            [*] Additional savings amount {finance_data[month]['additional_savings']} divided by savings: {finance_data[month]['saving_div']}
        """)


def admin_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == adminuser and password == adminpass:
        print("Welcome Back!")
        while True:
            calc = input("Do you want to calculate salary? (y/n): ")
            if calc == "y":
                calc_salary()
            elif calc == "n":
                admin_login()
            else:
                print("Invalid input!")
                continue
        else:
            print("Access Denied!")
            
admin_login()