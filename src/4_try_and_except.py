# =============================================================================
# ORIGINAL APPROACH WITH TRY/EXCEPT
# =============================================================================

def get_value_from_dict(dictionary, key):
    try:
        return dictionary[key]
    except:
        print('Key not found')

# Test cases
vars = ["name", "age"]
values = ["Dan", 28]

sample_dict = {}
for i in range(len(vars)):
    sample_dict[vars[i]] = values[i]
    continue

sample_dict = {"name": "Dan", "age": 28}

# This works correctly:
print(get_value_from_dict(sample_dict, "name"))  # Output: Dan

# This also works correctly:
print(get_value_from_dict(sample_dict, "city"))  # Output: Key not found

# What if we accidentally pass in a list instead of a dictionary?
sample_list = ['name', 'age']

# This prints "Key not found", but it should raise an error or return None:
print(get_value_from_dict(sample_list, "name"))

# What if we pass in None?
sample_list = None

# This also prints "Key not found", but it should raise an error or return None:
print(get_value_from_dict(sample_list, "name"))

# =============================================================================
# A BETTER WAY: USING SPECIFIC EXCEPTIONS AND IF STATEMENTS
# =============================================================================

# Improved version with specific exception handling:
def get_value_from_dict(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:  # Explicitly catching KeyError
        print('Key not found')
        return None
    except TypeError:  # Explicitly catching TypeError
        print('Provided input is not a dictionary')
        return None
get_value_from_dict(sample_dict, "name")  # Output: Dan
# =============================================================================
# AN EVEN BETTER WAY: USING IF STATEMENTS
# =============================================================================

# Even better approach: using if statements to avoid exceptions when possible:
def get_value_from_dict(dictionary, key):
    if not isinstance(dictionary, dict):
        print('Provided input is not a dictionary')
        return None
    elif key not in dictionary:
        print('Key not found')
        return None
    else:
        result = dictionary.get(key)
        return result

# This method is preferred because:
# 1. It avoids unnecessary exceptions, making the code clearer and more predictable.
# 2. It explicitly checks the input types and conditions, making it easier to understand and debug.
# 3. It provides specific feedback based on the exact problem, helping to diagnose issues faster.

# Test cases with improved function:

# Works correctly:
print(get_value_from_dict(sample_dict, "name"))  # Output: Dan

# Correctly handles missing key:
print(get_value_from_dict(sample_dict, "city"))  # Output: Key not found

# Correctly handles incorrect type (list instead of dictionary):
print(get_value_from_dict(sample_list, "name"))  # Output: Provided input is not a dictionary

# Correctly handles None input:
print(get_value_from_dict(None, "name"))  # Output: Provided input is not a dictionary

# =============================================================================
# I DO USE TRY AND EXCEPT FOR PROCESSES THAT TAKE A LONG TIME 
# (USE YOUR BEST JUDGMENT, SOME PREFER TO LET IT CRASH AND FIX ERRORS ONE BY ONE
# =============================================================================
import pandas as pd

# Sample DataFrame with some intentional issues
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'age': [25, 30, 'thirty-five', None, 45],
    'salary': [70000, 80000, 90000, None, 'Ninety Thousand']
}

df = pd.DataFrame(data)

# List to store any errors that occur during processing
errors_list = []

def process_row(row):
    # Example processing: convert age to integer and salary to float
    name = row['name']
    age = int(row['age'])  # This could fail if age is not an integer or is None
    salary = float(row['salary'])  # This could fail if salary is not a number or is None
    
    # Perform some operations (e.g., calculate retirement age)
    retirement_age = 65 - age
    adjusted_salary = salary * 1.03  # Assume a 3% salary increase
    
    # Return processed data (could be written back to a DataFrame or another structure)
    result_dict = {
        'name': name,
        'retirement_age': retirement_age,
        'adjusted_salary': adjusted_salary
    }
    return result_dict

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    try:
        result = process_row(row)
        print(f"Processed row {index}: {result}")
    except Exception as error:
        # Log the error with row information for later review
        errors_list.append({
            'index': index,
            'row': row.to_dict(),
            'error': str(error)
        })
        print(f"Error processing row {index}: {error}")

# After processing, print all errors encountered
print("\nErrors encountered during processing:")
for error in errors_list:
    print(f"Row {error['index']} | Error: {error['error']} | Data: {error['row']}")

# You can also write these errors to a log file or take further action
