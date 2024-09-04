#!/bin/bash

# here we call the python script explicitly defining the arguments as we go.
mkdir -p ./data

python ./src/5_command_line_arguments.py \
    --number_of_objects 5 \
    --object_type "bananas" \
    --diabolical_plan "take over the world" > ./data/diabolical.out

python ./src/5_command_line_arguments.py \
    --number_of_objects 18 \
    --object_type "pool floats" \
    --diabolical_plan "destroy the animals" >> ./data/diabolical.out

python ./src/5_command_line_arguments.py \
    --number_of_objects 100 \
    --object_type "finger nail clippings" \
    --diabolical_plan "dig to the center of the earth" >> ./data/diabolical.out
