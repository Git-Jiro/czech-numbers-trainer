#!/usr/bin/env python3
# czech numbers trainer

import random, sys

def lookup_hundrets(hundrets):
    switcher = {
        0: '',
        1: 'sto',
        2: 'dvě stě',
        3: 'tři sta',
        4: 'čtyři sta',
        5: 'pět set',
        6: 'šest set',
        7: 'sedm set',
        8: 'osm set',
        9: 'devět set',
    }
    return switcher[hundrets]

def lookup_tens(tens):
    switcher = {
        0: '',
        1: 'deset',
        2: 'dvacet',
        3: 'třicet',
        4: 'čtyřicet',
        5: 'padesát',
        6: 'šedesát',
        7: 'sedmdesát',
        8: 'osmdesát',
        9: 'devadesát',
    }
    return switcher[tens]

def lookup_singles(singles):
    switcher = {
        0: '',
        1: 'jedna',
        2: 'dva',
        3: 'tři',
        4: 'čtyři',
        5: 'pět',
        6: 'šest',
        7: 'sedm',
        8: 'osm',
        9: 'devět',
    }
    return switcher[singles]

def lookup_11_to_19(singles):
    switcher = {
        1: 'jedenáct',
        2: 'dvanáct',
        3: 'třináct',
        4: 'čtřnáct',
        5: 'padnáct',
        6: 'šestnáct',
        7: 'sedmnáct',
        8: 'osmnáct',
        9: 'devatenáct',
    }
    return switcher[singles]

def split_into_components(num):
    hundrets = num / 100 
    hundrets = int(hundrets)
    num -= hundrets * 100

    tens = num / 10
    tens = int(tens)
    num -= tens * 10

    singles = num
    num -= singles
    return (int(hundrets), int(tens), int(singles))

def convert_to_CZ(num):
    (hundrets, tens, singles) = split_into_components(num)
    result = ''
    result += lookup_hundrets(hundrets) + ' '
    if tens == 1 and singles > 0:
        result += lookup_11_to_19(singles)
    else:
        result += lookup_tens(tens) + ' '
        result += lookup_singles(singles)
    return result

def main():
    # show random number and wait for key
    while(1):
        num = random.randrange(1000)
        print (num)
        sys.stdin.readline()
        converted = convert_to_CZ(num)
        print (converted)
        print ('')

main()
