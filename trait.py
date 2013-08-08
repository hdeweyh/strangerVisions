'''
Created on Aug 6, 2013

@author: heather
'''

class Trait(object):
    '''
    classdocs
    '''
    rsid = 0
    alleles = dict()
    references = ""

    def __init__(self, _rsid, _references):
        '''
        Constructor
        '''
        self.rsid = _rsid
        self.references = _references
        self.alleles = dict()
        
    def __str__(self):
        outputStr = "\nRSID: " + self.rsid +"\n"
         
        for i in self.alleles:
            outputStr +=  i + " - " + self.alleles[i]+"\n"
            
        outputStr += "refs: " +  self.references +"\n"
        return outputStr
       
    def addAllele(self, allele, trait):
        self.alleles[allele] = trait