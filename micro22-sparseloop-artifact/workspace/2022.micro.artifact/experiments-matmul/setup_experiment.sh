#!/bin/bash

# Check if an argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <experiment_name>"
    exit 1
fi

# Get the experiment name from argument
exp_name=$1

# Create the experiment directory
exp_dir="experiment-${exp_name}"
mkdir -p "$exp_dir"

# Copy files from timeloop_output_test_3
cp -r timeloop_output_test_3/* "$exp_dir/"

# Copy searched_mapping.yaml
cp searched_mapping.yaml "$exp_dir/"

echo "Created $exp_dir and copied required files"
