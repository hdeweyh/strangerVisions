'''
Created on Aug 6, 2013

@author: heather
'''
import csv

class Genotype:
   
    SNPs = dict()
    
    def loadSNPFile(self, filename):
        #load a tab delimited file of SNPs -> genotypes (like 23andme generates)
        print "reading  data from " + filename 
        reader = csv.reader(open(filename, "rU"), delimiter='\t')
        for row in reader:
            if (len(row) == 4):
                self.SNPs[row[0]] = row[3] #set SNP -> genotype value
        print "done reading SNP file"
        
    def getSNPvalue(self, snp):
        if self.SNPs.has_key(snp):
            return self.SNPs[snp]
        else:
            return -1