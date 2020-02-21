# Overview
This is a sdk package that can be used in your python code as a plugin to be able to transfer a properly encoded string that represents stamp points to SnowShoe servers and get a response with stamp information.

# Installing

You can install `snowshoe-stamp-sdk` via [the PIP package](https://pypi.org/project/snowshoe-stamp-sdk/). 

    $ pip install snowshoe-stamp-sdk

# Getting Started

1. To be able to use this SDK tool you need to create an app first. You can learn how to [HERE](https://snowshoe.readme.io/v3.0/docs/part-1-create-a-snowshoe-application)

2. Make sure you get the API Key that you will need to run requests. You can learn more about the API Keys [HERE](https://snowshoe.readme.io/v3.0/docs/part-1-create-a-snowshoe-application#get-api-keys)

3. The stamp data passed to our servers is an array of x,y coordinates. These represent the touch points from the stamp that you are trying to get data for. If you are using our front-end jquery plugin (more info on this located [HERE](https://snowshoe.readme.io/v3.0/docs/maintained-libraries)) to capture stamp touch point data, then you can just pass that data directly through for the request with no need to change.

4. Here is a simple example that uses the mock data (`[[264,172],[267,371],[242,286],[69,375],[66,221]]`) to test that the plugin sdk installed and is working properly.

```
    $ python
    >>> from sssapi import Client
    >>> client = Client(api_key="INSERT_YOUR_API_KEY_HERE")
    >>> response = client.call("[[264,172],[267,371],[242,286],[69,375],[66,221]]")
    >>> print(response)
```

This should print out an unformatted JSON string showing a 'serial' of 'DEVA'. Formatted properly it should look more like this:

```
{
   "stamp":{
      "serial":"DEVA",
      "customName":"DEVA"
   },
   "receipt":"2b6a57a3-2862-4af9-b529-bcdbe13c0453",
   "created":"2020-02-05T20:10:39.8967579Z"
}
```

The information returned here is the data about the stamp relating to the points and api key you sent in the request. For more info on stamp data requests and returns go [HERE](https://snowshoe.readme.io/v3.0/docs/part-3-api-request)

# More info

- This sdk extension is made for simplistic retrieval of stamp data from our servers through the python language when your server uses this as it's primary code, such as a django server structure.
- For more info on how to use our product visit: 
    https://snowshoe.readme.io/v3.0/docs
