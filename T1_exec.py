from io import StringIO

from T1_Python_examples import Python_complex_var_assignment, Python_var_conversion, Python_string_ops, Python_string_formatting, Python_arrays, \
    Python_sets, Python_dictionaries, Python_if, Python_for, Python_while, Python_func, Python_read_file_1, Python_read_file_2, Python_read_file_3
from T1_REST_examples import REST_GET_Basic_Test, REST_GET_Basic_Test_wrong_host, REST_GET_Basic_Test_wrong_host_with_exception, REST_GET_Test, \
    REST_POST_Test, REST_DELETE_Test
from T1_XML_examples import Build_Simple_XML, Build_YANG_Like_XML, Print_XML, XML_Find_IP, XML_Traverse, XML_Find_IP_minidom
from T1_JSON_examples import JSON_Prettyprint, JSON_REST_GET_Test, JSON_Parse, JSON_print_APs, JSON_print_AP_radios, JSON_REST_POST_Test, \
    JSON_build_from_dictionary
#################### Python Examples ####################################

#Python_complex_var_assignment()

#Python_var_conversion()

#Python_string_ops()

Python_string_formatting()

#Python_arrays()

#Python_sets()

#Python_dictionaries()

#Python_if(11)

#Python_for()

#Python_while()

#Python_func(5,6,7)
#Python_func(arg3=103, arg2=102, arg1=101)
#Python_func(0)
#Python_func(10,arg3=12)

#Python_read_file_1(open("testfile.txt"))
#Python_read_file_2(open("testfile.txt"))
#Python_read_file_3(open("testfile.txt"))
#Python_read_file_3(StringIO("line 1\nline 2\nline 3\n"))

#################### REST Examples ####################################
#REST_GET_Basic_Test()

#REST_GET_Basic_Test_wrong_host()

#REST_GET_Basic_Test_wrong_host_with_exception()

#REST_GET_Test()

#REST_POST_Test()

#REST_DELETE_Test()
#################### XML Examples ####################################
#Print_XML(Build_Simple_XML())

#Print_XML(Build_YANG_Like_XML())

xml_string = """
<GigabitEthernet xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" xmlns:y="http://tail-f.com/ns/rest"  xmlns:ios="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <name>2</name>
    <description>SHAD was Here!</description>
    <ip>
        <address>
            <primary>
                <address>192.168.1.1</address>
                <mask>255.255.255.0</mask>
            </primary>
        </address>
    </ip>
    <mop>
        <enabled>false</enabled>
    </mop>
    <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
        <auto>true</auto>
    </negotiation>
</GigabitEthernet>
"""

#XML_Traverse(xml_string)

#XML_Find_IP(xml_string)

#XML_Find_IP_minidom(xml_string)

#################### JSON Examples ####################################
#JSON_REST_GET_Test()

#JSON_Prettyprint()

#JSON_Parse()

#JSON_print_APs()

#JSON_print_AP_radios()

#JSON_build_from_dictionary()

#JSON_REST_POST_Test()
