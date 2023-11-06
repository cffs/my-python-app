#!/usr/bin/env python3

import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://punapi.rest/api/pun')
    if r.status_code == 200:
        d = r.json()
        print(d['pun'])
    else:
        print("Error fetching pun from PunAPI!", file=sys.stderr)
        sys.exit(1)
