from typing import *

def CheckValues(values: List[int], max_value: int) -> List[int]:

    comparison_list = list(range(1,max_value+1))
    result = []

    for value in comparison_list:
        if value not in values:
            result.append(value)

    return result

