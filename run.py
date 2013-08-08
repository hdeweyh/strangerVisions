'''
Created on Aug 6, 2013

@author: Heather Dewey-Hagborg
'''



if __name__ == '__main__':
    from genotype import*
    from phenotype import*

    genotype = Genotype()
    phenotype = Phenotype()
    
    genotype.loadSNPFile("/Users/heather/Documents/strangerVisions/SNP_files/genome_Thomas_Dexter_Full_20130621222828.txt")
    
    phenotype.loadPossibleSNPs("/Users/heather/Documents/strangerVisions/SNPs_public.csv")

    phenotype.mapGenoToPheno(genotype.SNPs)
    