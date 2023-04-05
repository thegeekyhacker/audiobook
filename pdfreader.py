from PyPDF2 import *
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
bname = input("Enter the name of the book you want to read : ")
book_name = bname + ".pdf"
bookf = open(book_name,"rb")
bookobj = PdfFileReader(bookf)
pageno = bookobj.getNumPages()
for i in range (pageno):
    bookp = bookobj.getPage(i)
    bookp = bookp.extractText()
    print(bookp)
    speak(bookp)  