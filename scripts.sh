#!/bin/bash

# Number of iterations
ITERATIONS=3

for (( i=0; i<$ITERATIONS; i++ ))
do

	# load init dataset into gen_train/gen_0
	python data/tbbt/preprocess.py


    # Prepare step
    python data/tbbt/prepare.py --gen=$i
    
    # Train step
    python train.py config/train_tbbt.py --eval_iters=20 --device=cpu --compile=False --log_interval=10 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
    
    # Sample step
    GEN_SAMPLE=$((i + 1))
    python sample.py --gen=$GEN_SAMPLE --out_dir=tbb_out --device=cpu
done
