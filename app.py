#!/usr/bin/env python3

import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://official-joke-api.appspot.com/random_joke')
    if r.status_code == 200:
        d = r.json()
        print(d['setup'])
        print(d['punchline'])
    else:
        print("Error fetching joke!", file=sys.stderr)
        sys.exit(1)
