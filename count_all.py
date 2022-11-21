def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    x=0
    y=0
    for i in txt:
        if i.isalpha():
            x+=1
        if i.isdigit():
            y+=1
        else:
            pass
        
    return {"LETTERS": x, "DIGITS": y }
print(count_all("Hello World"))