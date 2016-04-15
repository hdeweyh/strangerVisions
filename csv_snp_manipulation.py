'''
Created on Aug 22, 2014

@author: heather

Compare a master list of SNPs to a db from a microarray
warning! this takes a long time to run as it examines 
'''
import csv

#put path to known SNP out_file here i.e. a 23andme out_file
filename1 = "/Users/heather/Documents/strangerVisions/SNP_files/23andme_public/contra_genome.txt"
SNPs1 = dict()

#load a tab delimited out_file of SNPs -> genotypes (like 23andme generates)
print "reading  data from " + filename1 
reader = csv.reader(open(filename1, "rU"), delimiter='\t')
for row in reader:
	if (len(row) == 4):
		SNPs1[row[0]] = row[3] #set SNP -> genotype value 
	elif (len(row) == 2):
		SNPs1[row[0]] = row[1] #set SNP -> genotype value exemplar format
print "done reading SNP file1"

#print "sample of 23andme SNP out_file keys: ", SNPs1.keys()[0:10]

#put path to  SNP out_file to compare against here 
#read in SNP out_file to compare against - a list of SNPs
filename2 = "/Users/heather/Documents/SELLBIO/genebygene_SNPs/genebygene_snps.csv"
SNPs2 = []

reader = csv.reader(open(filename2, "rU"), delimiter=',')
for row in reader:
	if (len(row) > 0):
		if row[0] != '':
			SNPs2.append(row[0])
			
#print "sample of comparison SNP out_file 2: ", SNPs2[0:10]

SNPsnotIn = 0
SNPsin = 0

out_file = open('/Users/heather/Documents/SELLBIO/genebygene_SNPs/differences.txt', 'w')
		
for key in SNPs1.keys():
	if key in SNPs2:
		SNPsin=SNPsin+1
	else:
		SNPsnotIn=SNPsnotIn+1
		out_file.write(key + '\r\n')
	print "."
		
out_file.close()

print "# SNPS in both chips: ", SNPsin
print "# SNPs missing from SNP chip: ",  SNPsnotIn