import streamlit as st
    interest_rate,
    project_years
)

present_value = calculate_present_value(
    future_value,
    interest_rate,
    project_years
)

depreciation_values = calculate_depreciation(
    initial_investment,
    depreciation_rate,
    project_years
)

decision = investment_decision(
    monthly_profit,
    npv,
    payback_period
)

# Project Details
st.subheader(f"Project: {project_name}")
st.write(f"Category: {project_category}")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Monthly Profit", f"₹ {monthly_profit:,.0f}")
col2.metric("Break-even Units", f"{break_even_units:.0f}")
col3.metric("NPV", f"₹ {npv:,.0f}")

col4, col5, col6 = st.columns(3)
col4.metric("Payback Period", f"{payback_period:.2f} years")
col5.metric("Future Value", f"₹ {future_value:,.0f}")
col6.metric("Present Value", f"₹ {present_value:,.0f}")

# Decision Section
st.subheader("Investment Decision")

if decision == "Good Investment":
    st.success(decision)
elif decision == "Moderate Risk":
    st.warning(decision)
else:
    st.error(decision)

# Charts
st.subheader("Charts")
plot_profit_chart(monthly_profit, project_years)
plot_depreciation_chart(depreciation_values)
plot_cost_pie_chart(fixed_cost, variable_cost * units_sold)
