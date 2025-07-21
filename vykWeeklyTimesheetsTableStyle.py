import reportlab.lib.colors
from reportlab.platypus import TableStyle

def RGB(r, g, b):
    return reportlab.lib.colors.Color(red=r/255.0, green=g/255.0, blue=b/255.0)

class vyk:
    class color:
        pass
    def __init__(self):
        pass

vyk.color.LightBlue_01 = RGB(200, 240, 255)
vyk.color.Blue_01 = RGB(150, 220, 255)
vyk.color.LightMustard_01 = RGB(255, 250, 235)
vyk.color.Mustard_01 = RGB(255, 235, 185)
vyk.color.Gray_01 = RGB(240, 240, 240)
vyk.color.BlueBlack_01 = RGB(0, 0, 120)

# Table style to match the layout
vyk.color.HeaderDark = vyk.color.Blue_01
vyk.color.HeaderLight = vyk.color.LightBlue_01
vyk.color.DataLight1 = vyk.color.LightMustard_01
vyk.color.DataLight2 = reportlab.lib.colors.white
vyk.color.DataDark1 = vyk.color.Mustard_01
vyk.color.DataDark2 = vyk.color.Gray_01

vykWTTableBorderThick = 2
rowsDataPerPage = 14

fontNameName = 'NotoSerifB'
fontNameNames = 'NotoSerifR'
fontNameDates = 'NotoSerifB'
fontNameWeekdays = 'NotoSerifR'
fontNameInOut = 'NotoSerifR'
fontNameData = 'NotoSerifR'

def vykGetWeeklyTimesheetTableStyle(rowsHeaders, rowsData, colsHeaders, colsData):
    cols = colsHeaders + colsData
    rows = rowsHeaders + rowsData
    tableStyle = TableStyle([
        #('BACKGROUND', (1, 0), (14, 2), colors.HeaderLight),  # Header background
        ('BACKGROUND', (3, 0), (4, 0), vyk.color.HeaderDark),  # Header background
        #('BACKGROUND', (0, 1), (-1, 1), colors.lightblue),  # Header background
        ('TEXTCOLOR', (0, 0), (-1, 2), vyk.color.BlueBlack_01),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
        ('ALIGN', (0, 3), (0, -1), 'RIGHT'),  # Center align all cells
        ('FONTNAME', (0, 0), (0, 2), fontNameName),
        ('FONTNAME', (0, 3), (0, -1), fontNameNames),
        ('FONTNAME', (1, 0), (-1, 0), fontNameDates),
        ('FONTNAME', (1, 1), (-1, 1), fontNameWeekdays),
        ('FONTNAME', (1, 2), (-1, 2), fontNameInOut),
        ('FONTNAME', (1, 3), (-1, -1), fontNameData),
        ('FONTSIZE', (0, 0), (-1, 1), 10),  # Font size for headers
        ('FONTSIZE', (0, 2), (-1, 2), 9),  # Font size for headers
        ('FONTSIZE', (0, 3), (-1, -1), 10),  # Font size for data
        ('TOPPADDING', (0, 0), (-1, -1), 3),  # Reduced padding for all cells
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),  # Reduced padding for all cells
        ('LEFTPADDING', (0, 0), (-1, -1), 3),  # Consistent padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),  # Consistent padding
        ('BACKGROUND', (0, 1), (-1, -1), reportlab.lib.colors.white),  # Data background
        ('GRID', (0, 0), (-1, -1), 0.5, reportlab.lib.colors.black),  # Thin grid lines
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical align middle
        ('BOX', (0, 0), (-1, -1), vykWTTableBorderThick, reportlab.lib.colors.black),  # Outer border
        ('BOX', (0, 0), (-1, 2), vykWTTableBorderThick, reportlab.lib.colors.black),  # Outer border
        ('SPAN',(0, 0), (0, 2)), # For "Name" across 3 rows in first column
        ('BACKGROUND', (0, 0), (0, 2), vyk.color.HeaderDark),  # Header background
    ] + [('SPAN',(col, 0), (col + 1, 0)) for col in range(1, cols, 2)
    ] + [('SPAN',(col, 1), (col + 1, 1)) for col in range(1, cols, 2)
    ] + [('BACKGROUND',(col, 0), (col + 1, 2), vyk.color.HeaderDark) for col in range(3, cols, 4)
    ] + [('BACKGROUND',(col, 0), (col + 1, 2), vyk.color.HeaderLight) for col in range(1, cols, 4)
    ] + [('BACKGROUND',(0, row), (0, row), vyk.color.DataDark1) for row in range(3, rows, 2)
    ] + [('BACKGROUND',(col, row), (col + 1, row), vyk.color.DataLight1) for row in range(3, rows, 2) for col in range(1, cols, 4)
    ] + [('BACKGROUND',(col, row), (col + 1, row), vyk.color.DataDark1) for row in range(3, rows, 2) for col in range(3, cols, 4)
    ] + [('BACKGROUND',(col, row), (col + 1, row), vyk.color.DataLight2) for row in range(4, rows, 2) for col in range(1, cols, 4)
    ] + [('BACKGROUND',(col, row), (col + 1, row), vyk.color.DataDark2) for row in range(4, rows, 2) for col in range(3, cols, 4)
    ] + [('BACKGROUND',(0, row), (0, row), vyk.color.DataDark2) for row in range(4, rows, 2)
    ] + [('BOX',(col, 0), (col+1, -1), vykWTTableBorderThick, reportlab.lib.colors.black) for col in range(1, cols, 4)
    ] + [('LINEBELOW',(0, row), (-1, row), vykWTTableBorderThick, reportlab.lib.colors.black) for row in range(rowsHeaders+rowsDataPerPage-1, rows, rowsDataPerPage)
    ]
    )
    return tableStyle
