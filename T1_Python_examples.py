import sys

def Python_var_conversion():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    i = 20
    s = str(i)
    print (type(s))

    ss = "123"
    j = int(ss)
    print(type(j))

    sss = "3.14"
    f = float(sss)
    print(type(f))


def Python_complex_var_assignment():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    i,j = 1,2
    print(i,j)

    a = 1
    a,b = 2*a, 4*a
    print (a,b)

    x = y = z = 111
    print (x,y,z)

def Python_string_ops():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    s1 = "first"
    s2 = "second"
    s = s1 + " and " + s2
    print (s)

    ipaddr = "192.168.1.3"
    octets=ipaddr.split('.')
    print(octets[0], octets[1], octets[2], octets[3])

    last = int(octets[3])
    ponovo = octets[0] + "." + octets[1] + "." + octets[2] + "." + str(last+1)
    print (ponovo)

def Python_string_formatting():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    i = 12345
    j = 67890
    s1 = "First number is {} and second number is {:,d}".format(i, j)
    print(s1)

    print()

    n1 = 10
    n2 = 20
    n3 = 30
    print("Third number is {2} then first is {0} then middle is {1} and third again is {2}".format(n1, n2, n3))

    print()

    b1 = 100
    b2 = 200
    print("First number is {first}, second is {second} and first again is {first}".format(first=b1, second=b2))

    print()

    print("{:10s} {:20s} {:>30s}".format("EFP ID", "Interface", "Description"))
    print("{:-^62}".format("-"))
    print("{:10s} {:20s} {:>30s}".format("10", "GigabitEthernet1", "Interface to DC"))

def Python_arrays():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    array = [1, 3, 5, 7, 9, 11]

    print("Array has " + str(len(array)) + " members")
    print(array[0])
    print(array[2])
    print(array[4])

    print ()

    build_array = []

    build_array.append(2)
    build_array.append(4)
    build_array.append(6)

    print(build_array)

    del_array = [10, 11, 12, 13, 14, 15, 16, 17]

    del(del_array[7])
    print(del_array)
    del(del_array[1:3])
    print(del_array)


def Python_sets():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    set1 = { 1, 2, 3, 4, 5 }
    print (set1)
    n1 = 1
    n2 = 7
    print ("set1 has "+str(n1)+": " + str(n1 in set1))
    print ("set1 has "+str(n2)+": " + str(n2 in set1))

    set2 = { 4, 5, 6, 7, 8}

    union= set1 | set2
    print ("Union is", union)

    intersect = set1 & set2
    print("Intersection is", intersect)

    set3 = set()
    set3.add(100)
    set3.add(101)
    set3.add(102)
    set3.add(100)
    print(set3)

def Python_dictionaries():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    dict = {'Name': 'Zara', 'Parents' : { 'Mother' : 'Mary', 'Father' : 'Fred'}}

    print ("Name: ", dict['Name'])
    print ("Mother: ", dict['Parents']['Mother'])
    print ("Father: ", dict['Parents']['Father'])

    dict.update({'Best Friend' : 'Lara'})
    print ("Best Friend: ",dict['Best Friend'])

def Python_if(num):
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    if num < 10:
       print ("Num is smaller then 10")
    else:
       print ("Num is bigger or equal then 10")


def Python_for():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    for i in range(1,5):
        print(i)

    array = [1,10,100,1000]
    for i in array:
        print (i)

    array1 = [1,10,100,1000]
    array2 = ["one", "ten", "hundred"]

    for i,s in zip(array1,array2):
        print(i,s)

def Python_while():
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    i = 5
    array_of5s = []
    while (i<100):
        array_of5s.append(i)
        i = i+10
    print(array_of5s)

def Python_func (arg1, arg2 = 1, arg3 = 2):
    print(arg1, arg2, arg3)

def Python_read_file_1(f):
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    for line in f:
        print (line)

def Python_read_file_2(f):
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    array_of_lines = f.readlines()
    for line in array_of_lines:
        print (line)

def Python_read_file_3(f):
    print("{0:*^40}".format(sys._getframe().f_code.co_name))

    text = f.read()
    array_of_lines = text.splitlines()

    for line in array_of_lines:
        print (line)
