#!/usr/bin/env python

import sys
import json
import argparse
import requests

def get_stats(url):
    response = requests.get('https://accountws.arin.net/public/rest/waitingList')
    response.raise_for_status()

    waitlist = response.json()
    first_waiting = waitlist[0]['waitListActionDate']

    min_24s = 0
    max_24s = 0
    for lir in waitlist:
        min_24s += 2 ** (24 - lir['minimumCidr'])
        max_24s += 2 ** (24 - lir['maximumCidr'])

    return json.dumps({
        'first_waiting_since': first_waiting,
        'min_24s': min_24s,
        'max_24s': max_24s,
        'length': len(waitlist)
    })

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--url', default="https://accountws.arin.net/public/rest/waitingList")

  args = parser.parse_args()
  print(get_stats(args.url))
