# -*- coding: utf-8 -*- 
import json
import urllib

GEOCODE_BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json'


def geocode(address, sensor = 'false', **geo_args):
    geo_args.update({
        'address': address,
        'sensor': sensor
    })

    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
    result = json.load(urllib.urlopen(url))
    
    print address
    # print url
    # print json.dumps(result)
    loc = ''
    if result['results']:
        try:
            loc = result['results'][0]['geometry']["location"]
        except KeyError, e:
            pass
    print loc
    # print json.dumps([s['formatted_address'] for s in result['results']], indent=2)


def readdata():
    sent_file = open("./data/data.csv")
    i = 0
    for line in sent_file:
        i += 1
        if i % 6 != 2:
            continue
        cells = line.split(',')
        
        address = ('ایران، %s، %s') % (cells[0], cells[1])        
        if not cells[2].startswith('بخش حومه') and not cells[2].startswith('بخش مركزي'):
            address += '،' + cells[2][6:]
        geocode(address)
        if i==500:
            break

if __name__ == '__main__':
    readdata()
