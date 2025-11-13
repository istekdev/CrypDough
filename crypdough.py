from termcolor import colored
import requests
import json
import time
import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

with open("config.json", "r") as r:
  config = json.load(r)

delay = config["delay"]
currency = config["currency"]
endpoint = config["endpoint"]
cryptocurrencies = config["coins"]
currencyParam = "&vs_currencies="

def test():
  try:
    testConnection = requests.get(endpoint)
    testConnection.raise_for_status()
    testJson = testConnection.json()
    return bool(testJson)
  except Exception:
    return False

def start():
  print(colored(f"Created By: {config['socials']['developer']}\nGithub: {config['socials']['github']}\n\nAPI Call Delay: {config['delay']} Seconds\nCurrency: {config['currency']}\nCryptocurrencies Listed: {config['coins']}\nAPI: {config['endpoint']}\n\nTo Change Specific Attributes, Access The Local config.json\n\nThe Program Will Start in 5 Seconds.", "white", attrs=["bold"]))
  time.sleep(5)
  clear()
  while True:
    for crypto in cryptocurrencies:
      completeAPI = f"{endpoint}{crypto}{currencyParam}{currency}"
      print(colored(f"{crypto.title()}: {completeAPI}\n", "white", attrs=["bold"]))
      time.sleep(delay)

if test() == True:
  start()
else:
  print(colored("Error - API Is Dysfunctional\n\nClosing In 5 Seconds", "red", attrs=["bold"]))
  time.sleep(5)
  return
  

