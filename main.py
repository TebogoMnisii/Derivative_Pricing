from black_scholes import black_scholes
from monte_carlo_pricing import monte_carlo

def run_models():
    S = 100      # Current stock price
    K = 100      # Strike price
    T = 1        # Time to maturity (in years)
    r = 0.05     # Risk-free interest rate
    sigma = 0.2  # Volatility
    option_type = 'call'

    bs_price = black_scholes(S, K, T, r, sigma, option_type)
    mc_price = monte_carlo(S, K, T, r, sigma, option_type=option_type)

    print(f"Black-Scholes {option_type.title()} Price: {bs_price:.2f}")
    print(f"Monte Carlo {option_type.title()} Price: {mc_price:.2f}")

    option_type = 'put'
    bs_price = black_scholes(S, K, T, r, sigma, option_type)
    mc_price = monte_carlo(S, K, T, r, sigma, option_type=option_type)

    print(f"Black-Scholes {option_type.title()} Price: {bs_price:.2f}")
    print(f"Monte Carlo {option_type.title()} Price: {mc_price:.2f}")

if __name__ == "__main__":
    run_models()
