# 2. Data quality check

# Create a function that checks a list that it contains exactly ten elements, 
# and none of them contains None. If they contain None, 
# print out an error message that says that it is invalid and print out what a 
# valid format should be.

def check_data_quality(data):
    if len(data) != 10:
        print("Error! The list must contain exactly 10 elements.")
        return False
    
    for index, item in enumerate(data):
        if item is None:
            print(f"Error! Element at index {index} is type None.")
            return False
    
    print("Data is valid.")
    return True

# Testa med en lista som är korrekt
data_valid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check_data_quality(data_valid)

# Testa med en lista som har mindre än 10 element
data_short = [1, 2, 3]
check_data_quality(data_short)

# Testa med en lista som har ett None-värde
data_none = [1, 2, None, 4, 5, 6, 7, 8, 9, 10]
check_data_quality(data_none)