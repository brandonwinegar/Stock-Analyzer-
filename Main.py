#!/usr/bin/python3
from SimpleGui import *
import argparse
import daemon

func = 'function=TIME_SERIES_DAILY'
symbol = 'symbol=MSFT'
example_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo'
base_url = 'https://www.alphavantage.co/query?'
# response = requests.get("http://api.open-notify.org/iss-now.json")
# Alpha Vantage key: XW4JRNJTHUYZ8HJC

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--daemon", action="store_true")
    return parser.parse_args()

def main():
    # Gets a response form the requested URL, stores in Response Object
    response = requests.get(example_url)
    # Loads Response Object into a dict
    response_json = json.loads(response.text)
    # Loads the dict into a string
    response_string = json.dumps(response_json)
    # Writes the string to a json file. This file will store information between executions of the program
    with open('example.json', 'w') as outfile:
        outfile.write(response_string)
    # Reads the JSON into the program as a dict
    with open('example.json') as f:
        json_foo = json.load(f)
    print(json_foo)


if __name__ == "__main__":
    # main demonstrates some json stuff
    # main()
    args = get_args()
    if args.daemon:
        print("daemonized")
        with daemon.DaemonContext():
            SimpleGui()
    else:
        SimpleGui()


