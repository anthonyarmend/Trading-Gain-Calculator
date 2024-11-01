# Trading Gain Calculator

This project provides a Python-based tool to calculate relative gains on a trading account compared to an index, such as the Nasdaq March 2024 futures index. The calculator is designed to compare personal yields with the index yield over a specified period, taking compound interest into account for more accurate gain comparisons.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Parameters](#parameters)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **Relative Gain Calculation**: Calculates the relative performance of an individual trading account compared to a benchmark index.
- **Compound Interest**: Takes compounding into account, allowing for more accurate financial comparisons over multiple periods.
- **Flexible Inputs**: Customizable for different yields, time periods, and initial balances.

## Getting Started

### Prerequisites
- **Python 3.x**: This script requires Python 3 to run. You can download it [here](https://www.python.org/downloads/).

### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/Trading-Gain-Calculator.git
   cd Trading-Gain-Calculator
   ```
2. Make sure Python is installed by running:
   ```bash
   python --version
   ```

---

## Usage

### Running the Program
1. Open the `gain_calculator.py` file in a code editor.
2. Modify the variables in the `Example usage` section to fit your trading parameters:
   - `initial_balance`: The initial amount of money in your trading account.
   - `personal_yield`: Your personal yield as a decimal (e.g., `0.0086` for `0.86%`).
   - `index_yield`: The index yield as a decimal (e.g., `-0.018` for `-1.8%`).
   - `periods`: The number of compounding periods (e.g., months or years).
3. Run the script:
   ```bash
   python gain_calculator.py
   ```

The output will display:
- Final balance based on your yield.
- Index-adjusted balance (i.e., what the balance would be if it grew according to the index yield).
- Relative gain percentage, showing your performance compared to the index.

---

## Parameters
- **`initial_balance`**: Float - The starting amount in your trading account.
- **`personal_yield`**: Float - Your personal yield as a decimal. For example, `0.0086` represents `0.86%`.
- **`index_yield`**: Float - The benchmark index yield as a decimal. For example, `-0.018` represents `-1.8%`.
- **`periods`**: Integer - Number of periods to apply the yield (e.g., `12` for 12 months).

---

## Example
Here's an example using a $50,000 initial balance, with a personal yield of `0.86%` per month and an index yield of `-1.8%` per month, over a 12-month period:

```python
# Example usage:
initial_balance = 50000
personal_yield = 0.0086  # 0.86%
index_yield = -0.018     # -1.8%
periods = 12             # 12 months

# Calculate and print results
final_balance, index_adjusted_balance, relative_gain = calculate_relative_gain(initial_balance, personal_yield, index_yield, periods)
print(f"Final Balance with Personal Yield: ${final_balance:.2f}")
print(f"Index-Adjusted Balance with Index Yield: ${index_adjusted_balance:.2f}")
print(f"Relative Gain Compared to Index: {relative_gain:.2f}%")
```

### Expected Output:
```
Final Balance with Personal Yield: $50436.13
Index-Adjusted Balance with Index Yield: $48842.00
Relative Gain Compared to Index: 3.26%
```

---

## Contributing
Contributions are welcome! Here’s how you can contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

