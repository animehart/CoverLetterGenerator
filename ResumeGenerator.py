from reportlab.pdfgen import canvas
from docx import Document

def resumeGeneratorTXT(position, company, file):
    f=open(company + "CoverLetter.txt", "w+")
    g=open(file + ".txt","r")
    contents = g.read()
    f.write(ssentence + " " + position + " position with " + company + contents)
    f.close()
    g.close()
    return 0;

def resumeGeneratorPDF(position, company, file): #in progress
    g=open(file + "txt","r")
    contents = g.readlines()
    
    c = canvas.Canvas(company + "coverLetter.pdf")
    
    textobject = c.beginText()
    textobject.setTextOrigin(10, 730)
    textobject.setFont('Times-Roman', 12)
    for x in contents:
        textobject.textLine(text=x)
        textobject.textLine(text="<br />")
        c.drawText(textobject)
    c.save()
    g.close()
    return 0;

def resumeGeneratorDOC(position, company, file):
    document = Document()
    
    g=open(file+".txt","r")
    
    contents = g.read()
    
    p = document.add_paragraph("Dear Sir/Madam:")
    p = document.add_paragraph("I am excited to apply for your" + " " + position + " position with " + company +". " +contents)
    
    g.close()
    document.save(company + "CoverLetter.docx")
    
    return 0;



