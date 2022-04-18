from django.shortcuts import render
from datetime import date
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar

def index(request,year,choice):
    year = int(year)
    choice = int(choice)
    if year < 1900 or year > 2099:
        year = date.today().year
    title = "Calendar - %s" %(year)
    cal1 = HTMLCalendar().formatmonth(year, 1)
    cal2 = HTMLCalendar().formatmonth(year, 2)
    cal3 = HTMLCalendar().formatmonth(year, 3)
    cal4 = HTMLCalendar().formatmonth(year, 4)
    cal5 = HTMLCalendar().formatmonth(year, 5)
    cal6 = HTMLCalendar().formatmonth(year, 6)
    cal7 = HTMLCalendar().formatmonth(year, 7)
    cal8 = HTMLCalendar().formatmonth(year, 8)
    cal9 = HTMLCalendar().formatmonth(year, 9)
    cal10 = HTMLCalendar().formatmonth(year, 10)
    cal11 = HTMLCalendar().formatmonth(year, 11)
    cal12 = HTMLCalendar().formatmonth(year, 12)
    if choice == 1:
        return render(request, 'employee.html',)
    else:
        return HttpResponse("<h1>%s</h1><p>%s</p><p>%s</p><p>%s</p><p>%s</p><p>%s</p><p>%s</p><p>%s</p><p>%s</p><p>%s</p><p>%s</p><p>%s</p><p>%s</p>" % (title, cal1,cal2,cal3,cal4,cal5,cal6,cal7,cal8,cal9,cal10,cal11,cal12))