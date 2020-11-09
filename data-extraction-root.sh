#!/bin/bash
#SBATCH --job-name="data_extraction_root"
#SBATCH -e data_extraction_root.err
#SBATCH -p common
#SBATCH -c 6
#SBATCH --mem=25G

source /hpc/home/jvp5/storage/venv/bin/activate

# Run 
python data_extraction/data_extraction_root.py \
--eicu_dir='physionet.org/files/eicu-crd/2.0' \
--output_dir='data'