# Program to calculate trading gains relative to the Nasdaq March 2024 futures index

# Define a function to calculate relative gains
def calculate_relative_gain(initial_balance, personal_yield, index_yield, periods):
    """
    Calculate the gain on a trading account relative to an index over a specified number of periods
    using compound interest formula.
    
    Parameters:
        initial_balance (float): Initial balance of the trading account.
        personal_yield (float): Personal yield per period (as a decimal, e.g., 0.0086 for 0.86%).
        index_yield (float): Index yield per period (as a decimal, e.g., 0.018 for -1.8% if negative).
        periods (int): Number of periods (e.g., months, years) over which to calculate the relative gain.

    Returns:
        tuple: Final balance, index-adjusted balance, and relative gain in terms of percentage.
    """
    # Calculate final account balance with personal yield compounded over the periods
    final_balance = initial_balance * ((1 + personal_yield) ** periods)
    
    # Calculate final account balance if only following the index yield (benchmarking)
    index_adjusted_balance = initial_balance * ((1 + index_yield) ** periods)
    
    # Calculate the relative gain as the difference in percentage terms
    relative_gain = ((final_balance - index_adjusted_balance) / index_adjusted_balance) * 100
    
    return final_balance, index_adjusted_balance, relative_gain


# Example usage:
# Assume a $50,000 initial balance, 0.86% personal yield per period, -1.8% index yield per period, over 12 months
initial_balance = 50000
personal_yield = 0.0086  # 0.86%
index_yield = -0.018    # -1.8%
periods = 12            # for 1 year

# Calculate the results
final_balance, index_adjusted_balance, relative_gain = calculate_relative_gain(initial_balance, personal_yield, index_yield, periods)

# Output the results
print(f"Final Balance with Personal Yield: ${final_balance:.2f}")
print(f"Index-Adjusted Balance with Index Yield: ${index_adjusted_balance:.2f}")
print(f"Relative Gain Compared to Index: {relative_gain:.2f}%")
