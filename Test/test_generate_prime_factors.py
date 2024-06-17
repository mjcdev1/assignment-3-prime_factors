import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

import prime

import pytest

def test_not_int():
    with pytest.raises(ValueError):
        prime.generate_prime_factors("hello")
        prime.generate_prime_factors(3.5)
        prime.generate_prime_factors([2, 3])
        
def test_for_one():
    assert prime.generate_prime_factors(1) == []