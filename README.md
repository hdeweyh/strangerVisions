Genotype-Phenotype Mapping
===============
This program will interpret a 23andme OR VCF datafile as a predicted phenotype profile
*It is a work in progress! 
I am in the process of adding more info, traits, ancestry, etc. 
It also needs to take account of SNP interactions with each other (I would love some help working on this)
This is the underlying idea behind Stranger Visions, an artwork which imagines what strangers might look like from their DNA.
http://deweyhagborg.com/projects/stranger-visions

Originally designed for 23andme style data tt works with VCF files now too. 
You can generate a larger imputed genotype file from your 23andme results over at DNA Land 
https://dna.land/

This program requires Python 2.7.12 and Biopython
~~~

run w/ cmdline args
a 23andme datafile and the included SNPS database CSV file, ie.:

$ python run.py "/Users/name/Documents/SNP_files/genome_NAME.txt" "/Users/name/Documents/workspace/genotype-phenotype/src/SNPs_public.csv"


For an example 23andme data file see:
https://github.com/msporny/dna
https://github.com/orta/dna

