def sort_dicts_by_key_ai(data, key):
    """
    Sort a list of dictionaries by the specified key using AI-suggested code.
    """
    return sorted(data, key=lambda x: x.get(key, None))
def sort_dicts_by_key_manual(data, key):
    """
    Sort a list of dictionaries by the specified key manually handling missing keys.
    """
    # Filter out dictionaries that don't have the key to avoid errors
    filtered_data = [d for d in data if key in d]
    # Sort the filtered list by the key
    filtered_data.sort(key=lambda x: x[key])
    return filtered_data