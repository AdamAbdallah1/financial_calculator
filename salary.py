adminuser = "Admin"
adminpass = "Admin123"
finance_data = {}

def calc_salary():
    global finance_data  
    salary = float(input("Enter your salary: "))
    month = input("Enter the name of the month: ").lower()

    savings_per = float(input("Enter the percentage of savings: "))
    rent_per = float(input("Enter the percentage of rent: "))
    electricity_per = float(input("Enter the Percentage of electricity: "))

    finance_data[month] = {
        "salary": salary,
        "savings": (savings_per / 100) * salary,
        "rent": (rent_per / 100) * salary,
        "electricity": (electricity_per / 100) * salary
    }

    finance_data[month]["total_expenses"] = (
        finance_data[month]["savings"] + finance_data[month]["rent"] + finance_data[month]["electricity"]
    )
    finance_data[month]["reminder"] = finance_data[month]["salary"] - finance_data[month]["total_expenses"]
    finance_data[month]["yearly_rent"] = finance_data[month]["rent"] * 12
    finance_data[month]["yearly_electricity"] = finance_data[month]["electricity"] * 12
    finance_data[month]["salary_squar"] = finance_data[month]["salary"] ** 2

    additional_savings = float(input("Enter any additional savings amount: "))
    finance_data[month]["additional_savings"] = additional_savings
    if finance_data[month]["savings"] != 0:
        finance_data[month]["saving_div"] = additional_savings / finance_data[month]["savings"]
    else:  
        finance_data[month]["saving_div"] = 0  # Properly set to 0

    print_finance_data(month)  # Call a function to display the data


def print_finance_data(month):
    """Prints financial data for a given month."""
    print(f"""
    [+] Financial Information for {month.capitalize()}
        [*] Salary: ${finance_data[month]["salary"]}
        [*] Amount of Savings: ${finance_data[month]["savings"]}
        [*] Amount of Rent: ${finance_data[month]["rent"]}
        [*] Amount of Electricity: ${finance_data[month]["electricity"]}
        [*] Total Expenses (savings + rent + electricity): ${finance_data[month]["total_expenses"]}
        [*] Remaining Balance: ${finance_data[month]["reminder"]}
        [*] Estimated Yearly Rent: ${finance_data[month]["yearly_rent"]}
        [*] Estimated Yearly Electricity: ${finance_data[month]["yearly_electricity"]}
        [*] Salary Squared: ${finance_data[month]["salary_squar"]}
        [*] Additional Savings: ${finance_data[month]["additional_savings"]}
        [*] Additional Savings ÷ Savings: {finance_data[month]["saving_div"]}
    """)


def view_s():
    """Displays stored salary data for all months."""
    if not finance_data:
        print("No salary data available.")
        return

    for month in finance_data:
        print_finance_data(month)


def admin_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == adminuser and password == adminpass:
        print("Welcome Back!")
        while True:
            print("""
                  Do you want to:
                    (C)alculate salary
                    (V)iew salaries
                    (E)xit
                  """)
            action = input(">_: ").lower()
            
            if action == "c":
                calc_salary()
            elif action == "v":
                view_s()
            elif action == "e":
                print("Goodbye!")
                break
            else:
                print("Invalid input! Try again.")
    else:
        print("Access Denied!")
        

admin_login()
