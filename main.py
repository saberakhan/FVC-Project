import random
import collections
from tabulate import tabulate

def simulate_random_walk(steps, simulations):
    final_prices = []
    start_price = 100

    for _ in range(simulations):
        price = start_price
        for _ in range(steps):
            price += random.choice([-1, 1])
        final_prices.append(price)

    return final_prices

def calculate_probabilities(final_prices):
    price_count = collections.Counter(final_prices)
    total_simulations = len(final_prices)
    probabilities = {price: count / total_simulations for price, count in price_count.items()}
    return probabilities

def display_probability_table(probabilities):
    table_data = sorted([[f"£{price}", f"{prob:.4f}"] for price, prob in probabilities.items()])
    headers = ["Final Price", "Probability"]
    print(tabulate(table_data, headers, tablefmt="grid"))

def main():
    while True:
        try:
            S = int(input("Enter the number of steps: "))
            N = int(input("Enter the number of simulations: "))

            if S < 1 or S > 10000 or N < 10 or N > 10000:
                print("Invalid input. S must be between 1 and 10000, and N must be between 10 and 10000.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    final_prices = simulate_random_walk(S, N)
    probabilities = calculate_probabilities(final_prices)

    display_probability_table(probabilities)

    if S == 10 and N == 10000:
        prob_100 = probabilities.get(100, 0)
        print(f"\nProbability that the final share price is £100 when S is 10 and N is 10000 is {prob_100:.4f}")

if __name__ == "__main__":
    main()
