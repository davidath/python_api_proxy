class C42Dispacher(object):
      api_token = None #token used in requests to Calendar42 API
      cached_response = None
      cache_time_interval = None
      start_t = None
      
      def __init__ (self,token,cti):
          self.api_token = token
          self.cache_time_interval = cti
