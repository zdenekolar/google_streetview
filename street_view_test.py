# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 23:14:37 2017

@author: Zdenek Kolar
"""
from urllib.request import urlretrieve
from urllib.parse import quote
import os
from googlemaps import Client
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

api_key = 'AIzaSyCCoSkeF2DYZWE0desgmxsYjg_ZagXMcUo'
gmaps = Client(key=api_key)


def get_coordinates(address):
    '''
    Return the coordinates of an address.
    :param address: string address
    :return: tuple coordinates (latitude, longitude)
    '''
    geocode_result = gmaps.geocode(address)
    lng = geocode_result[0]['geometry']['location']['lng']
    lat = geocode_result[0]['geometry']['location']['lat']
    print(address)
    print(lat, lng)
    return (lat,lng)


def get_views(add, saveloc):
    '''
    Saves views at the selected location, direction given by headings
    :param add:
    :param saveloc:
    :return:
    '''
    headings = range(0, 360, 30)
    pitch = 0
    for heading in headings:
        base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&location="
        key = "&key=" + "AIzaSyDoN7qwJr57RMRzMgLPsTR85Fzve8HjDLA"
        head = "&heading={}".format(heading)
        url = base + quote(add) + head + key
        fi = add + str(heading) + ".jpg"
        urlretrieve(url, os.path.join(saveloc, fi))


def plot_street(x, y):
    '''
    Plot the street coordinates in a graph
    :param x: latitude
    :param y: longitude
    :return:
    '''
    # data['lat'].plot()
    plt.figure()
    plt.scatter(x, y)
    plt.show()



if __name__ == '__main__':

    myloc = r""
    coords_lat = []
    coords_lon = []

    for i in range(1, 1000, 1):
    # Run through the numbers in the street from 1 to 1000, break if too many duplicite
    # points (Google returns duplicite points if it can't find the exact address.
        a = '{} Queens Road Central, Hong Kong'.format(i)
        get_views(add=a, saveloc=myloc)
        coord = get_coordinates(a)
        # Record coordinates if points not in the list
        if coord[0] not in coords_lat and coord[1] not in coords_lon:
            coords_lat.append(coord[0])
            coords_lon.append(coord[1])
            print(len(coords_lat))
        # If too many duplicate points, break
        if i > len(coords_lat) * 1.25 and i > 50:
            break

    # print(coords)
    # plot_street(coords_lat, coords_lon)

    # print(coords[-1])
    # print(len(coords))

