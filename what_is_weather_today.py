import requests
import calendar


# API endpoint, free by open-meteo.com, location: Sofia, take only temperatura in ^C, precipitation and wind speed
url = 'https://api.open-meteo.com/v1/forecast?latitude=42.70&longitude=23.32&hourly=temperature_2m,precipitation,windspeed_10m'

# Make request to the API
response = requests.get(url)

# Get the response data as a python object
data = response.json()

# Get date for today and this return me YY/MM/DD/hh:mm
def current_day():
    return data['hourly']['time'][0]


# Get name day of week
def day_of_week(year, month, day):
    day_of_week_number = calendar.weekday(year, month, day)
    name_day = calendar.day_name[day_of_week_number]
    return name_day


# Return day, day of week and year (Monday, 30.01.2023)
def print_current_day(day, day_week, month, year):
    return f'{day_week}, {day}.{month}.{year}y.'


today = current_day()[:10]

# Slicing current day for get year 2023, month and day
year = int(today[:4])
month = today[5:7]      # This is str, for 01 format
day = int(today[8:10])


current_week_day = day_of_week(year, int(month), day)
print(print_current_day(day, current_week_day,month, year))


# This function calculates average_values
def average_values(data):
    sum_all_values = 0
    count = 0
    for rain in data:
        sum_all_values += rain
        count += 1
    avarege = sum_all_values / count
    return avarege


avarege_temperature = average_values(data['hourly']['temperature_2m'][0: 25])
avarege_precipitation = average_values(data['hourly']['precipitation'][0: 25])
avarege_wind_speed = average_values(data['hourly']['windspeed_10m'][0: 25])

print(f'Avarege temperature today is: {avarege_temperature:.2f}')
print(f'Avarege precipitation today is: {avarege_precipitation:.2f}')
print(f'Avarege wind speed today is: {avarege_wind_speed:.2f}km/h')
