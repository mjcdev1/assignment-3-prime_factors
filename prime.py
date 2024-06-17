"""
prime.py -- Write the application code here
"""

def generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError()
        
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    return factors
    
print(generate_prime_factors(4))