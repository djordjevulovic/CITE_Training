from lxml import etree
from ncclient import manager
from T2_NETCONF_examples import NETCONF_prettyprint_XML_string
from T1_XML_examples import Print_XML

def NETCONF_Exercize_1():

    filter_string = """
    <filter>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>GigabitEthernet2.400</name>
      </interface>
    </filter>
    """

    m = manager.connect(host="ios-xe-mgmt.cisco.com", port=10000, username="root", password="D_Vay!_10&", hostkey_verify=False)

    xml_response_string = m.get_config(source='running', filter=filter_string).data_xml

    NETCONF_prettyprint_XML_string(xml_response_string)

def NETCONF_Exercize_2():
    # Add subinterface GigabitEthernet 2.400

    m = manager.connect(host="ios-xe-mgmt.cisco.com", port=10000, username="root", password="D_Vay!_10&", hostkey_verify=False)

    create_string = """
    <config>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
      <name>GigabitEthernet2.400</name>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
      <enabled>true</enabled>
      </interface>
  	</config>
    """
    response = m.edit_config(config=create_string, target="running")

    print (response)

def NETCONF_Exercize_3():

    m = manager.connect(host="ios-xe-mgmt.cisco.com", port=10000, username="root", password="D_Vay!_10&", hostkey_verify=False)

    config_e = etree.Element("config")

    interfaces_e = etree.SubElement(config_e, "interfaces", nsmap={None: 'urn:ietf:params:xml:ns:yang:ietf-interfaces'})

    interface_e = etree.SubElement(interfaces_e, "interface")

    name_e = etree.SubElement(interface_e, "name")
    name_e.text = "GigabitEthernet2.401"

    type_e = etree.SubElement(interface_e, "type", nsmap={"ianaift": 'urn:ietf:params:xml:ns:yang:iana-if-type'})
    type_e.text = "ianaift:ethernetCsmacd"

    enabled_e = etree.SubElement(interface_e, "enabled")
    enabled_e.text = "true"

    response = m.edit_config(config=config_e, target="running")
    print (response)


