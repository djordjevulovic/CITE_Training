import requests
from T1_REST_examples import REST_GET, HTTP_ACCEPT


def Python_Exercize_1():
    # Build set containing strings with all IP addresses from subnet 192.168.1.0/28

    s = set()

    for i in range(0, 16):
        s.add("192.168.0." + str(i))

    print(s)

def Python_Exercize_2():
    # Build dictionary where key is “GigabitEthernet0.<N> and value is string “192.168.<N>.1/24” (N=1..10)

    d= { }

    for n in range(1, 11):
        key = "GigabitEthernet0.{}".format(n)
        value = "192.168.{}.1/24".format(n)
        d.update({key: value})

    print(d)

def REST_Exercize_1():
    # Build function to call GET Request with the following parameters and print the output:
    #   URL: http://ios-xe-mgmt.cisco.com:9443/restconf/api/config/native/interface?deep
    #   Username: “root”
    #   Password “D_Vay!_10&”
    # Encapsulation "application/vnd.yang.data+json"

    try:
        url = "http://ios-xe-mgmt.cisco.com:9443/restconf/api/config/native/interface?deep"
        username = "root"
        password = "D_Vay!_10&"

        r = REST_GET(url, username, password, HTTP_ACCEPT.VND_JSON)
        return r.text

    except requests.exceptions.RequestException:
        return ""




