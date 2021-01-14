# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
from config import *


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # column 1
    items_col_1 = soup.find_all('td', class_='column-1')
    lst_c1 = []
    for item in items_col_1:
        if item.find('a'):
            lst_c1.append(item.find('a').get_text(strip=True))
        else:
            lst_c1.append(item.get_text(strip=True))
    # column 2, 3
    items_col_2 = soup.find_all('td', class_='column-2')
    items_col_3 = soup.find_all('td', class_='column-3')
    items_col_4 = soup.find_all('td', class_='column-4')
    items_col_5 = soup.find_all('td', class_='column-5')
    items_col_6 = soup.find_all('td', class_='column-6')
    lst_c2, lst_c3, lst_c4,lst_c5, lst_c6 = [], [], [], [], []
    for item in items_col_2:
        lst_c2.append(item.get_text(strip=True))
    for item in items_col_3:
        lst_c3.append(item.get_text(strip=True))
    for item in items_col_4:
        lst_c4.append(item.get_text(strip=True))
    for item in items_col_5:
        lst_c5.append(item.get_text(strip=True))
    for item in items_col_6:
        lst_c6.append(item.get_text(strip=True))
    # column
    lst_temp = [lst_c1, lst_c2, lst_c3, lst_c4, lst_c5, lst_c6]
    lst_all = []
    for i in range(len(lst_c1)):
        temp = []
        for j in range(6):
            temp.append(lst_temp[j][i])
        lst_all.append(temp)
    return lst_all


def save_file(lst, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(columns_names)
        for i in range(len(lst)):
            writer.writerow(lst[i])


def find_dif(path1, path2):
    change_bool = False
    with open(path1, 'r', newline='') as f1, open(path2, 'r', newline='') as f2, open('dif.csv', 'w', newline='') as f_dif:
        writer = csv.writer(f_dif, delimiter=';')
        writer.writerow(columns_date)
        writer.writerow(columns_names_dif)
        for line_pre, line_new in zip(f1, f2):
            l_pre = line_pre.strip().split(';')
            l_new = line_new.strip().split(';')
            sign = ''
            if l_new != l_pre:
                change_bool = True
                if int(l_new[1]) > int(l_pre[1]):
                    sign = '+'
                elif int(l_new[1]) > int(l_pre[1]):
                    sign = '-'
                writer.writerow(l_pre[:-2] + [sign] + l_new[1:-2])
    return change_bool


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        lst = get_content(html.text)
        save_file(lst, file_name)
        find_dif(pre_file_name, file_name)
    else:
        print('Error')
