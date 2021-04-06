from pikepdf import _cpphelpers
from DarkModePptx import convert_pptx
from DarkModePdf import pdf_to_images, image_to_pdf
import os
import magic

print("******* Welcome to the DARK SIDE! *******")
filePathName = input("Where is the file? : ")
outputpath = input("Where should I save it? (just press enter if you want it to be saved in the same folder): ")
print("******* Got it, let me do some DARK magic! *******")

def find_file_type(filePathName,outputpath = None):
    filecheck = magic.from_file(filePathName, mime=True)
    filename = os.path.basename(filePathName)
    filePathName = os.path.dirname(os.path.abspath(filePathName))
    if(outputpath == None):
        outputpath = filePathName
    if(filecheck == 'application/pdf'):
        return convert_pdf(filename,filePathName,outputpath)
    elif(filecheck == 'application/vnd.openxmlformats-officedocument.presentationml.presentation'):
        return convert_pptx(filename, filePathName,outputpath)

def convert_pdf(filename,inputpath,outputpath):
    pdf_to_images(filename, inputpath)
    num_pages,pid = image_to_pdf(filename, inputpath,outputpath)
    path_to_file = os.path.join(outputpath, 'DarkFile.pdf')
    os.remove('temp.jpg')
    for i in range(num_pages):
        number = str(i)
        name = 'temp' + number + '.pdf'
        os.remove(name)


find_file_type(filePathName)
a = input("******* Sorcery complete press any key to exit *******")
