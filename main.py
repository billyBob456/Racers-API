from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
import base64
import ast
import json
import random

app = Flask(__name__,static_url_path='')
CORS(app)

startCoins = 100000
allCars = [
	{"name": "Honda Civic", "top speed": 145},
	{"name":"Toyota Corolla", "top speed":180},
	{"name":"Hyundai Accent", "top speed":209},
	{"name":"Kia Optima", "top speed":152},
	{"name":"Chevrolet Camaro", "top speed":319}, 
	{"name":"GMC Sierra", "top speed":174},
	{"name":"Acura ILX", "top speed":209},
	{"name":"Tesla Model X", "top speed":250},
	{"name":"Chevrolet Corvette", "top speed":312},
	{"name":"Porsche 911", "top speed":330},
	{"name":"Subaru Forester", "top speed":188},
	{"name":"Ford Mustand Mach-E", "top speed":258},
	{"name":"Mazda CX-9", "top speed":217}]
for car in allCars:
	car["price"] = car["top speed"] * 1000
startCar = allCars[0]

def encode(msg):
	result = msg.encode("ascii")
	result = base64.b64encode(result)
	result = result.decode("ascii")
	return result

def decode(msg):
	result = msg.encode("ascii")
	result = base64.b64decode(result)
	result = result.decode("ascii")
	return result

allCarsKeys = allCars.copy()
for item in allCarsKeys:
	item["key"] = encode(str(item))

@app.route('/scripts/<path:path>')
def send_scripts(path):
	return send_from_directory('templates/', path)

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/status/")
def status():
	return "Racers API is ready to play!"

@app.route("/start/<username>/")
def start(username):
	key = {"username":username, "car":startCar, "coins":startCoins}
	key = encode(str(key))
	return {"message":"Welcome to Racers.API! Have fun!",
	"key": key}

@app.route("/account/<key>/")
def account(key):
	try:
		return decode(key)
	except:
		return 'Oops! An error occurred! Make sure you have the right key!'

@app.route("/available-races/<key>/")
def availableRaces(key):
	key = decode(key)
	key = ast.literal_eval(key)
	car = key['car']
	topSpeed = car['top speed']
	races = []
	for i in range(20):
		x = i - 10
		bonus = topSpeed / 100000
		bonus = bonus + 1
		races.append({"average top speed":topSpeed + x, "payout": ((i+1) * 1000) + random.choice(list(range(1,1000))) * bonus})
		races[-1]["key"] = encode(json.dumps(races[-1]))
	random.shuffle(races)
	races = json.dumps(races)
	return races

@app.route('/race/<key>/<raceKey>/')
def race(key, raceKey):
	key = decode(key)
	key = ast.literal_eval(key)
	coins = key["coins"]
	raceKey = decode(raceKey)
	raceKey = ast.literal_eval(raceKey)
	payout = raceKey["payout"]
	avgSpeed = raceKey["average top speed"]
	car = key["car"]
	carSpeed = car["top speed"]
	diff = float(carSpeed) - float(avgSpeed)
	if diff >= 0: positive = True
	else: positive = False
	if positive == True:
		if diff == 0: chances = 50
		elif diff <= 10: chances = 70
		elif diff <= 20: chances = 90
		elif diff >= 21: chances = 100
	else:
		if diff >= -10: chances = 40
		elif diff >= -20: chances = 20
		elif diff <= -21: chances = 0

	if random.choice(range(1,101)) <= chances: 
		key["coins"] = int(coins) + int(payout)
		return {"message":"Well done! You won your race as well as $" + str(payout) + "!", "key":str(encode(json.dumps(key)))}
	else:
		key["coins"] = int(coins) - int(payout)
		if key["coins"] < 0:
			return {"message":'Oh no! You lost the race! You have lost $' + str(payout) + '!', "key":str(encode(json.dumps(key)))}
		else:
			return {"message":"Oh no! You're bankrupt! Use your old key to try again from where you left off, or restart!"}

@app.route('/current-car/<key>/')
def currentCar(key):
	key = decode(key)
	key = ast.literal_eval(key)
	car = key['car']
	return car

@app.route('/available-cars/')
def availableCars():
	return {'message':'Copy the key to the car that you want to buy! Make sure you have enough credit though!', 'cars':json.dumps(allCarsKeys)}

@app.route('/buy-car/<key>/<carKey>/')
def buyCar(key, carKey):
	key = decode(key)
	key = ast.literal_eval(key)
	coins = key["coins"]
	carKey = decode(carKey)
	carKey = ast.literal_eval(carKey)
	price = carKey["price"]
	if float(coins) < float(price):
		return {"message":"Oh no! You don't have enough credits to buy this car! Win more races, then try again!"}
	else:
		key["car"] = carKey
		car = key["car"]
		return {"message":"Yay! You've bought the " + car["name"] + "!"}

app.run(host="0.0.0.0", port=8080)