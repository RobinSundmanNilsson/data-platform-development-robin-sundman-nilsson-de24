# c) The dictionary created can be seen as one row,
# now lets create more records and store each record (dictionary) in a list.

records = [
    {"id": 101, "name": "Erika", "is_active": True, "age": 45},
    {"id": 102, "name": "Marcus", "is_active": True, "age": 34},
    {"id": 103, "name": "David", "is_active": False, "age": 29},
    {"id": 104, "name": "Anna", "is_active": True, "age": 41.5},
    {"id": 106, "name": "Ingrid", "is_active": "NOPE", "age": 8},
]

# d) Do schema validation on the JSON array in c)

def validate_data(data):
    expected_data = {
        "id" : int,
        "name" : str,
        "is_active" : bool,
        "age" : int
    }

    results = {}
    for key, expected_type in expected_data.items():
        if key not in data:
            results[key] = "Missing"
        else:
            value = data [key]
            if isinstance(value, expected_type):
                results[key] = True
            else: results[key] = f"Expected {expected_type.__name__}, got {type(value).__name__}"
    return results

for index, record in enumerate(records, start=1):
    print(f"Validating record {index}: {record}")
    validation_results = validate_data(record)
    for key, result in validation_results.items():
        print(f"    {key} : {result}")
    print()

# e) Make a function for schema validation and try input the two examples and see if you get correct answer. 
# Also make other examples and test your function.