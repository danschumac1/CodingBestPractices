#!/bin/bash

# for my research, I use bash scripts to train models (writing explicitly)
# these backslashes are for readability (otherwise you would need one long line)
CUDA_VISIBLE_DEVICES=0 python fine_tune_gemma_it.py --dataset AQA \
    --epochs 1 \
    --model_context "relevant_context" \
    --base_model gemma-1.1-2b-it \
    --batch_size 16

CUDA_VISIBLE_DEVICES=0 python fine_tune_gemma_it.py --dataset AQA \
    --epochs 1 \
    --model_context "random_context" \
    --base_model gemma-1.1-2b-it \
    --batch_size 16

CUDA_VISIBLE_DEVICES=0 python fine_tune_gemma_it.py --dataset AQA \
    --epochs 1 \
    --model_context "no_context" \
    --base_model gemma-1.1-2b-it \
    --batch_size 16

CUDA_VISIBLE_DEVICES=0 python fine_tune_gemma_it.py --dataset AQA \
    --epochs 1 \
    --model_context "wrong_date_context" \
    --base_model gemma-1.1-2b-it \
    --batch_size 16

# ALWAYS MAKE SURE THAT ONE WORKS BEFORE TRYING TO LOOP IT DON'T WASTE YOUR TIME 
