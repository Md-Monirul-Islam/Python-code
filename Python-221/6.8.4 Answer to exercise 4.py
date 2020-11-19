''''
Create a tuple of month names and a tuple of the number of days in each month
(assume that February has 28 days). Usingasingleforloop,
constructadictionarywhichhasthemonthnamesaskeysandthecorresponding day numbers as values.
'''

months = ("January", "February", "March", "April", "May", "June",
"July", "August", "September", "October",
"November", "December")
days = list(range(1,28))
num_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month_dict = {}

for month, days in zip(months, days):
    month_dict[month] = days
print(days)