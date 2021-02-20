import pandas as pd
import os

filepath = './images'
beforeafter_minutes = 3

datafile = 'data/timeanddate.csv'

solar_data = pd.read_csv(datafile)

def lookupSunrise(date):
    return solar_data[solar_data['Date']==date]['Sunrise'].item()

def lookupNoon(date):
    time = solar_data[solar_data['Date']==date]['SolNoon'].item().split(':')
    return f'{time[0]}:{time[1]}'

def lookupSunset(date):
    return solar_data[solar_data['Date']==date]['Sunset'].item()

def lookupDawn(date):
    return solar_data[solar_data['Date']==date]['CivTwiStart'].item()

def lookupDusk(date):
    return solar_data[solar_data['Date']==date]['CivTwiEnd'].item()

def zeropad(number):
    if (number < 10):
        return f'0{number}'
    else:
        return f'{number}'

def time_tolerance(target_time, tolerance):
    t = target_time.split(':')
    res = [f'{t[0]}{t[1]}']
    i = 1
    while (i < tolerance):
        hour = t[0]
        tplushour = hour
        tminushour = hour

        tplus = int(t[1])+i
        if (tplus > 59):
            tplushour = int(tplushour) + 1
            tplushour = zeropad(tplushour)
            tplus = tplus - 60
        tplus = zeropad(tplus)
        res.append(f'{tplushour}{tplus}')

        tminus = int(t[1])-i
        if (tminus < 0):
            tminushour = int(tminushour) - 1
            tminushour = zeropad(tminushour)
            tminus = 60 + tminus
        tminus = zeropad(tminus)
        res.append(f'{tminushour}{tminus}')

        i = i+1
    return res

def select_images(times, filelist):
    res = []
    # print(times)
    for file in filelist:
        hhmm = file[0:4]
        if hhmm in times:
            res.append(file)
    return res

def calc_times_for_date (date, lookupFn):
    # lookup sunrise/sunset/noon for date
    target_time = lookupFn(date)

    start_end_times = time_tolerance(target_time, beforeafter_minutes)
    # print(date)
    files = os.listdir(f'{filepath}/{date}')
    the_images = select_images(start_end_times, files)
    the_images.sort()
    # print(date, target_time, len(the_images))
    return the_images

all_images = []
datelist = [
    '2020-07-31',
    '2020-08-01',
    '2020-08-02',
    '2020-08-03',
    '2020-08-04',
    '2020-08-05',
    '2020-08-06',
    '2020-08-07',
    '2020-08-08',
    '2020-08-09',
    '2020-08-10',
    '2020-08-11',
    '2020-08-12',
    '2020-08-13',
    '2020-08-14',
    '2020-08-15',
    '2020-08-16',
    '2020-08-17',
    '2020-08-18',
    '2020-08-19',
    '2020-08-20',
    '2020-08-21',
    '2020-08-22',
    '2020-08-23',
    '2020-08-24',
    '2020-08-25',
    '2020-08-26',
    '2020-08-27',
    '2020-08-28',
    '2020-08-29',
    '2020-09-01',
    '2020-09-02',
    '2020-09-03',
    '2020-09-04',
    '2020-09-05',
    '2020-09-06',
    '2020-09-07',
    '2020-09-08',
    '2020-09-09',
    '2020-09-10',
    '2020-09-11',
    '2020-09-12',
    '2020-09-13',
    '2020-09-14',
    '2020-09-15',
    '2020-09-16',
    '2020-09-17',
    '2020-09-18',
    '2020-09-19',
    '2020-09-20',
    '2020-09-21',
    '2020-09-22',
    '2020-09-23',
    '2020-09-24',
    '2020-09-25',
    '2020-09-26',
    '2020-09-27',
    '2020-09-28',
    '2020-09-29',
    '2020-09-30',
    '2020-10-01',
    '2020-10-02',
    '2020-10-03',
    '2020-10-04',
    '2020-10-05',
    '2020-10-06',
    '2020-10-07',
    '2020-10-08',
    '2020-10-09',
    '2020-10-10',
    '2020-10-11',
    '2020-10-12',
    '2020-10-13',
    '2020-10-14',
    '2020-10-15',
    '2020-10-16',
    '2020-10-17',
    '2020-10-18',
    '2020-10-19',
    '2020-10-20',
    '2020-10-21',
    '2020-10-22',
    '2020-10-23',
    '2020-10-24',
    '2020-10-25',
    '2020-10-26',
    '2020-10-27',
    '2020-10-28',
    '2020-10-29',
    '2020-10-30',
    '2020-10-31',
    '2020-11-01',
    '2020-11-02',
    '2020-11-03',
    '2020-11-04',
    '2020-11-05',
    '2020-11-06',
    '2020-11-07',
    '2020-11-08',
    '2020-11-09',
    '2020-11-10',
    '2020-11-11',
    '2020-11-12',
    '2020-11-13',
    '2020-11-14',
    '2020-11-15',
    '2020-11-16',
    '2020-11-17',
    '2020-11-18',
    '2020-11-19',
    '2020-11-20',
    '2020-11-21',
    '2020-11-22',
    '2020-11-23',
    '2020-11-24',
    '2020-11-25',
    '2020-11-26',
    '2020-11-27',
    '2020-11-28',
    '2020-11-29',
    '2020-11-30',
    '2020-12-01',
    '2020-12-02',
    '2020-12-03',
    '2020-12-04',
    '2020-12-05',
    '2020-12-06',
    '2020-12-07',
    '2020-12-08',
    '2020-12-09',
    '2020-12-10',
    '2020-12-11',
    '2020-12-12',
    '2020-12-13',
    '2020-12-14',
    '2020-12-15',
    '2020-12-16',
    '2020-12-17',
    '2020-12-18',
    '2020-12-19',
    '2020-12-20',
    '2020-12-21',
    '2020-12-22',
    '2020-12-23',
    '2020-12-24',
    '2020-12-25',
    '2020-12-26',
    '2020-12-27',
    '2020-12-28',
    '2020-12-29',
    '2020-12-30',
    '2020-12-31',
]
# datelist = [
#     '2020-08-16',
#     '2020-08-17',
#     '2020-10-22',
#     '2020-10-23',
# ]
for date in datelist:
    img_for_date = calc_times_for_date(date, lookupNoon)
    img_for_date = [f"file '{filepath}/{date}/{imgname}'" for imgname in img_for_date]
    all_images = all_images + img_for_date

with open("output.txt", "w") as file: 
    # Writing data to a file 
    file.writelines('\n'.join(all_images)) 
