import json
import pickle


def Parking_Bay_Reader(filename):
    finalDataPolygon = {'features': []}

    """This opens the file finds all the polygons and multipolygons in the json file
    then sorts them into lists"""
    with open(filename, 'r') as datafile:
        data = json.loads(datafile.read())
        for i in data['features']:
            if i['geometry']['type'] != 'MultiPolygon':
                #Gets the avg for each polygon line
                for line in i['geometry']['coordinates']:
                    lat = 0
                    long = 0
                    for value in line:
                        lat = lat + value[0]
                        long = long + value[1]
                    lat -= line[0][0]
                    long -= line[0][1]
                    avgLat = lat / (len(line)-1)
                    avgLong = long / (len(line)-1)

                    finalDataPolygon['features'].append({'poly': i['geometry']['coordinates'][0], 'avgLat': avgLong,
                                                         'avgLng': avgLat})
            else:
                for line in i['geometry']['coordinates'][0]:
                    lat = 0
                    long = 0
                    for value in line:
                        lat = lat + value[0]
                        long = long + value[1]
                    lat -= line[0][0]
                    long -= line[0][1]
                    avgLat = lat / len(line) - 1
                    avgLong = long / len(line) - 1

                    finalDataPolygon['features'].append({'poly': i['geometry']['coordinates'], 'avgLat': avgLat,
                                                         'avgLng': avgLong})

    with open('ParkingPolygonData', 'w') as fdatafile:
        json.dump(finalDataPolygon, fdatafile)

Parking_Bay_Reader('Parking_Bays.json')
