
month_to_firstday = [4, 7, 7, 3, 5, 1, 3, 6, 2, 4, 7, 2]

d, m = [int(x) for x in input().split()]

day_to_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

weekday_index =  (d-1)%7
x = (month_to_firstday[m-1] + weekday_index) % 7
print(day_to_name[x-1])
