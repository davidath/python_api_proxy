import urllib2
import json
import time

class C42Dispacher(object):
      api_token = None #token used in requests to Calendar42 API
      cached_response = None #variable for response storing
      cache_time_interval = None #interval in seconds used as cache timer
      start_t = None #variable for timestamping
      
      def __init__ (self,token,cti):
          #API token & cache interval initialization
          self.api_token = token
          self.cache_time_interval = cti
          
      def c42_api_call(self,event_id):
          time = 
          # url initialization
          evt_details_url = "https://demo.calendar42.com/api/v2/events/"+event_id+"/"
          evt_sub_url = "https://demo.calendar42.com/api/v2/event-subscriptions/?event_ids=["+event_id+"]"
          # header initialization
          req_headers = {
           "Accept": "application/json",
           "Content-type": "application/json",
           "Authorization": "Token " + self.api_token,
          }
          # GET event_details request and contents
          details_request = urllib2.Request(evt_details_url,headers=req_headers)
          details_contents = urllib2.urlopen(details_request).read()
          # GET event_with_sub request and contents
          sub_request = urllib2.Request(evt_sub_url,headers=req_headers)
          sub_contents = urllib2.urlopen(sub_request).read()
          # return responses from C42 API as json
          return json.loads(details_contents),json.loads(sub_contents)
          
      def cache(self):
          

      def prepare_response(self,event_id):
          # This method is the one that views.py calls in order to serve responses
          # GET C42 api responses
          # Extract information about the event
          details,subscriptions = self.c42_api_call(event_id)
          details_data = details['data']
          # although the data array only contains one element(in this case) i dont want to use "magic number" and access it by details_data[0]
          for event_data in details_data:
              evt_json = event_data
          title = evt_json['title']
          # Extract information about the users that will attend to the event
          subscription_data = subscriptions['data']
          # Initialize attendees list
          attendees = []
          # Find the names of users that will attend our event
          for user in subscription_data:
              sub = user['subscriber']
              attendees.append(sub['first_name'])
          # Build response
          response = {}
          response['id'] = event_id
          response['title'] = title
          response['names'] = attendees
          return response
