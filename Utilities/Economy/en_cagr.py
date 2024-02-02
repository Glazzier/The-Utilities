def calculate_cagr(initial, final, periods):
    cagr = (final / initial) ** (1 / periods) - 1
    return cagr

initial_investment = 10000
final_investment = 15000
periods = 3

cagr_rate = calculate_cagr(initial_investment, final_investment, periods)

print(f"The Compound Annual Growth Rate (CAGR) is: {cagr_rate:.2%}")