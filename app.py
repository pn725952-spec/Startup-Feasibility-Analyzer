import streamlit as st
    calculate_depreciation,
    investment_decision
)
from charts import plot_profit_chart, plot_depreciation_chart, plot_cost_pie_chart

st.set_page_config(page_title="Startup Feasibility Analyzer", layout="wide")

st.title("Startup Feasibility Analyzer")
st.markdown("Analyze whether your startup or engineering project is profitable.")

st.sidebar.header("Project Inputs")

project_name = st.sidebar.text_input("Project Name", "Smart Irrigation System")
project_category = st.sidebar.selectbox(
    "Project Category",
    ["IoT", "EV", "Manufacturing", "Software", "Agriculture", "Healthcare"]
)

initial_investment = st.sidebar.number_input("Initial Investment (₹)", min_value=0, value=500000)
fixed_cost = st.sidebar.number_input("Fixed Cost (₹)", min_value=0, value=100000)
variable_cost = st.sidebar.number_input("Variable Cost per Unit (₹)", min_value=0, value=500)
selling_price = st.sidebar.number_input("Selling Price per Unit (₹)", min_value=1, value=1000)
units_sold = st.sidebar.number_input("Expected Units Sold per Month", min_value=1, value=300)
interest_rate = st.sidebar.slider("Annual Interest Rate (%)", 1, 20, 10)
project_years = st.sidebar.slider("Project Duration (Years)", 1, 10, 5)
depreciation_rate = st.sidebar.slider("Depreciation Rate (%)", 1, 30, 10)

# Calculations
monthly_total_cost = calculate_total_cost(fixed_cost, variable_cost, units_sold)
monthly_revenue = calculate_revenue(selling_price, units_sold)
monthly_profit = calculate_profit(monthly_revenue, monthly_total_cost)
break_even_units = calculate_break_even(fixed_cost, selling_price, variable_cost)
payback_period = calculate_payback_period(initial_investment, monthly_profit)
npv = calculate_npv(initial_investment, monthly_profit, interest_rate, project_years)
future_value = calculate_future_value(initial_investment, interest_rate, project_years)
present_value = calculate_present_value(future_value, interest_rate, project_years)
depreciation_values = calculate_depreciation(initial_investment, depreciation_rate, project_years)
decision = investment_decision(monthly_profit, npv, payback_period)

st.subheader(f"Project: {project_name}")
st.write(f"Category: {project_category}")

col1, col2, col3 = st.columns(3)

col1.metric("Monthly Profit", f"₹ {monthly_profit:,.0f}")
col2.metric("Break-even Units", f"{break_even_units:.0f}")
col3.metric("NPV", f"₹ {npv:,.0f}")

col4, col5, col6 = st.columns(3)

col4.metric("Payback Period", f"{payback_period:.2f} years")
col5.metric("Future Value", f"₹ {future_value:,.0f}")
col6.metric("Present Value", f"₹ {present_value:,.0f}")

st.subheader("Investment Decision")

if decision == "Good Investment":
    st.success(decision)
elif decision == "Moderate Risk":
    st.warning(decision)
else:
    st.error(decision)

st.subheader("Charts")

plot_profit_chart(monthly_profit, project_years)
plot_depreciation_chart(depreciation_values)
plot_cost_pie_chart(fixed_cost, variable_cost * units_sold)
