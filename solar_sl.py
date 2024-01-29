import streamlit as st
import random
import numpy as np
import plotly.express as px

st.title('SnapSolar Broker Company Simulator')

# Sidebar for inputs
with st.sidebar:
    st.header("Input Parameters")
    total_mailers = st.number_input("Total number of mailers sent", min_value=0, value=100000, step=1000)
    callback_percentage = st.number_input("Callback percentage (as a decimal)", min_value=0.0, max_value=1.0, value=0.015,format="%.3f")
    close_percentage = st.number_input("Close percentage (as a decimal)", min_value=0.0, max_value=1.0, value=0.3)
    cost_per_mailer = st.number_input("Cost per mailer", min_value=0.0, value=0.5)
    average_deal_value = 5000  # You can make this an input if you want
    days = 365  # You can also make this an input
    execution_time = 60  # Same as above
    execution_capacity = 3  # And this one
    sales_percentage = st.number_input("Revenue split percentage for sales team (as a decimal)", min_value=0.0, max_value=1.0, value=0.6)
    execution_percentage = st.number_input("Revenue split percentage for execution team (as a decimal)", min_value=0.0, max_value=1.0, value=0.3)
    company_percentage = st.number_input("Revenue split percentage for company (as a decimal)", min_value=0.0, max_value=1.0, value=0.1)
    business_overhead = st.number_input("Business overhead costs", min_value=0.0, value=50000.0)
    execution_misc_costs = st.number_input("Miscellaneous costs for execution team", min_value=0.0, value=12000.0)

# Button to run simulation
if st.button('Run Simulation'):
    # Simulation code
    total_callbacks = total_mailers * callback_percentage
    leads_per_day = total_callbacks / days
    total_mailer_cost = total_mailers * cost_per_mailer

    total_revenue = 0
    execution_schedule = np.zeros(execution_time)

    for day in range(days):
        for _ in range(int(leads_per_day)):
            if random.random() < close_percentage:
                deal_value = average_deal_value
                total_revenue += deal_value

        execution_schedule = np.roll(execution_schedule, -1)
        execution_schedule[-1] = 0

    net_revenue = total_revenue - total_mailer_cost - execution_misc_costs - business_overhead
    sales_revenue = net_revenue * sales_percentage
    execution_revenue = net_revenue * execution_percentage
    company_revenue = net_revenue * company_percentage

    sales_team = ['Angelo', 'Tom', 'Tom', 'Jerry', 'Allan']
    execution_team = ['James', 'Aaron']
    sales_revenue_per_person = sales_revenue / len(sales_team)
    execution_revenue_per_person = execution_revenue / len(execution_team)

    # Output
    st.subheader("Simulation Results")
    st.write(f"Total Revenue: ${total_revenue}")
    st.write(f"Net Revenue (after SALES, EXECUTION, and COMPANY OVERHEAD costs): ${net_revenue}")
    st.write("Revenue Per Person:")
    for person in sales_team:
        st.write(f"{person} (Sales): ${sales_revenue_per_person:.2f}")
    for person in execution_team:
        st.write(f"{person} (Execution): ${execution_revenue_per_person:.2f}")
    st.write(f"Company Revenue: ${company_revenue:.2f}")

        # Revenue Distribution Pie Chart
    labels = ['Sales Team', 'Execution Team', 'Company']
    values = [sales_revenue, execution_revenue, company_revenue]
    fig = px.pie(names=labels, values=values, title='Revenue Distribution')
    st.plotly_chart(fig)

    # Optional: Revenue Over Time Line Graph
    # This requires storing daily revenue data during the simulation
    # dates = pd.date_range(start="2021-01-01", periods=days)
    # daily_revenues = [...]  # You should populate this list during the simulation
    # time_series_fig = px.line(x=dates, y=daily_revenues, title='Revenue Over Time')
    # st.plotly_chart(time_series_fig)


# Run this app with `streamlit run your_script_name.py`
