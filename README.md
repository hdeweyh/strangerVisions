strangerVisions
===============
This program will interpret a 23andme datafile as a phenotype profile
*It is a work in progress! I am in the process of adding more info, traits, ancestry, etc. 

run w/ cmdline args
a 23andme datafile and the included SNPS database CSV file, ie.:

$ python run.py "/Users/name/Documents/SNP_files/genome_NAME.txt" "/Users/name/Documents/workspace/genotype-phenotype/src/SNPs_public.csv"


For an example 23andme data file see:
https://github.com/msporny/dna
https://github.com/orta/dna

It works with VCF files too now, you can generate a larger imputed genotype file over at
DNA Land 
https://dna.land/