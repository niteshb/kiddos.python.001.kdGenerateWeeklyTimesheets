from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import mm

# Data for the table
names = [
    "Swati B",
    "Rupam Priya",
    "Ramya S",
    "Sakshi S",
    "Mansi R",
    "Tulika N",
    "Poonam",
    "Mayshar"
]

# Column headers for July 21-27, 2025
days = [
    "21 Jul 2025\nMonday", "22 Jul 2025\nTuesday", "23 Jul 2025\nWednesday",
    "24 Jul 2025\nThursday", "25 Jul 2025\nFriday", "26 Jul 2025\nSaturday",
    "27 Jul 2025\nSunday"
]
headers = ["Name"] + [day + "\nIn" for day in days] + [day + "\nOut" for day in days]

# Create table data: first column is names, rest are empty
data = [[name] + [""] * (len(days) * 2) for name in names]
data.insert(0, headers)  # Insert headers as the first row

# Create PDF with A4 page size
pdf_file = "week_schedule.pdf"
doc = SimpleDocTemplate(
    pdf_file,
    pagesize=(A4[1], A4[0]),  # Swap width and height for landscape (297mm x 210mm)
    leftMargin=10*mm,
    rightMargin=10*mm,
    topMargin=10*mm,
    bottomMargin=10*mm
)
# Create table
table = Table(data)

# Table style to match the layout
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for headers
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Regular font for data
    ('FONTSIZE', (0, 0), (-1, 0), 8),  # Smaller font size for headers
    ('FONTSIZE', (0, 1), (-1, -1), 8),  # Same font size for data
    ('LEADING', (0, 0), (-1, -1), 10),  # Line spacing
    ('BOTTOMPADDING', (0, 0), (-1, 0), 6),  # Padding for header
    ('TOPPADDING', (0, 0), (-1, 0), 6),  # Padding for header
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Data background
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Thin grid lines
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical align middle
    ('BOX', (0, 0), (-1, -1), 1, colors.black),  # Outer border
]))

# Column widths as specified: 35mm for Name, 18mm for each In/Out column
col_widths = [35*mm] + [18*mm] * (len(days) * 2)  # 15 columns total
table._argW = col_widths

# Build PDF
elements = [table]
doc.build(elements)

print(f"PDF generated: {pdf_file}")