# !/binbash
# this ^^^ exactly as written has to be the top thing of your file
# it has a fun name: shebang
# Without it, the system may try to run the script with a different shell, leading to errors if the syntax is different.

# =============================================================================
# CREATING VARIABLES
# =============================================================================
# you CANNOT uses spaces around the = sign
age=1

# you MUST use double quotes to wrap strings with spaces
name="Gemma" # shout out to my cute dogo

# this is the syntax for lists in bash. Notice (), and no commas.
numbers=(1 2 3)

# using a variable in a string
echo "My dogo's name is $name"

# using multiple variables in a string
echo "My dogo's name is $name and she is $age years old"


# =============================================================================
# BASIC COMMANDS
# =============================================================================
# echo
echo "echo prints to the console"

# combined with a variable
# use the $ sign to access a variable inside of a string (kinda like f strings in python without the f)

echo "echo with a variable: Hello, $name"

# cd
# change directory
# back up
cd ../

# to a specific place
# you will need to change this to run on your machine
cd /home/dan/coding_best_practices_presentation/resources

# take me back!!
cd -


# =============================================================================
# OUTPUT REDIRECTION
# =============================================================================
# I always make sure that the data directory exists
mkdir -p ./data

name="Louisa"
echo "My dogo's name is $name" > "./data/echo1.txt"

# append to a file
name="Gemma"
echo "My puppy's name is $name" >> "./data/echo1.txt"

# If I go back to using >, it will overwrite the file
name="Paige"
echo "My wife's name is $name, notice Louisa and Gemma are gone!" > "./data/echo1.txt"

# =============================================================================
# CONDITIONALS
# =============================================================================
name="Gemma"
name="Louisa"
name="Dan"
if [ $name == "Gemma" ]; then
    echo "Gemma is the best puppy"
elif [ $name == "Louisa" ]; then
    echo "Louisa is the best dog"
else
    echo "You are not Gemma or Louisa"
fi

# =============================================================================
# FOR LOOPS
# =============================================================================
# simple example
numbers=(1 2 3)
for number in ${numbers[@]}; do
    echo "The number is $number"
done

# simple example redirecting output
mkdir -p ./data
for number in ${numbers[@]}; do
    echo "The number is $number" >> "./data/simple_for_loop.txt"
done

# more complex
number_of_objects=(5 18 100)
object_types=("bananas" "pool floats" "finger nail clippings")
diabolical_plans=("take over the world" "destroy the animals" "dig to the center of the earth")

mkdir -p ./data
for number in "${number_of_objects[@]}"; do
    for object in "${object_types[@]}"; do
        for plan in "${diabolical_plans[@]}"; do
            echo "We will have $number $object and $plan" >> "./data/for_loop.txt"
        done
    done
done

# =============================================================================
# RUNNING PY FILES
# =============================================================================
# you can run other scripts
python ./src/utils/print_num_4.py

# you can redirect output from other scripts
python ./src/utils/print_num_4.py >> ./data/print_num_4.txt

# =============================================================================
# REDIRECTING ERRORS
# =============================================================================
numbers=(4 8 0)
# you cannot divide by 0

# create (or clear) the files
echo "" > ./data/divide_24_by_x.txt
echo "" > ./data/divide_24_by_x_ERRORS.txt

chmod +x ./src/utils/divide_24_by_x.py

for number in ${numbers[@]}; do
    python ./src/utils/divide_24_by_x.py $number >> ./data/divide_24_by_x.txt 2>> ./data/divide_24_by_x_ERRORS.txt
done

