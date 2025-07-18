from reportlab.lib import pagesizes
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate
from reportlab.platypus import Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.platypus import Table, Image
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from functools import partial
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
styleNormal = styles['Normal']

from vykWeeklyTimesheetsTableStyle import vykGetWeeklyTimesheetTableStyle
from vykWeeklyTimesheetsData import vykWTCurrentStaffNames
from vykWeeklyTimesheetsDataProcessed import vykWTDates, vykWTWeekdays, vykWTHeaderLeft, vykWTHeaderMiddle

pdfmetrics.registerFont(TTFont('Noto Serif', 'C:\\Windows\\Fonts\\NotoSerif-VariableFont_wdth,wght.ttf'))
from pprint import pprint

# Create PDF with A4 page size in landscape
# Create PDF with A4 page size in landscape
pdf_file = "week_schedule.pdf"
doc = BaseDocTemplate(
    pdf_file,
    pagesize=pagesizes.landscape(pagesizes.A4),  # Swap width and height for landscape (297mm x 210mm)
    leftMargin=2*mm,  # Reduced to fit table
    rightMargin=2*mm,  # Reduced to fit table
    topMargin=13*mm,
    bottomMargin=4*mm,
    #showBoundary=1,
)
doc.title = 'Attendance Sheet - Staff - AY 2025-26'
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height-3.7*mm, id='normal',
    leftPadding=0,
    topPadding=0,
    rightPadding=0,
    bottomPadding=0,
    #showBoundary=1,
)
def vykOnPageWeeklyTimesheet(canvas, doc, imgLogo):
    canvas.saveState()
    # Header
    x, y = 62*mm, 194*mm
    imgLogoPath = r"D:\GoogleDrive\kiddos.academy.in@gmail.com\Stationery\Logo\images\transparent - shadow - no-internal-glow - 10%.png"
    canvas.drawImage(
        imgLogoPath, 
        x, y,
        height=16*mm,
        preserveAspectRatio=True,
        mask='auto',
    )
    styleNormal.fontSize = 24
    styleNormal.fontName = 'Noto Serif'
    paraHeader = Paragraph(vykWTHeaderLeft, styleNormal)
    w, h = paraHeader.wrap(doc.width, doc.height)
    paraHeader.drawOn(canvas, doc.leftMargin+3*mm, doc.height+9*mm)

    styleNormal.fontSize = 20
    paraHeader = Paragraph(vykWTHeaderMiddle, styleNormal)
    w, h = paraHeader.wrap(doc.width, doc.height)
    paraHeader.drawOn(canvas, doc.leftMargin+170*mm, doc.height+7*mm)
    # Footer
    #
    canvas.restoreState()

# Add image to the top right
image_path = r"D:\GoogleDrive\kiddos.academy.in@gmail.com\Stationery\Logo\images\transparent - shadow - no-internal-glow - 10%.png"
imgLogo = Image(image_path)
imgLogo.vAlign = 'TOP'
imgLogo.hAlign = 'LEFT'
imgLogo._restrictSize(70*mm, 16*mm) # width, hieght

doc.addPageTemplates([
    PageTemplate(id='OneCol', frames=frame, 
        onPage=partial(vykOnPageWeeklyTimesheet, imgLogo=imgLogo),
    ), 
])

# Create table
headers = [
    ["Name"] + [""] * 14, 
    [""] * 15, 
    [""] + ["In", "Out"] * 7
]
headers[0][1::2] = vykWTDates
headers[1][1::2] = vykWTWeekdays
data = headers + [[name] + [""] * (len(vykWTWeekdays) * 2) for name in vykWTCurrentStaffNames]
#pprint(data)
rowsHeaders = 3
# Column widths: 35mm for Name, 18mm for each In/Out column
colWidthsHeader = 35*mm
colWidthsData = 18*mm
# Set row heights to 12mm for all rows (including header)
rowHeightsHeaders = 7*mm
rowHeightsData = 12*mm

rowsData = len(vykWTCurrentStaffNames)
table = Table(data, 
    repeatRows=3,
    rowHeights=[rowHeightsHeaders] * rowsHeaders + [rowHeightsData] * rowsData,  # 3 header rows + name rows
    colWidths=[colWidthsHeader] + [colWidthsData] * (len(vykWTWeekdays) * 2),
)
table.setStyle(vykGetWeeklyTimesheetTableStyle(rowsHeaders, rowsData, 1, 14))

# Build PDF
elements = [table]
doc.build(elements)
print(f"PDF generated: {pdf_file}")
