import string

def oxford_comma(items):
    # joins a list of strings
    if len(items) <= 1:
    # returns the first item, otherwise returns an empty string
        return items[0]
    # returns two items with and between them
    if len(items) == 2:
        last_item = f' and {items[-1]}'
    # otherwise returns the last item with and before it without a comma
    else:
        last_item = f', and {items[-1]}'
    # constructs the final string
    return f', '.join(items[:-1])  + last_item
