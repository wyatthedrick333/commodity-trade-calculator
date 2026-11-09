# Commodity Trade Calculator 🌾

A beginner-friendly Streamlit finance app for estimating profit or loss from buying and selling grain (soybeans, corn, wheat, or other grain).

## Problem it solves
A grain merchandiser needs to know whether the difference between a purchase price and a selling price will cover freight and other costs.

## Features
- Enter purchase and selling prices per bushel, bushel quantity, freight, and other costs.
- See trade profit/loss, profit per bushel, return on cost, and break-even selling price.
- Review an itemized trade breakdown and a selling-price sensitivity chart.
- View formulas directly inside the app.
- No external market data, logins, or API keys required.

## Calculation formulas
- Revenue = selling price × bushels
- Total cost = purchase price × bushels + freight per bushel × bushels + other costs
- Profit = revenue − total cost
- ROI on total cost = profit / total cost × 100, if total cost > 0
- Break-even selling price = total cost / bushels

## Example to verify by hand
Buy 10,000 bushels for $10.00/bu and sell for $10.50/bu; freight is $0.20/bu and other costs total $500.
- Revenue: $105,000
- Total cost: $102,500
- Profit: $2,500
- Profit per bushel: $0.25
- Return on total cost: 2.44%
- Break-even selling price: $10.25/bu

## Run locally (optional)
Install packages from `requirements.txt`, then run:

```bash
streamlit run app.py
```

## Deploy using the GitHub website
1. Create a public repository named `commodity-trade-calculator` at https://github.com/new. Choose **Add a README file** if you want, then upload/replace it with the supplied README.
2. Upload `app.py`, `requirements.txt`, and `README.md` to the top level of that repository.
3. Visit https://share.streamlit.io and sign in using GitHub.
4. Choose **New app** > your repository > branch `main` > main file path `app.py` > **Deploy**.
5. Test the live app and submit its `https://...streamlit.app` address on Canvas.

## Testing
The included `test_calculations.py` contains independent checks for a profitable trade, loss, a zero-cost case, and zero quantity. Run `python -m unittest test_calculations.py`. You do not need to upload the test file for deployment, but keeping it in GitHub helps document verification.

## Limitations
This is an educational scenario calculator, not trading advice. It does not model storage, shrink, interest, basis contracts, futures hedges, or real-time prices unless included manually in other costs.

## AI assistance
The original project was built with ChatGPT's assistance. All numerical outputs should be checked against the sample calculations before submission.
