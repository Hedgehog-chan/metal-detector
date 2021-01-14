import datetime
URL = 'https://alkom.spb.ru/tseny/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/87.0.4280.66 Safari/537.36',
           'accept': '*/*'
           }
now = datetime.datetime.now()
yesterday = (now - datetime.timedelta(days=1))
pre_file_name = 'price_' + yesterday.strftime("%d_%m_%Y") + '.csv'
file_name = 'price_' + now.strftime("%d_%m_%Y") + '.csv'
columns_date = [yesterday.strftime("%d_%m_%Y"), '---->', now.strftime("%d_%m_%Y")]
columns_names = ['Лом', 'До 100 кг', '100-1000 кг', 'От 1000 кг', 'На карту физ. лицам', 'Безнал для юр. лиц']
columns_names_dif = columns_names[:-2] + ['Новые:'] + columns_names[1:-2]