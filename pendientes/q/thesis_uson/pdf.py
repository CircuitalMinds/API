# importing required modules 
import PyPDF2 
import os
    
# creating a pdf file object 
pdfFileObj = open('alejandra_morales.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
print(pdfReader.numPages) 
    
# creating a page object 
pageObj = lambda n: print(pdfReader.getPage(n).extractText().splitlines())
for n in range(pdfReader.numPages - 1):
    pageObj(n)
    
# closing the pdf file object 
pdfFileObj.close() 
