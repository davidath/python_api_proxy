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
          #Starting Timestamp
          self.start_t = time.time()
          # url initialization
          evt_details_url = "https://demo.calendar42.com/api/v2/events/"+event_id+"/"
          evt_sub_url = "https://demo.calendar42.com/api/v2/event-subscriptions/?event_ids=["+event_id+"]"
          # header initialization
          req_headers = {
           "Accept": "application/json",
           "Content-type": "application/json",
           "Authorization": "Token " + self.api_token,
          }
          try:
              # GET event_details request and contents
              details_request = urllib2.Request(evt_details_url,headers=req_headers)
              details_contents = urllib2.urlopen(details_request).read()
              # GET event_with_sub request and contents
              sub_request = urllib2.Request(evt_sub_url,headers=req_headers)
              sub_contents = urllib2.urlopen(sub_request).read()
              # return responses from C42 API as json
              return json.loads(details_contents),json.loads(sub_contents)
          except: #If id is not valid
              return 'Event id not valid'
          
      def combine_and_cache(self,event_id):
          #Get C42 API responses if event id is valid
          try:
             details,subscriptions = self.c42_api_call(event_id)
          except: #if not return error
             response = {}
             response['Error'] = 'Event id not valid'
             return response
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
          self.cached_response = json.dumps(response)
          return response

      def prepare_response(self,event_id):
          # This method is the one that views.py calls in order to serve responses
          #If there is no timestamp (Running for the first time)
          if self.start_t is None:
             return self.combine_and_cache(event_id)
          #If class is not running for the first time then compare timestamps
          #Extract cached response id
          try: #Check if cached response has a valid event id
             cache_json = json.loads(self.cached_response)
          except:
             return self.combine_and_cache(event_id)
          #If timestamp hasn't passed 4.2 minutes and user requests the same event then return cached response
          if (time.time() - self.start_t < self.cache_time_interval) and (event_id == cache_json['id']):
                #although timestamp comparing is not needed i'll leave it there for proof that the response is cached for 4.2 minutes
                return json.loads(self.cached_response),(time.time() - self.start_t)
          else:
                #Reload cached response
                return self.combine_and_cache(event_id)
