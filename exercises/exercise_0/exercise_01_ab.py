# 1. Schema Validation

# In order to maintain data quality, consistency and reliability,
# a system needs to validate that it conforms to certain predefined structure or format.
# This is called schema validation and you'll practice this in the following exercises.

# a) Create a dictionary that look like this:

# Key       : Value
# id        : 101
# name      : Erika
# is_active : True
# age       : 45

data = {
    "id" : 101,
    "name" : "Erika",
    "is_active" : True,
    "age" : 45
    }

# b) Validate that the id is integer, name is string, is_active is boolean and age is integer.
# It should return true if valid and false if not valid.

data = {
    "id" : 101,
    "name" : "Erika",
    "is_active" : True,
    "age" : 45
    }

def check_dictionary(data):
    expected_data = {
        "id": int,
        "name": str,
        "is_active": bool,
        "age": int
    }

    for key, expected_type in expected_data.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True

result = check_dictionary(data)
print(result)

##################################################

# Alternativ lösning:

def check_dictionary(data):
    expected_data = {
        "id": int,
        "name": str,
        "is_active": bool,
        "age": int
    }

    results = {}  # För att lagra resultaten för varje nyckel

    for key, expected_type in expected_data.items():
        if key not in data:
            results[key] = "Missing"
        else:
            results[key] = isinstance(data[key], expected_type)

    return results


# Anropa funktionen och skriv ut resultaten
validation_results = check_dictionary(data)

for key, result in validation_results.items():
    print(f"{key}: {result}")