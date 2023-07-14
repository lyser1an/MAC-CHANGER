import subprocess
import optparse

def get_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac",dest="mac_address",help="mac address!")
    return parse_object.parse_args()


def mac_change_main(us_interface,us_mac):
    subprocess.call(["ifconfig",us_interface ,"down"])
    subprocess.call(["ifconfig",us_interface ,"hw","ether",us_mac])
    subprocess.call(["ifconfig",us_interface ,"up"])

def control_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    print(ifconfig)


print("Started...")
(u_inputs,arguments)= get_inputs()
mac_change_main(u_inputs.interface,u_inputs.mac_address)
control_mac(u_inputs.interface)