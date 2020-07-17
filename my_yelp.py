import requests

def search_businesses():
    
    api_key = "C06s_2SrxRd2j5Bv3dk5z7xl7uUeiFUo7znDcbQCVjdSeJ99bS-FOKchxUcJSXf1ouwwaRkEQtINN1IsjKEHpbdEp7tmxBrq1P7ABCU1dGKaXRTwtnBoNzVNRAcSX3Yx"
    
    url = "https://api.yelp.com/v3/businesses/search"
    
    my_headers = {
        "Authorization": f"Bearer {api_key}"    
    }
    
    my_params = {
        "term": "restaurants",
        "location": "chicago",
        "limit": 3,
    }
    
    businesses_object = requests.get(url, params=my_params, headers=my_headers)
    
    businesses_dict = businesses_object.text
    
    return businesses_dict

invoke_yelp = search_businesses()
