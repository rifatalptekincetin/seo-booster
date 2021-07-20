import requests
import time
import os
from stem import Signal
from stem.control import Controller

def renew_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="alptekin01")
        controller.signal(Signal.NEWNYM)

def start_tor():
    os.system("start Tor/tor.exe --defaults-torrc Data/Tor/torrc")

if __name__ == "__main__":
    start_tor()
