def flat(test_list):
    if isinstance(test_list, list):
        l = []
        for i in test_list:
            l.extend(flat(i))
        return l
    else:
        return [test_list]

test_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
result = flat(test_list)
print(result)
