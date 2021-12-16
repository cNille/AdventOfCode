print(chr(27)+'[2j')
print('\033c')
# f = open('16.test', 'r')
import math
import functools
f = open('16.input', 'r')
data = [x.strip() for x in f.readlines()][0]

def hex_to_bin(str_hex):
    return ''.join([str("{0:08b}".format(int(s, 16)))[4:] for s in str_hex])

def fprint(name, value):
    print("%s: %s (%d)" % (name, value, int(value, 2)))

def get_value(ptype, values):
    if ptype == 0:
        return sum(values)
    elif ptype == 1:
        return functools.reduce(lambda x, y: x * y, values, 1)
    elif ptype == 2:
        return min(values) 
    elif ptype == 3:
        return max(values) 
    elif ptype == 5:
        return 1 if values[0] > values[1] else 0
    elif ptype == 6:
        return 1 if values[1] > values[0] else 0
    elif ptype == 7:
        return 1 if values[1] == values[0] else 0


def parse_header(header_data, verbose=True):
    VERSION = header_data[:3]
    version = int(VERSION, 2)
    TYPE = header_data[3:6]
    ptype = int(TYPE, 2)
    if verbose:
        fprint("VERSION", VERSION)
        fprint("TYPE", TYPE)
    return (version, ptype)

def parse_packet(data, is_sub = False, verbose=True):
    if verbose:
        if is_sub:
            print('-- Subpacket: %s' % data)
        else:
            print('Packet: %s' % data)

    version, ptype = parse_header(data[:6], False)
    version_sum = version
    PAYLOAD = data[6:]
    
    if ptype == 4:
        # VALUE PACKAGE
        VALUE = ''
        i = 0
        while True:
            prefix = PAYLOAD[i]
            VALUE += PAYLOAD[i+1:i+5]
            i += 5
            if prefix == '0':
                break
        if verbose:
            fprint("VALUE", VALUE)
        return (PAYLOAD[i:], version, int(VALUE, 2))
    else:
        # Operations packet
        values = []
        LENGTH_TYPE = PAYLOAD[0]
        if verbose:
            fprint("LENGTH_TYPE", LENGTH_TYPE)
        if LENGTH_TYPE == '0':
            # LENGTHTYPE 0 
            TOTAL_LENGTH = PAYLOAD[1:16]
            if verbose:
                fprint("TOTAL_LENGTH", TOTAL_LENGTH)
            sub_length = int(TOTAL_LENGTH, 2)
            next_package = PAYLOAD[16:16+sub_length]
            while len(next_package) > 0:
                next_package, version, value= parse_packet(next_package, True, verbose)
                version_sum += version
                values.append(value)
            next_package = PAYLOAD[16+sub_length:]

        else: 
            # LENGTHTYPE 1 
            NBR_PACKAGES = PAYLOAD[1:12]
            if verbose:
                fprint("NBR_PACKAGES", NBR_PACKAGES)
            packages_count = int(NBR_PACKAGES, 2)

            next_package = PAYLOAD[12:]
            for i in range(packages_count):
                next_package, version, value = parse_packet(next_package, True, verbose)
                version_sum += version
                values.append(value)

        # RETURN RESULT 
        package_value = get_value(ptype, values)
        return (next_package, version_sum, package_value)

def parse_data(data):
    print('==========')
    print('PARSING DATA: %s' % data)
    print('--')
    packet = hex_to_bin(data)
    _left, version_sum, packet_value = parse_packet(packet, False, False)
    print("Version sum: %d" % version_sum)
    print("Packet value: %d" % packet_value)

# parse_data("D2FE28")
# parse_data("38006F45291200")
# parse_data("EE00D40C823060")
parse_data(data)
