#region # ABOUT FILE
"""
Created on 09/04/2024

@author: Dan Schumacher
ABOUT: This file shows how to set up and run command line arguments, and shows their benifit.
HOW TO RUN: 
    python command_line_arguments.py 
        --number_of_objects 5 \
        --object_type "bananas" \
        --diabolical_plan "take over the world" >> test.out
"""
#endregion

# =============================================================================
# IMPORTS AND SET UP
# =============================================================================
import argparse


# =============================================================================
# CLA set up
# =============================================================================
# Create the parser
parser = argparse.ArgumentParser(description='Return your diabolical plan')
parser.add_argument('--number_of_objects', type=int, help='The number of objects you have')
parser.add_argument('--object_type', type=str, help='The type of object you have')
parser.add_argument('--diabolical_plan', type=str, help='Your diabolical plan')

# Parse the arguments
args = parser.parse_args()

# =============================================================================
# MAIN FUNCTION
# =============================================================================
def main():
    print(f"USING PYTHON SCRIPT: I will {args.diabolical_plan} with my {args.number_of_objects} {args.object_type}")

if __name__ == "__main__":
    main()  