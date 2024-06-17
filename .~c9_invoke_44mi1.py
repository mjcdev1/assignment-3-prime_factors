"""
prime.py -- Write the application code here
"""

def generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError()
        
    factors = []
    
    div = 2 
    
    while n > 1:
        while n % div == 0:
            factors.append(div)
            n = n // div
        div += 1
        
    return factors
    
print(generate_prime_factors(4))









