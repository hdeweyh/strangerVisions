# -*- coding: utf-8 -*-

'''
A simple class to handle pretty prints of Genotype data in the console
'''

import texttable, os

class Console:
    def __init__(self):
        self.table = texttable.Texttable()
        self.table.set_deco(texttable.Texttable.HEADER)
        # to get the size on the console.
        rows, columns = os.popen('stty size', 'r').read().split()
        self.width = int(columns)

    def printTable(self, results):
        # Results is an array of dictionnaries returned by the map2pheno command
        header = ['rsid', 'ge', 'f', 'r', 'allele' ]
        self.table.header(header)
        # Will use the maximum width to display the table
        # There is 3 characters between each colum.
        self.table.set_cols_width( [10, 2, 1, 1, self.width - 27] )

        for item in results:
            row = [
                item['rsid'],
                item['genotype'] if 'genotype' in item  else "",
                "✓" if 'flipped' in item and item['flipped'] else "",
                "✓" if 'revComp' in item and item['revComp'] else "",
                item['allele'] if item['allele'][0:3] != 'NOT' else bcolors.RED + item['allele'] + bcolors.ENDC
            ]
            self.table.add_row( row )

        print( self.table.draw() )

class bcolors:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
