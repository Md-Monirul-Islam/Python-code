''''
1. Write a program which uses a nested for loop to
populate a three-dimensional list representing a calendar:
the top-level list should contain a sub-list for each month,
and each month should contain four weeks. Each week should be an empty list.
'''
calender = []
for m in range(12):
    month = []
    for w  in range(4):
        month.append([])
    calender.append(month)
(JANUARY, FEBRUARY, MARCH, APRIL,
 MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER) = range(12)

(WEEK_1, WEEK_2, WEEK_3, WEEK_4) = range(4)
print(calender[JULY][WEEK_2].append("Go on holiday!"))