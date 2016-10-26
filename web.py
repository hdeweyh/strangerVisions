import cherrypy
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

from genotype import*
from phenotype import*

import os

class FileUpload(object):
    @cherrypy.expose
    def index(self):
        template = env.get_template('upload.html')
        return template.render()

    @cherrypy.expose
    def upload(self, myFile):
        template = env.get_template('result.html')

        # CherryPy reads the uploaded file into a temporary file;
        # The variable is defined by the name in the html form.
        # In this case, you can access the file like this:  myFile.file
        genotype.loadSNPData(myFile.file)
        results = phenotype.mapGenoToPheno(genotype.SNPs)

        return template.render(results=results)

if __name__ == '__main__':
    # Setting up genotype and phenotype
    genotype = Genotype()
    phenotype = Phenotype()
    phenotype.loadPossibleSNPs("SNPs_public.csv")

    # Starting webserver
    cherrypy.quickstart(FileUpload())
