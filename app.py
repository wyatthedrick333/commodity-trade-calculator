"""Commodity Trade Calculator - a beginner-friendly finance Streamlit app."""

import pandas as pd
import streamlit as st


# Calculation logic is kept separate so it can be checked and tested easily.
def calculate_trade(buy_price, sell_price, bushels, freight_per_bushel, other_costs):
    """Return revenue, costs, profit, return on costs and break-even selling price."""
    purchase_cost = buy_price * bushels
    freight_cost = freight_per_bushel * bushels
    total_cost = purchase_cost + freight_cost + other_costs
    revenue = sell_price * bushels
    profit = revenue - total_cost
    roi = profit / total_cost * 100 if total_cost > 0 else 0.0
    breakeven = total_cost / bushels if bushels > 0 else 0.0
    return {
        "purchase_cost": purchase_cost,
        "freight_cost": freight_cost,
        "total_cost": total_cost,
        "revenue": revenue,
        "profit": profit,
        "roi": roi,
        "breakeven": breakeven,
        "profit_per_bushel": profit / bushels if bushels > 0 else 0.0,
    }


st.set_page_config(page_title="Commodity Trade Calculator", page_icon="🌾", layout="centered")
st.title("🌾 Commodity Trade Calculator")
st.write(
    "Estimate the potential profit on a grain trade. Enter a purchase price, "
    "sale price, quantity, and costs to see whether the trade makes money."
)
st.caption("For educational use. Prices are assumptions, not live market quotes.")

commodity = st.selectbox("Commodity", ["Soybeans", "Corn", "Wheat", "Other grain"])

left, right = st.columns(2)
with left:
    buy_price = st.number_input("Purchase price ($/bushel)", min_value=0.0, value=10.00, step=0.05, format="%.2f")
    bushels = st.number_input("Quantity (bushels)", min_value=1, value=10000, step=1000)
    other_costs = st.number_input("Other total costs ($)", min_value=0.0, value=500.0, step=50.0)
with right:
    sell_price = st.number_input("Selling price ($/bushel)", min_value=0.0, value=10.50, step=0.05, format="%.2f")
    freight = st.number_input("Freight ($/bushel)", min_value=0.0, value=0.20, step=0.05, format="%.2f")

# Calculate using the numbers provided by the user.
result = calculate_trade(buy_price, sell_price, bushels, freight, other_costs)

st.subheader(f"Results: {commodity}")
a, b = st.columns(2)
a.metric("Estimated profit / loss", f"${result['profit']:,.2f}")
b.metric("Return on total cost", f"{result['roi']:,.2f}%")
c, d = st.columns(2)
c.metric("Profit per bushel", f"${result['profit_per_bushel']:,.2f}")
d.metric("Break-even selling price", f"${result['breakeven']:,.2f}/bu")

if result["profit"] > 0:
    st.success("At these prices and costs, the trade is profitable.")
elif result["profit"] < 0:
    st.warning("At these prices and costs, the trade loses money.")
else:
    st.info("At these prices and costs, the trade breaks even.")

st.subheader("Trade breakdown")
breakdown = pd.DataFrame(
    {
        "Item": ["Sales revenue", "Grain purchase", "Freight", "Other costs", "Net profit / loss"],
        "Amount ($)": [result["revenue"], -result["purchase_cost"], -result["freight_cost"], -other_costs, result["profit"]],
    }
)
st.dataframe(
    breakdown.style.format({"Amount ($)": "${:,.2f}"}),
    hide_index=True,
    use_container_width=True,
)

st.subheader("What if the selling price changes?")
st.write("This chart shows the estimated profit or loss at different selling prices, holding the other inputs fixed.")
# Test sale prices around the selected sale price, from $1.00 lower to $1.00 higher.
scenario_prices = [round(max(0.0, sell_price - 1.0) + i * 0.10, 2) for i in range(21)]
scenarios = pd.DataFrame(
    {
        "Selling price ($/bu)": scenario_prices,
        "Profit ($)": [price * bushels - result["total_cost"] for price in scenario_prices],
    }
)
st.line_chart(scenarios.set_index("Selling price ($/bu)"), y="Profit ($)")

with st.expander("How are the numbers calculated?"):
    st.write("**Revenue** = selling price × bushels")
    st.write("**Total cost** = (purchase price × bushels) + (freight × bushels) + other costs")
    st.write("**Profit** = revenue − total cost")
    st.write("**Return on cost** = profit ÷ total cost × 100 (if total cost is greater than zero)")
    st.write("**Break-even selling price** = total cost ÷ bushels")
    st.write("The model assumes the full quantity is purchased and sold, with no shrink, financing costs, or price hedges.")

st.caption("Built with AI-assisted coding using Python and Streamlit.")
