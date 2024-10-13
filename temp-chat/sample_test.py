code1 = """
def my_redundant_sum(x):
    res = 0
    for i in range(x):
        res += j
    for j in range(x):
        res += j
            
    res2 = 0
    for j in range(x):
        res2 += j
            
    return res2
"""

def double_sum(x):
    res = 0
    for i in range(x):
        # 0 to x
        for j in range(x):
            res += j
            
    res2 = 0
    for i in range(x):
        # 0 to x
        for j in range(x):
            res2 += j
            
    return res2

def example_function(x):
    result = 0
    for i in range(x):
        result += i
    return result

