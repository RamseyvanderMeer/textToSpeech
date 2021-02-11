#imports
import pyttsx3
import pdfplumber
import PyPDF2

#Name of PDF to be converted
name = "The Rising of the Shield Hero Vol 02"

file = './pdf/The Rising of the Shield Hero Vol 02.pdf'

pdfFileObj = open(file, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pages = pdfReader.numPages

total = ''

with pdfplumber.open(file) as pdf:
    for i in range(0,pages):
        page = pdf.pages[i]
        text = page.extract_text()
        pg = "https://mp4directs.com" 
        #remove page numbers with page marking
        #print("Page | %d" % (pg))
        text = text.replace("%s" % (pg),"") 
        #print(text)
        total = total + text

        
print(total)

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate+85)
speaker.save_to_file(total , './output/The Rising of the Shield Hero Vol 02.mp3')
#speaker.say(total)
speaker.runAndWait()
