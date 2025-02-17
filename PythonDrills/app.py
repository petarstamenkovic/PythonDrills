# Simple fle that tests module usage

import utils # or from utils import find_max
import ecommerce # from ecommerce.shipping import calculate_shipping or from ecommerce import shipping

numbers = [1,4,76,8,3,6,66,845,13,441]

print(f"Biggest number in the list is: {utils.find_max(numbers)}")




