#!/bin/bash

# ALWAYS MAKE SURE THAT ONE WORKS BEFORE TRYING TO LOOP IT DON'T WASTE YOUR TIME 
# then you can loop it like so:

# Array of context types
contexts=("wrong_date_context" "no_context") #   "random_context" "relevant_context"

# Array of base models
base_models=("gemma-1.1-7b-it") # Add "gemma-1.1-2b-it" if needed

# Log files
log="AQA-IT_LOG.out"
echo "Generation started at $(date)" > ${log}

# Clear the log file at the start
echo "" > $log

# TQE HAS THE DEFAULT EPOCHS
for base_model in "${base_models[@]}"; do
  for context in "${contexts[@]}"; do
    echo -e "\n\nAQA: TRAINING $base_model WITH $context\n\n" | tee -a $log    
    nohup bash -c "CUDA_VISIBLE_DEVICES=0 python fine_tune_gemma_it.py \
     --dataset AQA \
     --epochs 1 \
     --model_context $context \
     --base_model $base_model \
     --batch_size 16" >> $log 2>&1
  
    echo " FINISHED $base_model WITH $context at $(date)" >> ${log}
  done
done
echo "Generation script ended at $(date)" >> ${log}

# chmod +x ./bin/4_actual_looped.sh
# CUDA_VISIBLE_DEVICES=0 bash ./bin/4_actual_looped.sh