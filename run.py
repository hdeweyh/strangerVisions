'''
Created on Aug 6, 2013

@author: Heather Dewey-Hagborg
'''



if __name__ == '__main__':
    from genotype import*
    from phenotype import*
    import sys
    
    if len(sys.argv) < 3:
        print "this program requires 2 arguments to run, a 23andme data file path as well as a SNP CSV database path."
        sys.exit(-1)
    
    data_23andmeFile = sys.argv[1]
    snpFile = sys.argv[2]
    
    genotype = Genotype()
    phenotype = Phenotype()
    
    genotype.loadSNPFile(data_23andmeFile)
    
    phenotype.loadPossibleSNPs(snpFile)

    phenotype.mapGenoToPheno(genotype.SNPs)
    