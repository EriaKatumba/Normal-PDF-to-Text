# importing required modules
import PyPDF2, os, glob, time

print('PROCESSING.........')
pdf_path=r'C:\Users\ERIA\Desktop\PDFs TO PROCESS'
os.chdir(pdf_path)
pdf_list=glob.glob('*.pdf')
pdf_list.sort(key=os.path.getmtime)

count=0
for p in pdf_list:
# creating a pdf file object
	count+=1
	pdfFileObj = open(p,'rb')
	
# creating a pdf reader object
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	
# printing number of pages in pdf file
	tot_pages=pdfReader.numPages
	print('File',count,'has',tot_pages,'pages')

# creating a page object
	for y in range(tot_pages):
		pageObj = pdfReader.getPage(y)
	
# extracting text from page
		text=pageObj.extractText()
		os.chdir(pdf_path)
		name='pdf('+str(count)+')_text.txt'
		with open(name,'a+') as f:
			f.write(text)
			f.write('\n')
	
# closing the pdf file object
pdfFileObj.close()
