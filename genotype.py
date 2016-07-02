'''
Created on Aug 6, 2013

@author: heather
'''
import csv, os, sys

class Genotype:
   
    SNPs = dict()
    
    def loadSNPFile(self, filepath):
        filename, file_extension = os.path.splitext(filepath)
        if 'vcf' in file_extension:
            print "interpreting as a VCF file"
            csv.field_size_limit(1000000000)
            # load a tab delimited file of SNPs -> genotypes (like 23andme generates)
            print "reading  data from " + filename 
            reader = csv.reader(open(filepath, "rU"), delimiter='\t')
            print "length of file: ", reader.line_num
            i = 0

            for row in reader:
                print i
                i = i + 1
                if '#' in row[0]: 
                    print row
                    continue
                if (len(row) == 10):
                    rsid = row[2]
                    ref = row[3]
                    alt = row[4]
                    data = row[9]
                    allele1 = data[0]
                    allele2 = data[2]
                    genotype = ""
                    if allele1[0] == '0': genotype = genotype + ref 
                    elif allele1[0] == '1': genotype = genotype + alt 
                    else: 
                        print allele1, " issue with ", rsid
                        print row
                    
                    if allele2[0] == '0': genotype = genotype + ref
                    elif allele2[0] == '1': genotype = genotype + alt 
                    else: 
                        print allele2, " issue with ", rsid
                        print row
                    
                    self.SNPs[rsid] = genotype  # set SNP -> genotype value

            print "done reading VCF file"
        else:
            print "interpreting as a 23andme or exemplar formated data file"
            # load a tab delimited file of SNPs -> genotypes (like 23andme generates)
            print "reading  data from " + filename 
            reader = csv.reader(open(filepath, "rU"), delimiter='\t')
            for row in reader:
                if row[0] == '#': continue
                if (len(row) == 4):
                    self.SNPs[row[0]] = row[3]  # set SNP -> genotype value
                elif (len(row) == 2):
                    self.SNPs[row[0]] = row[1]  # set SNP -> genotype value exemplar format
            print "done reading data file"
        
    def getSNPvalue(self, snp):
        if self.SNPs.has_key(snp):
            return self.SNPs[snp]
        else:
            return -1

        
