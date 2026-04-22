import streamlit as st
import matplotlib.pyplot as plt


def plot_profit_chart(monthly_profit, years):
    yearly_profit = [monthly_profit * 12 * year for year in range(1, years + 1)]
    years_list = list(range(1, years + 1))

    fig, ax = plt.subplots()
    ax.plot(years_list, yearly_profit, marker='o')
    ax.set_title("Profit Growth Over Years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Profit (₹)")

    st.pyplot(fig)


def plot_depreciation_chart(depreciation_values):
    years = list(range(1, len(depreciation_values) + 1))

    fig, ax = plt.subplots()
    ax.bar(years, depreciation_values)
    ax.set_title("Depreciation Over Years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Asset Value (₹)")

    st.pyplot(fig)


def plot_cost_pie_chart(fixed_cost, variable_cost_total):
    labels = ['Fixed Cost', 'Variable Cost']
    values = [fixed_cost, variable_cost_total]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title("Cost Distribution")

    st.pyplot(fig)
