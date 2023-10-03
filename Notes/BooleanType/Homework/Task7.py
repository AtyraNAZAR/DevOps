
minute = int(input("Enter the minute to convert: "))

minute_day = 24 * 60
minute_year = 365 * minute_day

years = minute_year // 365 // 12
days = years //60

print( minute_year,  years, days)