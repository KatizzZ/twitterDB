#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:35:09 2019

@author: shivam
"""

''' import mysql.connector

cnx = mysql.connector.connect(user='root', password='shivam96',
                              host='127.0.0.1',
                              database='twitterdb1')
cnx.close() '''

import mysql.connector
from mysql.connector import Error
import tweepy
import json
from dateutil import parser
import time
import os
import subprocess

''' #Could have placed these variables with environment settings file settings.sh
importing file which sets env variable
subprocess.call("./settings.sh", shell = True)
subprocess.call("/home/shivam/Desktop/python/settings.sh", shell = True)

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
password = os.environ['PASSWORD']

export CONSUMER_KEY='0Lwh9KtHD2AKbe59YyeLABfKu'
export CONSUMER_SECRET='eo9wxJJPGVFaWXgPidAjBBVlExSZNqfbVRtQbL63ijP2wS9s0w'
export ACCESS_TOKEN='2938216434-tQl8pbG27z1wSk6iAiO499EqMRmaUcxaQTlS0Wg'
export ACCESS_TOKEN_SECRET='kesC5nfVfMRZ66dw8z8v53hMnGlebWOemaAUOxmc0FVS6'
export PASSWORD='shivam96'

'''
#My Tokens
consumer_key = '0Lwh9KtHD2AKbe59YyeLABfKu'
consumer_secret = 'eo9wxJJPGVFaWXgPidAjBBVlExSZNqfbVRtQbL63ijP2wS9s0w'
access_token = '2938216434-tQl8pbG27z1wSk6iAiO499EqMRmaUcxaQTlS0Wg'
access_token_secret ='kesC5nfVfMRZ66dw8z8v53hMnGlebWOemaAUOxmc0FVS6'
password = 'shivam96'

def connect(username, created_at, tweet, retweet_count, place , location):
	"""
	connect to MySQL database and insert twitter data
	"""
	try:
		con = mysql.connector.connect(host = 'localhost',
		database='twitterdb', user='root', password = password, charset = 'utf8')
		

		if con.is_connected():
			"""
			Insert twitter data
			"""
			cursor = con.cursor()
			# twitter, golf
            #place your table name here (as Golf here) 
			query = "INSERT INTO Golf (username, created_at, tweet, retweet_count,place, location) VALUES (%s, %s, %s, %s, %s, %s)"
			cursor.execute(query, (username, created_at, tweet, retweet_count, place, location))
			con.commit()
			
			
	except Error as e:
		print(e,tweet,location,sep='^^^')

	cursor.close()
	con.close()

	return


# Tweepy class to access Twitter API to fetch tweets
class Streamlistener(tweepy.StreamListener):
	

	def on_connect(self):
		print("You are connected to the developer Twitter API")


	def on_error(self):
		if status_code != 200:
			print("error found")
			# returning false stream disconnected
			return False

	"""
	This method reads in tweet data as Json
	and extracts the data we want.
	"""
	def on_data(self,data):
		
		try:
			raw_data = json.loads(data)

			if 'text' in raw_data:
				 
				username = raw_data['user']['screen_name']
				created_at = parser.parse(raw_data['created_at'])
				tweet = raw_data['text']
				retweet_count = raw_data['retweet_count']

				if raw_data['place'] is not None:
					place = raw_data['place']['country']
					print(place)
				else:
					place = None
				

				location = raw_data['user']['location']

				#insert data just collected into MySQL database
				connect(username, created_at, tweet, retweet_count, place, location)
				print("Tweet colleted at: {} ".format(str(created_at)))
		except Error as e:
			print(e,tweet,location,sep='^^^')            

if __name__== '__main__':

	# # #Allow user input
	track = []
	while True:

		input1  = input("what do you want to collect tweets on?: ")
		track.append(input1)

		input2 = input("Do you wish to enter another word? y/n ")
		if input2 == 'n' or input2 == 'N':
			break
	
	print("You want to search for {}".format(track))
	print("Initialising Connection to developer Twitter API....")
	time.sleep(2)

	# authentification so we can access twitter
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api =tweepy.API(auth, wait_on_rate_limit=True)

	# create instance of Streamlistener
	listener = Streamlistener(api = api)
	stream = tweepy.Stream(auth, listener = listener)
    # You can also choose by given keywords here 
	#track = ['golf', 'masters', 'reed', 'mcilroy', 'woods']
	#track = ['WaitForSC']
	# choose what we want to filter by
	stream.filter(track = track, languages = ['en'])
