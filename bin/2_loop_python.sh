#!/bin/bash

# Ensure the data directory exists
mkdir -p ./data

log="./data/LOOP_command_line_arguments.log"
error_log = "./data/LOOP_command_line_arguments.error.log"

# this is the syntax for lists in bash. Notice (), lack of spaces, and no commas.
number_of_objects=(5 18 100)

# you MUST use double quotes to wrap strings with spaces
object_type=("bananas" "pool floats" "finger nail clippings")
diabolical_plan=("take over the world" "destroy the animals" "dig to the center of the earth")

for number_of_objects in ${number_of_objects[@]}; do
   for object_type in ${object_type[@]}; do
      for diabolical_plan in ${diabolical_plan[@]}; do
         python ./src/5_command_line_arguments.py \
            --number_of_objects $number_of_objects \
            --object_type $object_type \
            --diabolical_plan $diabolical_plan >> $log
      done
    done
done

#  2> this is standard error. 
#  2> /dev/null # this will suppress the error messages


# UP TO THIS POINT WE HAVE BEEN COPY AND PASTING TO THE TERMINAL.
# HOWEVER, YOU CAN RUN ENTIRE BASH SCRIPTS AS FOLLOWS
# set up permissions (do this once)
   #  chmod +x ./bin/2_loop_python.sh
# then from there on out:
   # bash file_name.sh

# in this case:
   # bash ./bin/2_loop_python.sh