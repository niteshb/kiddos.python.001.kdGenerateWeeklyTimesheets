from datetime import date, timedelta
from vykWeeklyTimesheetsData import vykWTAcademicYearStartDayTuple, vykWTWeekNumber, vykWTAcademicYearStartYear

vykWTAcademicYearStartDay = date(vykWTAcademicYearStartDayTuple[0], vykWTAcademicYearStartDayTuple[1], vykWTAcademicYearStartDayTuple[2])

vykWTAcademicYearStartWeekday = vykWTAcademicYearStartDay.weekday() # monday = 0
vykWTAcademicYearStartDayFix = vykWTAcademicYearStartDay - timedelta(vykWTAcademicYearStartWeekday)

vykWTWeekStartDay = vykWTAcademicYearStartDayFix + timedelta((vykWTWeekNumber - 1) * 7)
assert(vykWTWeekStartDay.weekday() == 0) # check it is monday

vykWTDates = [(vykWTWeekStartDay + timedelta(delta)).strftime("%d-%b-%Y") for delta in range(7)]
vykWTWeekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

vykWTAcademicYear = '%d - %d' % (vykWTAcademicYearStartYear, vykWTAcademicYearStartYear + 1)
vykWTHeaderLeft = 'AY ' + vykWTAcademicYear + ': In Out Timesheet'
vykWTHeaderMiddle = 'Week %02d' % vykWTWeekNumber

def printInfo():
    print('vykWTAcademicYearStartDay:', vykWTAcademicYearStartDay.strftime("%d-%b-%Y"))
    print('vykWTAcademicYearStartDayFix:', vykWTAcademicYearStartDayFix.strftime("%d-%b-%Y"))
    print('vykWTWeekStartDay:', vykWTWeekStartDay.strftime("%d-%b-%Y"))
    print('vykWTDates:', vykWTDates)
    print(vykWTHeaderLeft)
    print(vykWTHeaderMiddle)

printInfo()

if __name__ == '__main__':
    printInfo()
