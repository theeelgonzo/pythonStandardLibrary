# Calendar Module
from datetime import datetime, timedelta
import calendar

now = datetime.now()

testDate = now + timedelta(days = 2)
myFirstLinkedInCourse = now - timedelta(weeks = 3)
print(testDate.date())
print(myFirstLinkedInCourse.date())

cal = calendar.month(2001, 10)
print(cal)