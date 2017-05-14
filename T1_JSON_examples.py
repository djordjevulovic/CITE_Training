import requests
import json
from T1_REST_examples import REST_GET, REST_POST, HTTP_ACCEPT
import sys

def JSON_REST_GET(url, username, password):

    return REST_GET(url, username, password, HTTP_ACCEPT.JSON).json()

def JSON_REST_GET_Test():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    try:
        url = "https://cmxlocationsandbox.cisco.com/api/config/v1/aps/00:2b:01:00:08:00"
        json = JSON_REST_GET(url, "learning", "learning")
        print(json)
    except requests.exceptions.RequestException:
        print("ERROR: cannot send request to {}".format(url))

def JSON_Prettyprint():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    url = "https://cmxlocationsandbox.cisco.com/api/config/v1/aps/00:2b:01:00:08:00"
    json_obj = JSON_REST_GET(url, "learning", "learning")
    print(json.dumps(json_obj, sort_keys=True, indent=4))

def JSON_Parse():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    url = "https://cmxlocationsandbox.cisco.com/api/config/v1/aps/00:2b:01:00:08:00"
    json = JSON_REST_GET(url, "learning", "learning")
    print("AP {} works in mode {}".format(json["name"],json["apMode"]))

def JSON_print_APs():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    url = "https://cmxlocationsandbox.cisco.com/api/config/v1/aps/"
    json = JSON_REST_GET(url, "learning", "learning")
    for ap in json:
        print("AP {} MAC {}".format(ap["name"], ap["radioMacAddress"]))

def JSON_print_AP_radios():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    url = "https://cmxlocationsandbox.cisco.com/api/config/v1/aps/"
    json = JSON_REST_GET(url, "learning", "learning")
    for ap in json:
        print("AP {} MAC {}".format(ap["name"],ap["radioMacAddress"]))
        for radio in ap["apInterfaces"]:
            print ("---- Band {} Channel {} Power {}".format(radio["band"],radio["channelNumber"],radio["txPowerLevel"]))

def JSON_build_from_dictionary():

    intf_array = []

    for n in range (0,3):
        intf_dic = { "name" : str(n) , "description" : "Description of GigabitEthernet{}".format(n) }
        intf_array.append(intf_dic)

    dict = { "Cisco-IOS-XE-native:interface": { "GigabitEthernet": intf_array } }

    print(json.dumps(dict, sort_keys=True, indent=4))

def JSON_REST_POST(url, username, password, payload_as_dict):

    return REST_POST(url, username, password, json.dumps(payload_as_dict, sort_keys=False), HTTP_ACCEPT.JSON)

def JSON_REST_POST_Test():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    try:
        url = "https://cmxlocationsandbox.cisco.com/api/config/v1/aaa/users"
        username = "learning"
        password = "learning"
        payload = { "username" : "USERCITE9999", "password" : "PASSCITE9999" }

        code = JSON_REST_POST(url, username, password, payload)

        print("Response Code = " + str(code))

    except requests.exceptions.RequestException:
        print("ERROR: cannot send request to {}".format(url))
