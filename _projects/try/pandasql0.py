import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pandasql as psql
import os
from libdefinitions import *

def listdir (path):
    printSectionHead(os.listdir(path))

def load_sourcefile (filename):
    printSectionHead ('Reading source file <%s>' % (filename))
    filedf = pd.read_csv(filename,header=0)
    printSectionHead ('Finished Reading source file <%s>' % (filename))
    return filedf
if __name__ == "__main__":
    sourcefile = '../toy_dataset.csv'
    sourcepath = """C:/Development/python/try/pandasql/"""
    sourcefile = 'toy_dataset.csv'
    fullsourcefilename = sourcepath + sourcefile
    # listdir (sourcepath)
    toydf = load_sourcefile (fullsourcefilename)
    printSectionHead("toydf head")
    print(toydf.head())
    printSectionHead("Cities: ")
    print(toydf.City.unique())
    printSectionHead("Income:")
    print(toydf.Income.describe())

    printSectionHead("Getting Query")
    sdfc = psql.sqldf("SELECT Age, Income FROM toydf limit 5")
    print('\nsdcf head \n', sdfc.head())

