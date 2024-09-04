import time

#region # NO MAIN FUNCTION
# =============================================================================
# NO MAIN FUNCTION
# =============================================================================
def add_two_numbers(a, b):
    return a + b

print("WHOOPS THERE IS CRAP IN YOUR CODE")
print("This is bad because when you import this file, it will run this code.")

# here is some code that will take 10 sec to run and every second it will print a regret that you have

def i_regret_not_having_a_main_function():
    for i in range(10):
        print(f"Regretting for {i} seconds...")
        time.sleep(1)
        
i_regret_not_having_a_main_function()