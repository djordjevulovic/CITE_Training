import requests
import enum
import sys

def REST_GET_Basic(url, username, password):

    response = requests.get(url, auth=requests.auth.HTTPBasicAuth(username, password),verify=False)

    return response

def REST_GET_Basic_Test():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    r = REST_GET_Basic("https://cmxlocationsandbox.cisco.com/api/config/v1/aps/00:2b:01:00:08:00","learning","learning")
    print (r.text)

def REST_GET_Basic_Test_wrong_host():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    r = REST_GET_Basic("https://wrong.cisco.com/api/config/v1/aps/00:2b:01:00:08:00","learning","learning")
    print (r.text)

def REST_GET_Basic_Test_wrong_host_with_exception():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    try:
        url = "https://wrong.cisco.com/api/config/v1/aps/00:2b:01:00:08:00"
        r = REST_GET_Basic(url, "learning", "learning")
        print (r.text)
    except requests.exceptions.RequestException:
        print("ERROR: cannot send request to {}".format(url))

class HTTP_ACCEPT(enum.Enum):
    JSON = 1
    XML = 2
    VND_JSON = 3
    VND_XML = 4

def REST_GET(url, username, password, accept_type = None):

    accept_type_strings = {
        HTTP_ACCEPT.JSON: "application/json",
        HTTP_ACCEPT.XML: "application/xml",
        HTTP_ACCEPT.VND_JSON: "application/vnd.yang.data+json",
        HTTP_ACCEPT.VND_XML: "application/vnd.yang.data+xml",
    }

    if (accept_type != None):
        header = {"Accept": accept_type_strings.get(accept_type)}

    print (header)

    response = requests.get(url, headers=header, auth=requests.auth.HTTPBasicAuth(username, password),verify=False)

    return response

def REST_GET_Test():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    try:
        url = "http://ios-xe-mgmt.cisco.com:9443/restconf/api/config/native/interface/GigabitEthernet/2/"
        username = "root"
        password = "D_Vay!_10&"

        r = REST_GET(url, username, password, HTTP_ACCEPT.VND_XML)
        print(r.text)

        r = REST_GET(url, username, password, HTTP_ACCEPT.VND_JSON)
        print(r.text)

    except requests.exceptions.RequestException:
        print("ERROR: cannot send request to {}".format(url))

def REST_POST(url, username, password, payload, content_type = None):

    accept_type_strings = {
        HTTP_ACCEPT.JSON: "application/json",
        HTTP_ACCEPT.XML: "application/xml",
        HTTP_ACCEPT.VND_JSON: "application/vnd.yang.data+json",
        HTTP_ACCEPT.VND_XML: "application/vnd.yang.data+xml",
    }

    if (content_type != None):
        header = {"Content-Type": accept_type_strings.get(content_type)}

    response = requests.post(url, data=payload, auth=requests.auth.HTTPBasicAuth(username, password), headers=header, verify=False)

    return response.status_code

def REST_POST_Test():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    try:
        url = "https://cmxlocationsandbox.cisco.com/api/config/v1/aaa/users"
        username = "learning"
        password = "learning"
        payload = """
        {
           "username" : "USERCITE999",
           "password" : "PASSCITE999"
        }
        """

        code = REST_POST(url, username, password, payload, HTTP_ACCEPT.JSON)
        print("Response Code = " + str(code))

    except requests.exceptions.RequestException:
        print("ERROR: cannot send request to {}".format(url))


def REST_DELETE(url, username, password, payload, content_type = None):

    accept_type_strings = {
        HTTP_ACCEPT.JSON: "application/json",
        HTTP_ACCEPT.XML: "application/xml",
        HTTP_ACCEPT.VND_JSON: "application/vnd.yang.data+json",
        HTTP_ACCEPT.VND_XML: "application/vnd.yang.data+xml",
    }

    if (content_type != None):
        header = {"Content-Type": accept_type_strings.get(content_type)}

    response = requests.delete(url, data=payload, auth=requests.auth.HTTPBasicAuth(username, password), headers=header, verify=False)

    return response.status_code

def REST_DELETE_Test():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    try:
        url = "https://cmxlocationsandbox.cisco.com/api/config/v1/aaa/users/USERCITE999"
        username = "learning"
        password = "learning"
        payload = """
        {
           "username" : "USERCITE999"
        }
        """

        code = REST_DELETE(url, username, password, payload, HTTP_ACCEPT.JSON)
        print("Response Code = " + str(code))

    except requests.exceptions.RequestException:
        print("ERROR: cannot send request to {}".format(url))
