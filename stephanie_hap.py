#!/usr/bin/env bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=1-00:00
#SBATCH --mem=8000M
#SBATCH --job-name="hap.py 60x test"

export HGREF=~./projects/def-msteiner/readdepth/ref_genome/human_g1k_v37.fa
echo $HGREF

source $HOME/hap.py/bin/activate

hap.py HG001_GRCh37_NA12878.vcf scratch/vcf/HuRef60x.testmem.vcf -r human_g1k_v37.fasta -o test.hap.py.60x

echo "output"
ls test.hap.py.60*
