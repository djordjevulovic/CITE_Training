from ncclient import manager
from lxml import etree

def NETCONF_prettyprint_XML_string(xml_string):
    xml_bytes = etree.fromstring(xml_string.encode('utf-8'))
    nice_xml_bytes = etree.tostring(xml_bytes, pretty_print=True)
    nice_xml_string = nice_xml_bytes.decode('utf-8')

    print(nice_xml_string)
def NETCONF_get_full_config():

    m = manager.connect(host="ios-xe-mgmt.cisco.com", port=10000, username="root", password="D_Vay!_10&", hostkey_verify=False)

    xml_response_string = m.get_config(source='running').data_xml

    NETCONF_prettyprint_XML_string(xml_response_string)

def NETCONF_get_interface_Gi2_config():

    filter_string = """
    <filter>
       <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
           <interface><GigabitEthernet>
               <name>2</name>
            </GigabitEthernet></interface>
        </native>
    </filter>
    """

    m = manager.connect(host="ios-xe-mgmt.cisco.com", port=10000, username="root", password="D_Vay!_10&", hostkey_verify=False)

    xml_response_string = m.get_config(source='running', filter=filter_string).data_xml

    NETCONF_prettyprint_XML_string(xml_response_string)

def NETCONF_create_new_subif():

    m = manager.connect(host="ios-xe-mgmt.cisco.com", port=10000, username="root", password="D_Vay!_10&", hostkey_verify=False)

    create_string = """
    <config>
       <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
			<interface><GigabitEthernet>
				<name>2.102</name>
				<encapsulation>
					<dot1Q><vlan-id>102</vlan-id></dot1Q>
				</encapsulation>
			</GigabitEthernet></interface>
  	  </native>
  	</config>
    """
    response = m.edit_config(config=create_string, target="running")

    print (response)

def NETCONF_add_ip_to_subif():

    m = manager.connect(host="ios-xe-mgmt.cisco.com", port=10000, username="root", password="D_Vay!_10&", hostkey_verify=False)

    config_e = etree.Element("config")

    native_e = etree.SubElement(config_e, "native", nsmap={None: 'http://cisco.com/ns/yang/Cisco-IOS-XE-native'})

    interface_e = etree.SubElement(native_e, "interface")

    gigabitethernet_e = etree.SubElement(interface_e, "GigabitEthernet")

    name_e = etree.SubElement(gigabitethernet_e, "name")
    name_e.text = "2.102"

    ip_e = etree.SubElement(gigabitethernet_e, "ip")

    address1_e = etree.SubElement(ip_e, "address")

    primary_e = etree.SubElement(address1_e, "primary")

    address2_e = etree.SubElement(primary_e, "address")
    address2_e.text = "102.102.102.1"

    mask_e = etree.SubElement(primary_e, "mask")
    mask_e.text = "255.255.255.0"

    response = m.edit_config(config=config_e, target="running")

    print (response)