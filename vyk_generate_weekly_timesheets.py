from reportlab.lib import pagesizes
<<<<<<<<< Temporary merge branch 1
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from vyk_weekly_timesheets_tableStyle import tableStyle

pdfmetrics.registerFont(TTFont('Noto Serif', 'C:\\Windows\\Fonts\\NotoSerif-VariableFont_wdth,wght.ttf'))
from pprint import pprint

# Data for the table
names = [
    "Swati B",
    "Rupam Priya",
    "Ramya S",
    "Sakshi S",
    "Mansi R",
    "Tulika N",
    "",
    "Poonam",
    "Mayshar",
    "Shabnam",
    "Harkumari",
    "Lalita",
    "",
    "",
]

# Verify 14 name rows
assert len(names) == 14, f"Expected 14 name rows, got {len(names)}"

# Column headers for July 21-27, 2025
dates = ["21 Jul 2025", "22 Jul 2025", "23 Jul 2025", "24 Jul 2025", "25 Jul 2025", "26 Jul 2025", "27 Jul 2025"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
headers1 = ["Name"] + [""] * 14
headers1[1::2] = dates
#[date, "" for date in dates]
headers2 = [""] * 15
headers2[1::2] = days
#days + ["" for date in dates]
headers3 = [""] + ["In", "Out"] * 7

# Create table data: first column is names, rest are empty
data = [[name] + [""] * (len(days) * 2) for name in names]
data.insert(0, headers3)  # Insert headers as the first row
data.insert(0, headers2)  # Insert headers as the first row
data.insert(0, headers1)  # Insert headers as the first row

=========
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate
from reportlab.platypus import Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.platypus import Table, Image
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from functools import partial
from vykWeeklyTimesheetsTableStyle import vykGetWeeklyTimesheetTableStyle
from vykWeeklyTimesheetsData import vykWTCurrentStaffNames, vykWTDates, vykWTDays

pdfmetrics.registerFont(TTFont('Noto Serif', 'C:\\Windows\\Fonts\\NotoSerif-VariableFont_wdth,wght.ttf'))
from pprint import pprint

# Create PDF with A4 page size in landscape
# Create PDF with A4 page size in landscape
pdf_file = "week_schedule.pdf"
doc = BaseDocTemplate(
    pdf_file,
    pagesize=pagesizes.landscape(pagesizes.A4),  # Swap width and height for landscape (297mm x 210mm)
<<<<<<<<< Temporary merge branch 1
    leftMargin=8*mm,  # Reduced to fit table
    rightMargin=8*mm,  # Reduced to fit table
    topMargin=8*mm,
    bottomMargin=8*mm,
    showBoundary=1,
)
doc.title = 'Attendance Sheet - Staff - AY 2025-26'

# Create table
#pprint(data)
table = Table(data)


table.setStyle(tableStyle)

# Column widths: 35mm for Name, 18mm for each In/Out column
col_width_first = 35*mm
col_width_rest = 18*mm
table._argW = [col_width_first] + [col_width_rest] * (len(days) * 2)  # 15 columns total

# Set row heights to 12mm for all rows (including header)
row_height_headers = 7*mm
row_height_data = 12*mm
table._argH = [row_height_headers] * 3 + [row_height_data] * 14  # 17 rows (3 header rows + 14 name rows)

# Build PDF
elements = []


# Add image to the top right
image_path = r"D:\GoogleDrive\kiddos.academy.in@gmail.com\Stationery\Logo\images\transparent - shadow - no-internal-glow - 10%.png"  # Replace with your image file path
img = Image(image_path)
img.vAlign = 'TOP'
#img.drawHeight = 20
#img.drawWidth = 150
img.hAlign = 'RIGHT'
img._restrictSize(70*mm, 16*mm) # width, hieght

=========
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
headers[1][1::2] = vykWTDays
data = headers + [[name] + [""] * (len(vykWTDays) * 2) for name in vykWTCurrentStaffNames]
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
    colWidths=[colWidthsHeader] + [colWidthsData] * (len(vykWTDays) * 2),
)
table.setStyle(vykGetWeeklyTimesheetTableStyle(rowsHeaders, rowsData, 1, 14))

# Build PDF
elements = [table]
doc.build(elements)
print(f"PDF generated: {pdf_file}")

