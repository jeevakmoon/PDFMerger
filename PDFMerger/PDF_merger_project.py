#pdf merger project
from fileinput import filename
import PyPDF2
import os
from PyPDF2 import PdfFileReader

#merging 2 pdf files
#creating file merger instance 
merger=PyPDF2.PdfFileMerger()

#providing path of the folder
path="C:\\Users\\jeeva\\Downloads"    

#using for loop for accesing file in given directory
for file in os.listdir(path):
        if file.endswith(".pdf"):
                print(file)
#providing location of files
path_of_filename1=input("Enter path of first pdf file:")
path_of_filename2=input("Enter path of second pdf file:")

#this will remove '"' from the path
filename1=path_of_filename1.translate({ord('"'): None})
filename2=path_of_filename2.translate({ord('"'): None})

#this will add second file after first file
merger.append(PdfFileReader(open(filename1, 'rb')))
merger.append(PdfFileReader(open(filename2, 'rb')))

#specify path with name of file
merger.write("C:\\Users\\jeeva\\OneDrive\\Desktop\\Python\\Python Projects\\combined.pdf")
