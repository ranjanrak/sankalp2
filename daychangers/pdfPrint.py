from io import BytesIO
from reportlab.lib.units import mm
from reportlab.lib import colors
import time
import reportlab.pdfgen
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table,\
    TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

class PdfPrint():

	def __init__(self, buffer):
	    self.buffer = buffer
	    self.pageSize = 'A4'
	    self.width, self.height = self.pageSize

	def pageNumber(self, canvas, doc):
		number = canvas.getPageNumber()
		canvas.drawCentredString(100*mm, 15*mm, str(number))

	def report(self,title,stock):
	    doc = SimpleDocTemplate(
	        self.buffer,
	        rightMargin=72,
	        leftMargin=72,
	        topMargin=30,
	        bottomMargin=72,)
	    styles = getSampleStyleSheet()
	    # create document
	    styles.add(ParagraphStyle(name="TableHeader", fontSize=11, alignment=TA_CENTER,fontName="Times-Roman"))
	    styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY, fontName="Times-Roman"))
	    styles.add(ParagraphStyle(name="ParagraphTitle", fontSize=11, alignment=TA_JUSTIFY,fontName="Times-Roman"))
	    data = []
	    data.append(Paragraph(title, styles['Title']))
	    data.append(Spacer(1, 12))
	    table_data = []
	    table_data.append([
            Paragraph('Date', styles['Justify']),
            Paragraph('Symbol', styles['Justify']),
            Paragraph('Price', styles['Justify']),
            Paragraph('Quantity', styles['Justify']),
            Paragraph('Trade Type', styles['Justify']),
            Paragraph('Order no', styles['Justify']),
            Paragraph('Order Type', styles['Justify'])])
	    for wh in stock:
	    	
	    	table_data.append(
                [
                 Paragraph(wh.date.strftime('%Y-%m-%d'), styles['Justify']),
                 format(wh.symbol),
                 format(wh.price),
                 format(wh.quantity),
                 format(wh.trade_type),
                 format(wh.orderno),
                 format(wh.ordertype)])
	    wh_table = Table(table_data, colWidths=None,rowHeights=None)
	    wh_table.hAlign = 'LEFT'
	    wh_table.setStyle(TableStyle(
            [('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),
             ('BOX', (0, 0), (-1, -1), 1.0, colors.black),
             ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
             ('BACKGROUND', (0, 0), (-1, 0), colors.gray)]))
	    data.append(wh_table)
	    data.append(Spacer(1, 48))
	    doc.build(data, onFirstPage=self.pageNumber,
                  onLaterPages=self.pageNumber)
	    pdf = self.buffer.getvalue()
	    self.buffer.close()
	    return pdf
        
        
        
        
        
        
        
         
             	
            

        
        
        
        
        
        
	     
	    	