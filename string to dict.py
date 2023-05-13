def str_to_dict(p):
    """iterate input string"""
    my_keys = []
    my_vals = []
    items = []
    for i in p:
        if i in "{},:'":
            pass
        else:
            items.append(i)

    """slip items into words"""
    joyner = ''.join(items).split()
    """sort to keys and values"""
    for i in range(len(joyner)):
        if (i % 2) == 0:
            my_keys.append(joyner[i])
        else:
            my_vals.append(joyner[i])

    """create new dictionary"""
    final_approach = {}
    for i in range(len(my_keys)):
        final_approach.update({my_keys[i]: my_vals[i]})

    return final_approach
