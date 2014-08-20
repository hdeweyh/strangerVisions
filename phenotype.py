'''
Created on Aug 6, 2013

@author: heather
'''
import csv
from trait import*
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

class Phenotype:
    
    traits = dict() #actual traits of this genotype
    
    possibleTraitsList = [] #various possible traits
    possibleTraits = dict()


        
    def loadPossibleSNPs(self, filename):
        #load a CSV of SNPs -> traits 
        print "reading  data from " + filename 
        reader = csv.reader(open(filename, "rU"), delimiter=',')
        for row in reader:
            #print row
            if (len(row) >= 8):
                if row[0] == '':
                    continue
                trait = Trait(row[0], row[-1])
                i=1
                while i< (len(row)-1):
                    trait.addAllele(row[i], row[i+1]) 
                    i=i+1
                
                self.possibleTraits[trait.rsid] = trait #add this new trait to dict indexed by RSID
                self.possibleTraitsList.append(trait) #add to list of traits as well
                #print trait
            else:
                print "row of incorrect length" , row
                
        print "done reading possible SNPs\n"
        
    def mapGenoToPheno(self, genotype):
        #for each possible trait see if we have a genotype
        #if we do add it with its value to the traits dict
        for trait in self.possibleTraitsList:
            if genotype.has_key(trait.rsid):
                self.traits[trait.rsid] = genotype[trait.rsid]
                if trait.alleles.has_key(genotype[trait.rsid]):
                    print trait.rsid, " - ", genotype[trait.rsid], " - ", trait.alleles[genotype[trait.rsid]]
                else:
                    #try reverse complement
                    #print genotype[trait.rsid]
                    my_dna = Seq(genotype[trait.rsid], generic_dna)
                    rev = str(my_dna.complement())
                    #print rev
                    if trait.alleles.has_key(rev):
                        print trait.rsid, " - ", rev, " (rev comp) -", trait.alleles[rev]
                    else:
                        print "genotype " , genotype[trait.rsid], "and rev comp " , rev, " not found in traits for " , trait.rsid   
                        
            else:
                print "genotype not found for ", trait.rsid, " available genotype mappings: ", trait.alleles
                