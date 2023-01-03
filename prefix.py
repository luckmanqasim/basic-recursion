def prefix_items(partial_strings, digit):
    if len(partial_strings) == 0:
        return []
    else:
        new_item = str(digit) + partial_strings[0]
        return [new_item] + prefix_items(partial_strings[1:], digit)

print(prefix_items(["1","2","3"], "1"))
