from typing import *

def PostCodeGen(start_code: str, end_code: str) -> List[str]:

     merge = lambda x:  int(x.replace('-',''))
     begin_val, end_val = merge(start_code) + 1, merge(end_code)

     result = ['{}-{}'.format( x // 1000, x % 1000) for x in range(begin_val,end_val)]
     return result
