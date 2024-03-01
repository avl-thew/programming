#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}
# TODO здесь заполнение словаря

# MoscowLondon = ((sites['Moscow'][0] - sites['London'][0]) **2 + (sites['Moscow'][1] - sites['London'][1]) **2 ) ** 0.5
# MoscowParis =  ((sites['Moscow'][0] - sites['Paris'][0]) **2 + (sites['Moscow'][1] - sites['Paris'][1]) **2 ) ** 0.5
# LondonParis = ((sites['London'][0] - sites['Paris'][0]) **2 + (sites['London'][1] - sites['Paris'][1]) **2 ) ** 0.5
# distances['Moscow_and_London'] = round(MoscowLondon, 1)
# distances['Moscow_and_Paris'] = round(MoscowParis, 1)
# distances['London_and_Paris'] = round(LondonParis, 1)
# print(distances)

def distance(a: tuple, b: tuple) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    
    




