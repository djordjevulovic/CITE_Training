from lxml import etree
from io import BytesIO, StringIO
import sys
from xml.dom import minidom

def Build_Simple_XML():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    top = etree.Element("first")
    second = etree.SubElement(top, "second")
    second.text = 'Value for second'
    third = etree.SubElement(second, "third")
    third.text = 'Value for third'
    fourth = etree.SubElement(top, "fourth")
    fourth.text = 'Value for fourth'

    return top

def Print_XML(tree):
    xml_in_bytes = etree.tostring(tree, pretty_print=True)
    xml_in_str = xml_in_bytes.decode("utf-8")
    print(xml_in_str)


def Build_YANG_Like_XML():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    top = etree.Element("config")

    configuration = etree.SubElement(top, "interface-configurations",
                        nsmap={None: 'http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg'})

    interface_cfg = etree.SubElement(configuration, "interface-configuration")
    active = etree.SubElement(interface_cfg, "active").text = 'act'

    interface_name = etree.SubElement(interface_cfg, "interface-name").text = 'GigabitEthernet0/0/0/0'

    description = etree.SubElement(interface_cfg, "description").text = 'Configured by Python'

    return top

def XML_Traverse(xml_string):
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    my_events = ("start", "end")
    my_context = etree.iterparse(BytesIO(bytes(xml_string,'utf-8')),events=my_events)

    for action, elem in my_context:
        print("%s: %s" % (action, elem.tag))

def XML_Find_IP(xml_string):
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    my_events = ("start", "end")
    my_context = etree.iterparse(BytesIO(bytes(xml_string,'utf-8')),events=my_events)

    primary_tag = False

    for action, elem in my_context:

        if (action =="start" and elem.tag.endswith("primary")):
            primary_tag = True
        if (action == "end" and elem.tag.endswith("address") and primary_tag == True):
            print("IP Address: %s" % (elem.text))
        if (action == "end" and elem.tag.endswith("primary")):
            primary_tag = False

def XML_Find_IP_minidom(xml_string):
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    doc = minidom.parse(StringIO(xml_string))

    primary_nodes = doc.getElementsByTagName('primary')

    for primary in primary_nodes:
        for child in primary.childNodes:
            if (child.nodeType==minidom.Element.ELEMENT_NODE and child.tagName=="address"):
                print("IP Address: %s" % (child.firstChild.data))

