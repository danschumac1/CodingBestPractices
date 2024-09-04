
import pandas as pd

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
print(df)
print("I am using pandas version", pd.__version__)

# Python is great

# But it always changes and that is a pain

# save yourself (AND OTHERS) hassle by creating a requirements.txt file


# this will make it easier to install all the packages you need

# and it will make it easier for others to install the packages they need

# here is a simple way to do it
    # 1. run the following command in your terminal
        # pip freeze > ./resources/requirements.txt
    # 2. now you have a requirements.txt file that you can use to install all the packages you need
        # pip install -r ./resources/requirements.txt

# now when dr. rios runs your code, he won't hate you.
# and when you run your code on a new computer, you won't hate yourself. :)