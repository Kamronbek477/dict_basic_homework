def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    s={}
    for i in range(len(cities)):
        s[i]=cities[i]

    return s
print(cities_dict(["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]))