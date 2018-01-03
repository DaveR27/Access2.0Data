import json

count = 0

def pramRampFileMaker(filename):
    finalPramRamps = {'features': []}

    with open(filename) as datafile:
        data = json.loads(datafile.read())
        for i in data['features']:
            finalPramRamps['features'].append({'lat': i['geometry']['coordinates'][1],
                                               'lng': i['geometry']['coordinates'][0]})

    with open('RampData.json', 'w') as fdatafile:
        json.dump(finalPramRamps, fdatafile)


pramRampFileMaker('Pram_Ramp.json')
