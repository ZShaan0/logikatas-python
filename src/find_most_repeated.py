def find_most_repeated(elements):
    if not elements:
        return {"elements": [], "repeats": None}
    
    unique_elements = set(elements)
    elements_dict = {element : 0 for element in unique_elements}

    for element in elements:
        if element in elements_dict.keys():
            elements_dict[element] += 1
    
    if max(elements_dict.values()) <= 1:
        return {"elements": [], "repeats": None}

    result = {
        "repeats": max(elements_dict.values())
    }
    result["elements"] = sorted([key for key in elements_dict if elements_dict[key] == result["repeats"]])
    return result

a = find_most_repeated(["foo", "foo", "bar", "hello", "world"])
print(a)