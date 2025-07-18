from reportlab.lib import pagesizes
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

# Create PDF with A4 page size in landscape
pdf_file = "week_schedule.pdf"
doc = SimpleDocTemplate(
    pdf_file,
    pagesize=pagesizes.landscape(pagesizes.A4),  # Swap width and height for landscape (297mm x 210mm)
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

elements.append(table)
#elements.append(img)
doc.build(elements)
print(f"PDF generated: {pdf_file}")
