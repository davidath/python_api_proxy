# python_api_proxy

A simple python API proxy using Django framework in order to test my skills.

In order to accomplish the objective of this proxy i'll use a simple class called C42Dispacher.
Using classes makes the response more modular,more maintainable and reusable.
Being that modular makes it less prone to struggle in case of changes.
For example if we decide for a different path to our API proxy then all we have to do is change the path,
due to the architecture our class will maintain workabillity.

### Dispacher's Attributes

- api_token (Simple token used for API calls)
- cache_time_interval (time in seconds that the cached response will be stored)
- cached_response (json response that is cached for x minutes per request)
- start_t (timestamp of a request used for cache purposes)

### Dispacher's methods

- __ init __ (simple constructor for api_token/cache_time_interval)
- c42_api_call (method that performs multiple GET requests from C42 API)
- prepare_response (method that combines responses from c42_api_call)
- cache (method that caches the response for future uses)

### Technologies used

- Django framework (Manipulating GET requests to our API proxy)
- urllib2 (Manipulating requests and responses to C42 API)
- json (Manipulating JSON)
- time (Timestamps for cache purposes)

