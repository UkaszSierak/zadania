from decimal import Decimal
from typing import *
Number = Union[int, float, complex, Decimal]

def GenerateDecimal(min_val: Optional[Number] = 2, max_val: Optional[Number] = 5.5, jump: Optional[Number] = 0.5)-> Decimal:

        while min_val <= max_val:
            yield Decimal(min_val)
            min_val += jump



