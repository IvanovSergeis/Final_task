# -*- coding: utf-8 -*-
"""PythonUrban_final_task.ipynb

# Финальное задание.
"""

# TODO собрать установку всех необходимых модулей в одном месте

!pip install geopandas

!pip install mapclassify  # необходимо для визуализации

!pip install osmnx  # устанавливаем модуль osmnx

!pip install keplergl


# TODO собрать импорты всех модулей в одном месте

import geopandas as gpd

import osmnx as ox

import requests

import json

from keplergl import KeplerGl


TILES = "CartoDB positron"  # Название подложки для карт

# TODO указать любой район Санкт-Петербург из OSM https://wiki.openstreetmap.org/wiki/RU:%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3/%D0%A0%D0%B0%D0%B9%D0%BE%D0%BD%D1%8B
TERRITORY_NAME = 'Петроградский район, Санкт-Петербург'  # название территории для которой будут строиться слои



KGIOP_FILE_URL = "https://raw.githubusercontent.com/aeksei/PythonUrbanITMO2023/main/geojson_layers/kgiop_objects.geojson"  # ссылка на слой с объектами культурного наследия

STREETS_FILE_URL = "https://raw.githubusercontent.com/aeksei/PythonUrbanITMO2023/main/geojson_layers/streets.geojson"  # ссылка на слой с улицами


district = ox.geocode_to_gdf(TERRITORY_NAME)

district.explore(tiles=TILES)


district = ox.geocode_to_gdf(TERRITORY_NAME)

gdf = gpd.read_file(KGIOP_FILE_URL, mask=district)

gdf.explore(tiles=TILES)

gdf.crs

gdf



district = ox.geocode_to_gdf(TERRITORY_NAME)

gdf = gpd.read_file(STREETS_FILE_URL, mask=district)

gdf.explore(tiles=TILES)

gdf.crs

gdf



osm_id = "R1114905"

territory = ox.geocode_to_gdf([osm_id], by_osmid=True)

territory


gdf.to_crs(4326).to_file('streets.geojson', driver='GeoJSON')

gdf.to_crs(4326).to_file('kgiop_objects.geojson', driver='GeoJSON')
