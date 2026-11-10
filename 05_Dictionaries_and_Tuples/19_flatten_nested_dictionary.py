# Q19. Flatten a dictionary that may contain nested dictionaries so that all keys appear in a single-level dictionary, using dot-separated keys.
def flatten_dictionary(dictionary, prefix=''):
    flattened = {}
    for key, value in dictionary.items():
        new_key = f"{prefix}.{key}" if prefix else str(key)
        if isinstance(value, dict):
            flattened.update(flatten_dictionary(value, new_key))
        else:
            flattened[new_key] = value
    return flattened

nested_dict = {
    "name": "Rahul",
    "age": 25,
    "address": {
        "city": "Bhubaneswar",
        "state": "Odisha",
        "zip": {"code": 751001, "area": "Cuttack Road"}
    },
    "hobbies": ["reading", "painting"]
}
print(flatten_dictionary(nested_dict))
