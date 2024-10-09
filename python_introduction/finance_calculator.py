# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask for the user's total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Define the annual interest rate
interest_rate = 0.05

# Calculate projected savings after one year with interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

# Output the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.") 