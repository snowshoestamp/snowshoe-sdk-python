# Overview
This is a sdk package that can be used in your python code as a plugin to be able to transfer a properly encoded string that represents a stamps points to SnowShoe servers and get a response with stamp information.

# Installing

You can install `snowshoe-stamp-sdk` via [the PIP package](https://pypi.org/project/snowshoe-stamp-sdk/). 

    $ pip install snowshoe-stamp-sdk

# Getting Started

1. To get the app running, you will need to create an app on our site. Go to https://app.snowshoestamp.com/ and Sign In if you have an account or sign up if you don't have one. Once you are logged in, click “New App” to create a new one.

2. After you have created the new application look at it's settings and you will find 'API Key 1' and 'API Key 2'. These can both be used to pass through as the needed param `api_key` to get stamp data back from our servers.

3. The stamp data passed to our servers is encoded in Base64 and then sent through as form-data. If you use our snowshoe jquery plugin to capture stamp touch point data ( located here: https://cdn.snowshoestamp.com/snowshoe-jquery/0.3.3/jquery.snowshoe.js ) then you don't have to worry about this because the data passed through will already be encoded. In this example we will use mock data of points in Base64 (`W1swLDBdLFszNiwzNl0sWzM2LDBdLFsyMCw0XSxbOCwzNl1d`) to get a stamp return when we send the request.

4. Here is a simple example that uses the mock data (`W1swLDBdLFszNiwzNl0sWzM2LDBdLFsyMCw0XSxbOCwzNl1d`) listed in the last step to test that the plugin sdk installed and is working properly.

```
    $ python
    >>> from sssapi import Client
    >>> client = Client(api_key="INSERT_YOUR_API_KEY_HERE")
    >>> response = client.call({"data":"W1swLDBdLFszNiwzNl0sWzM2LDBdLFsyMCw0XSxbOCwzNl1d"})
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

The information returned here is the data about the stamp relating to the points and api key you sent in the request.

# More info

-This sdk extension is made for simplistic retrieval of stamp data from our servers through the python language when your server uses this as it's primary code, such as a django server structure.
-For more info on how to use our product visit: 
    https://snowshoe.readme.io/v3.0/docs
