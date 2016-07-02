'''
Created on Aug 6, 2013

@author: Heather Dewey-Hagborg

run w/ cmdline args
a 23andme datafile and the included SNPS database CSV file, ie.:

$ python run.py "/Users/name/Documents/SNP_files/genome_NAME.txt" "/Users/name/Documents/workspace/genotype-phenotype/src/SNPs_public.csv"


For an example 23andme data file see:
https://github.com/msporny/dna
https://github.com/orta/dna
'''



if __name__ == '__main__':
    from genotype import*
    from phenotype import*
    import sys
    
    if len(sys.argv) < 3:
        print "this program requires 2 arguments to run, a data file path as well as a SNP CSV database path."
        sys.exit(-1)
    
    dataFile = sys.argv[1]
    snpFile = sys.argv[2]
    
    genotype = Genotype()
    phenotype = Phenotype()
    
    genotype.loadSNPFile(dataFile)
    
    phenotype.loadPossibleSNPs(snpFile)

    phenotype.mapGenoToPheno(genotype.SNPs)
    