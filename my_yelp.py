import requests, json

def search_businesses(search_term, search_location):
    
    api_key = "C06s_2SrxRd2j5Bv3dk5z7xl7uUeiFUo7znDcbQCVjdSeJ99bS-FOKchxUcJSXf1ouwwaRkEQtINN1IsjKEHpbdEp7tmxBrq1P7ABCU1dGKaXRTwtnBoNzVNRAcSX3Yx"
    
    url = "https://api.yelp.com/v3/businesses/search"
    
    my_headers = {
        "Authorization": f"Bearer {api_key}"    
    }
    
    my_params = {
        "term": search_term,
        "location": search_location,
        "limit": 3,
    }
    
    businesses_object = requests.get(url, params=my_params, headers=my_headers)
    
    businesses_str = businesses_object.text
    
    businesses_json = json.loads(businesses_str)
    
    businesses_list = businesses_json["businesses"]
    
    return businesses_list


# invoke_yelp = search_businesses("restaurants", "chicago")
# print(invoke_yelp)
