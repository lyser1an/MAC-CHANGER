import subprocess
import optparse
import random


def get_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    return parse_object.parse_args()


def mac_change_main(us_interface,us_mac):
    subprocess.call(["ifconfig",us_interface ,"down"])
    subprocess.call(["ifconfig",us_interface ,"hw","ether",us_mac])
    subprocess.call(["ifconfig",us_interface ,"up"])


def random_mac_generate():
    mac = [ 0x00, 0x16, 0x3e,
    random.randint(0x00, 0x7f),
    random.randint(0x00, 0xff),
    random.randint(0x00, 0xff) ]
    return':'.join(map(lambda x: "%02x" % x, mac))


def control_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    print(ifconfig)


print("Started...")
(u_inputs,arguments)= get_inputs()
mac_change_main(u_inputs.interface,random_mac_generate())
control_mac(u_inputs.interface)