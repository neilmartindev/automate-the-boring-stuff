import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('meetingminutes.pdf', 'rb'))

print(pdfReader.isEncrypted)

print(pdfReader.getPage(0))
