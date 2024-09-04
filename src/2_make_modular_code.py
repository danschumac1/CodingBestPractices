import json

# Loading the diagnosis mapping from a JSON file
with open('./resources/diagnosis_mappings.json') as f:
    diagnosis_mapping = json.load(f)

def diagnose_lab_or_vital(lab_vital_name: str, value: float) -> str:
    """
    Diagnoses a condition based on lab or vital sign values using a predefined mapping.
    
    :param lab_vital_name: The name of the lab or vital sign (e.g., 'SpO2', 'HR').
    :param value: The value of the lab or vital sign.
    :return: A diagnosis string if the value is outside the normal range, otherwise None.
    """
    mapping = diagnosis_mapping.get(lab_vital_name)
    
    if not mapping:
        return "Lab/Vital name not found in the mapping."

    # Initialize high_range and low_range to None
    high_range = mapping.get('high_range')
    low_range = mapping.get('low_range')

    # Handle cases with only a high range and diagnosis
    if high_range is not None and value >= high_range:
        return mapping.get('diagnosis_high', 'No high diagnosis defined')
    
    # Handle cases with only a low range and diagnosis
    if low_range is not None and value <= low_range:
        return mapping.get('diagnosis_low', f"No low diagnosis defined for {lab_vital_name}")

    # If no diagnosis is made, return that the value is within the normal range
    return f"{lab_vital_name} is within the normal range."


# Test cases
print(diagnose_lab_or_vital("SpO2", 85))        # Expected: Hypoxemia
print(diagnose_lab_or_vital("HR", 102))         # Expected: Tachycardia
print(diagnose_lab_or_vital("Temp", 101))       # Expected: Fever
print(diagnose_lab_or_vital("BG", 65))          # Expected: Hypoglycemia
print(diagnose_lab_or_vital("Cholesterol", 250))# Expected: Lab/Vital name not found in the mapping.
print(diagnose_lab_or_vital("Temp", 98.6))      # Expected: Temp is within the normal range

#endregion
#region # THE BAD WAY TO DO THIS (IMO)
# =============================================================================
# THE BAD WAY TO DO THIS (IMO)
# =============================================================================
# MAKE A FUNCTION FOR EACH LAB/VITAL
def diagnose_spo2(value):
    if value < 90:
        return "Hypoxemia"
    else:
        return "Normal"
    
def diagnose_hr(value):
    if value > 100:
        return "Tachycardia"
    else:
        return "Normal"

def diagnose_temp(value):
    if value > 100:
        return "Fever"
    else:
        return "Normal"

def diagnose_bg(value):
    if value < 70:
        return "Hypoglycemia"
    else:
        return "Normal"
    
# now if say the physician wants to change the bg threshold, the have to edit the python code itself 
# rather than just changing a json file