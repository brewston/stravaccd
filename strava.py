import stravalib #sudo pip install stravalib
import math
import time
import sys
from stravalib import Client

# Access token instructions - https://yizeng.me/2017/01/11/get-a-strava-api-access-token-with-write-permission/

token = open(".token","r")
MyToken = token.read()
MyToken = MyToken.rstrip()
client = Client(access_token=MyToken)
athlete = client.get_athlete() # Get my full athlete record






def totaldistance(ID):
	totaldistance = 0
	#athlete = client.get_athlete(ID)
	#athlete_stats = athlete.stats(ID)
	activitiesthiswinter = client.get_activities(after="2018-11-01T00:00:00Z", limit=500) # Download all activities this winter

	for activity in activitiesthiswinter:
		totaldistance += int(stravalib.unithelper.miles(activity.distance)) #add up the total distance
	return totaldistance

def totalkudos(ID):
        totalkudos = 0
        activitiesthiswinter = client.get_activities(after="2018-11-01T00:00:00Z", limit=500) # Download all activities this winter

        for activity in activitiesthiswinter:
                totalkudos +=int(activity.kudos_count)
        return totalkudos


MyName = athlete.firstname
MyID = athlete.id
MyTotalDistance = totaldistance(MyID)
MyTotalKudos = totalkudos(MyID)
MyCity = athlete.city


	



print ("{} from {} has cycled {} miles for Cycle Down Dementia receiving {} kudos".format(MyName,MyCity, MyTotalDistance, MyTotalKudos))


