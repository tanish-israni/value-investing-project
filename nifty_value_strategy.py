import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

def run_value_strategy(capital):
    # Step 1: Load stock fundamentals (now with current_price)
    df = pd.read_csv('nifty500_fundamental.csv')

    # Step 2: Define metrics and calculate percentiles
    metrics = ['p_e_ratio', 'p_b_ratio', 'p_s_ratio', 'ev_ebitda', 'ev_gp']
    for metric in metrics:
        df[metric + '_percentile'] = df[metric].rank(pct=True, ascending=True)

    # Step 3: Calculate RV Score
    percentile_cols = [m + '_percentile' for m in metrics]
    df['rv_score'] = df[percentile_cols].mean(axis=1)

    # Step 4: Select top 50 value stocks
    df_top = df.sort_values('rv_score').head(50).copy().reset_index(drop=True)

    # Step 5: Capital allocation setup
    df_top['shares_to_buy'] = 0
    capital_top = capital * 0.80
    capital_bottom = capital * 0.20

    # Step 6: Allocate to top 10 stocks (80%)
    remaining_top = capital_top
    for i in range(10):
        price = df_top.at[i, 'current_price']
        if pd.notna(price) and price > 0:
            shares = int(remaining_top // price)
            if shares > 0:
                df_top.at[i, 'shares_to_buy'] = shares
                remaining_top -= shares * price

    # Step 7: Allocate to bottom 40 stocks (20%)
    remaining_bottom = capital_bottom
    for i in range(10, 50):
        price = df_top.at[i, 'current_price']
        if pd.notna(price) and price > 0:
            shares = int(remaining_bottom // price)
            if shares > 0:
                df_top.at[i, 'shares_to_buy'] = shares
                remaining_bottom -= shares * price

    # Step 8: Optional low capital warning
    total_shares = df_top['shares_to_buy'].sum()
    if total_shares == 0:
        print("⚠️ Warning: Capital too low to purchase any stock. Consider increasing the amount.")

    # Step 9: Save to Excel (now includes current price and shares to buy)
    writer = pd.ExcelWriter('value_strategy_results.xlsx', engine='xlsxwriter')
    df_top.to_excel(writer, sheet_name='Top 50 Value Stocks', index=False)
    writer.close()

    # Step 10: Plot and save chart (using current price)
    fig, ax = plt.subplots()
    valid_prices = df_top['current_price'].dropna().values
    if valid_prices.size > 0:
        ax.plot(df_top['current_price'].dropna().values, label='Current Share Price')
        ax.set_title('Top 50 Value Stocks - Current Share Price')
        ax.set_xlabel('Stock Index')
        ax.set_ylabel('Share Price')
        ax.legend()
        plt.grid(True)
        plt.savefig('strategy_comparison.png')
        plt.close()
    else:
        print("Warning: No valid current prices to plot.")

    return df_top[['stock', 'rv_score', 'current_price', 'shares_to_buy']]

if __name__ == '__main__':
    try:
        initial_capital_input = float(input("Enter the initial capital: "))
        results_df = run_value_strategy(initial_capital_input)
        print("\nValue Strategy Results:")
        print(results_df)
    except ValueError:
        print("Invalid input. Please enter a numeric value for the capital.")