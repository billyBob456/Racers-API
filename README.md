# Racers-API

## About
Racers API is a game where you have to go around racing with your car, earning money. 
With that money you can buy cars and progress through the game!
You have to combine your coding skills and knowledge to start and finish. 
Making HTTP requests to the API and getting a response is what you need to learn.
You can play Racers API with any language that supports HTTP requests.
Learn more in the [Documentation](https://github.com/billyBob456/Racers-API/#documentation) section

## Documentation
### Python
Checking the status of the server:
``` python
import requests

#Checking the status of the server
statusURL = "https://racersapi.billybob456.repl.co/status"
status = requests.get(statusURL)
status = status.content.decode("utf-8")
print(status)
if status == "Racers API is ready to play!":
	pass
else:
	print("Racers API is unavailable to play at the moment")
	exit()
```
If it outputs "Racers API is ready to play!" then the server is available. Otherwise, you might get an error. If that happens and all you code is correct, it means the server is likely down.
##
Getting a key and starting off: 
``` python
import requests
import json

#Checking the status of the server
statusURL = "https://racersapi.billybob456.repl.co/status"
status = requests.get(statusURL)
status = status.content.decode("utf-8")
print(status)
if status == "Racers API is ready to play!":
	pass
else:
	print("Racers API is unavailable to play at the moment")
	exit()

#Getting an API key
username = "hello"
startURL = "https://racersapi.billybob456.repl.co/start/" + username

x = requests.get(startURL)
x = x.content
x = json.loads(x)
key = x["key"]
print(x["message"])
```
##
Getting your account information:
``` python
import requests
import json

#Checking the status of the server
statusURL = "https://racersapi.billybob456.repl.co/status"
status = requests.get(statusURL)
status = status.content.decode("utf-8")
print(status)
if status == "Racers API is ready to play!":
	pass
else:
	print("Racers API is unavailable to play at the moment")
	exit()

#Getting an API key
username = "hello"
startURL = "https://racersapi.billybob456.repl.co/start/" + username

x = requests.get(startURL)
x = x.content
x = json.loads(x)
key = x["key"]
print(x["message"])

account = requests.get("https://racersapi.billybob456.repl.co/account/" + key).content.decode("utf-8")
print(account)
```
##
Getting your current car:
``` python
import requests
import json
import ast

#Checking the status of the server
statusURL = "https://racersapi.billybob456.repl.co/status"
status = requests.get(statusURL)
status = status.content.decode("utf-8")
print(status)
if status == "Racers API is ready to play!":
	pass
else:
	print("Racers API is unavailable to play at the moment")
	exit()

#Getting an API key
username = "hello"
startURL = "https://racersapi.billybob456.repl.co/start/" + username

x = requests.get(startURL)
x = x.content
x = json.loads(x)
key = x["key"]
print(x["message"])

account = ast.literal_eval(requests.get("https://racersapi.billybob456.repl.co/account/" + key).content.decode("utf-8"))
print(account)

currentCar = account["car"]
print(currentCar)
```
##
Getting the available races:
```python
...
availableRaces = requests.get("https://racersapi.billybob456.repl.co/available-races/" + key).content.decode("utf-8")
print(availableRaces)
```
## 
Selecting the race with best difficult:payout ratio:
``` python
...
#Selecting the best race with difficulty:payout ratio
litEvalList = ast.literal_eval(availableRaces)
length = len(litEvalList)
for race in litEvalList:
	avgSpeed = race["average top speed"]
	if avgSpeed == currentCar["top speed"]:
		raceNum = litEvalList.index(race)
raceKey = json.loads(availableRaces)[raceNum]["key"]
```
## 
Racing the selected race:
``` python
...
#Racing the selected race
raceURL = "https://racersapi.billybob456.repl.co/race/" + key + "/" + raceKey
raceResults = requests.get(raceURL).content.decode('utf-8')
raceKey = ""
raceResults = ast.literal_eval(raceResults)
print(raceResults["message"])
try:
	key = raceResults["key"]
except:
	pass
```
## 
Full script:
``` python
import requests
import json
import ast

#Checking the status of the server
statusURL = "https://racersapi.billybob456.repl.co/status"
status = requests.get(statusURL)
status = status.content.decode("utf-8")
print(status)
if status == "Racers API is ready to play!":
	pass
else:
	print("Racers API is unavailable to play at the moment")
	exit()

#Getting an API key
username = "hello"
startURL = "https://racersapi.billybob456.repl.co/start/" + username

x = requests.get(startURL)
x = x.content
x = json.loads(x)
key = x["key"]
print(x["message"])

#Getting account information
account = ast.literal_eval(requests.get("https://racersapi.billybob456.repl.co/account/" + key).content.decode("utf-8"))
print(account)

#Getting you current car
currentCar = account["car"]
print(currentCar)

#Getting available races
availableRaces = requests.get("https://racersapi.billybob456.repl.co/available-races/" + key).content.decode("utf-8")
print(availableRaces)

#Selecting the best race with difficulty:payout ratio
litEvalList = ast.literal_eval(availableRaces)
length = len(litEvalList)
for race in litEvalList:
	avgSpeed = race["average top speed"]
	if avgSpeed == currentCar["top speed"]:
		raceNum = litEvalList.index(race)
raceKey = json.loads(availableRaces)[raceNum]["key"]

#Racing the selected race
raceURL = "https://racersapi.billybob456.repl.co/race/" + key + "/" + raceKey
raceResults = requests.get(raceURL).content.decode('utf-8')
raceKey = ""
raceResults = ast.literal_eval(raceResults)
print(raceResults["message"])
try:
	key = raceResults["key"]
except:
	pass

```
## 
Well done! You've successfully gone through the basics of Racers API and completed your first race! Below are your next steps.
## 
After getting you new key, you want to save it somewhere! Here's a modified script of the full script that will allow you to continue your game with the new key:
``` python
import requests
import json
import ast

#Checking the status of the server
statusURL = "https://racersapi.billybob456.repl.co/status"
status = requests.get(statusURL)
status = status.content.decode("utf-8")
print(status)
if status == "Racers API is ready to play!":
	pass
else:
	print("Racers API is unavailable to play at the moment")
	exit()

key = "YOUR KEY HERE!" #put your key in there!

#Getting account information
account = ast.literal_eval(requests.get("https://racersapi.billybob456.repl.co/account/" + key).content.decode("utf-8"))
print(account)

#Getting you current car
currentCar = account["car"]
print(currentCar)

#Getting available races
availableRaces = requests.get("https://racersapi.billybob456.repl.co/available-races/" + key).content.decode("utf-8")
print(availableRaces)

#Selecting the best race with difficulty:payout ratio
litEvalList = ast.literal_eval(availableRaces)
length = len(litEvalList)
for race in litEvalList:
	avgSpeed = race["average top speed"]
	if avgSpeed == currentCar["top speed"]:
		raceNum = litEvalList.index(race)
raceKey = json.loads(availableRaces)[raceNum]["key"]

#Racing the selected race
raceURL = "https://racersapi.billybob456.repl.co/race/" + key + "/" + raceKey
raceResults = requests.get(raceURL).content.decode('utf-8')
raceKey = ""
raceResults = ast.literal_eval(raceResults)
key = raceResults["key"]
print(raceResults["message"])
```
## 
More documentation coming out soon including how to buy new cars and mod the game to add your own cars!