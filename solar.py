import random
import numpy as np

# Inputs
total_mailers = int(input("Enter total number of mailers sent: "))
callback_percentage = float(input("Enter callback percentage (as a decimal): "))
close_percentage = float(input("Enter close percentage (as a decimal): "))
cost_per_mailer = float(input("Enter cost per mailer: "))
average_deal_value = 5000  # Average revenue from a closed deal
days = 365  # Simulation period (1 year)
execution_time = 60  # Days to complete an installation
execution_capacity = 3  # Number of teams available for execution
sales_percentage = float(input("Enter revenue split percentage for sales team (as a decimal): "))
execution_percentage = float(input("Enter revenue split percentage for execution team (as a decimal): "))
company_percentage = float(input("Enter revenue split percentage for company (as a decimal): "))
business_overhead = float(input("Enter business overhead costs: "))
execution_misc_costs = float(input("Enter miscellaneous costs for execution team: "))

# Calculating leads per day and total cost of mailers
total_callbacks = total_mailers * callback_percentage
leads_per_day = total_callbacks / days
total_mailer_cost = total_mailers * cost_per_mailer

# Simulation
total_revenue = 0
execution_schedule = np.zeros(execution_time)  # Schedule for execution teams

for day in range(days):
    # Sales arm operation
    for _ in range(int(leads_per_day)):
        if random.random() < close_percentage:
            deal_value = average_deal_value
            total_revenue += deal_value

    # Update execution schedule
    execution_schedule = np.roll(execution_schedule, -1)
    execution_schedule[-1] = 0

# Net Revenue Calculation
net_revenue = total_revenue - total_mailer_cost - execution_misc_costs - business_overhead

# Revenue Allocation
sales_revenue = net_revenue * sales_percentage
execution_revenue = net_revenue * execution_percentage
company_revenue = net_revenue * company_percentage

# Add mailer costs back to sales revenue before division
adjusted_sales_revenue = sales_revenue

# Individual Revenue Distribution
sales_team = ['Angelo', 'Tom', 'Tom', 'Jerry', 'Allan']
execution_team = ['James', 'Aaron']

sales_revenue_per_person = adjusted_sales_revenue / len(sales_team)
execution_revenue_per_person = execution_revenue / len(execution_team)

# Output
print(f"Total Revenue: ${total_revenue}")
print(f"Net Revenue (after SALES, EXECUTION, and COMPANY OVERHEAD costs): ${net_revenue}")
print("Revenue Per Person:")
for person in sales_team:
    print(f"{person} (Sales): ${sales_revenue_per_person:.2f}")
for person in execution_team:
    print(f"{person} (Execution): ${execution_revenue_per_person:.2f}")
print(f"Company Revenue: ${company_revenue:.2f}")
