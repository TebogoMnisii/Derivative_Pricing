import numpy as np

def monte_carlo(S, K, T, r, sigma, num_simulations=10000, option_type='call'):
    z = np.random.standard_normal(num_simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * z)

    if option_type == 'call':
        payoffs = np.maximum(ST - K, 0)
    elif option_type == 'put':
        payoffs = np.maximum(K - ST, 0)
    else:
        raise ValueError("Invalid option_type. Use 'call' or 'put'.")

    option_price = np.exp(-r * T) * np.mean(payoffs)
    return option_price
