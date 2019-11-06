def PowersetList(list):
    result = [[]]
    for a in list:
        result.extend([x+[a] for x in result])
    return result

