days_of_week = {1: "Saturday", 2: "Sunday", 3: "Monday", 4: "Tuesday", 5: "Wednesday", 6: "Thursday", 7: "Friday", 8: "Saturday", 9: "Sunday", 10: "Monday", 11: "Tuesday", 12: "Wednesday", 13: "Thursday", 14: "Friday"}
months = {1 : 'January' , 2 : 'February' , 3 : 'March' , 4 : 'April' , 5 : 'May' , 6 : 'June' , 7 : 'July' , 8 : 'August' , 9 : 'September' , 10 : 'October' , 11 : 'November' , 12 : 'December'}
list1 = ['st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th']

year, month, day = input().split("/")
year = int(year)
month = int(month)
day = int(day)
dayy = input()
number = int(input())

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f'{year} is a Leap Year')
else:
    print(f'{year} is NOT a Leap Year')


print(f'{month}{list1[month - 1]} month ({months[month]})')


f = number % 7
for i in days_of_week:
    if days_of_week[i] == dayy:
        s = i
        break
s += f
print(f'{number} days later is {days_of_week[s]}')