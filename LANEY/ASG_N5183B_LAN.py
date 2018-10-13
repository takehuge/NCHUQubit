from visa import ResourceManager
from time import time, sleep
from numpy import arange
from colorama import Fore, Back, init
init(autoreset=True)

start = time()
rm = ResourceManager()

# ip2 = "192.168.0.12"
# # pna = rm.open_resource("TCPIP0::%s::inst0::INSTR" %ip2)
# pna = rm.open_resource("TCPIP0::%s::8088::inst0::INSTR" %ip2)
# who = pna.query("*IDN?")
# print("I am %s" %who)

ip = "169.254.0.1"
# asg = rm.open_resource("TCPIP0::169.254.157.31::inst0::INSTR")
# asg = rm.open_resource("TCPIP0::%s::inst0::INSTR" %ip)
asg = rm.open_resource("TCPIP0::%s::INSTR" %ip)
# asg = rm.open_resource("TCPIP0::A-N5183B-270812.local::5025::SOCKET")
# asg = rm.open_resource("TCPIP0::A-N5183B-270812.local::inst0::INSTR")

asg.read_termination = '\n'
asg.timeout = 8000   # milisec
asg.write("*RST")

who = asg.query("*IDN?")
print("I am %s" %who)

ip = asg.query(":SYSTem:COMMunicate:LAN:IP?")
print("IP: %s" %ip)

feq = asg.query(":FREQ?")
print("frequency: %sGHz" %(float(feq)/1e9))

start_freq = float(input(Back.WHITE + Fore.BLACK + "Enter Starting Frequency (GHz): "))
stop_freq = float(input(Back.WHITE + Fore.BLACK + "Enter Last Frequency (GHz): "))
N = int(input(Back.WHITE + Fore.BLACK + "How many points: "))

i = 1
for freq in arange(start_freq, stop_freq, (stop_freq - start_freq)/N):
    asg.write(":FREQ %sGHz" %freq)
    feq = asg.query(":FREQ?")
    sleep(1)
    print(Back.BLACK + Fore.YELLOW + "%s. frequency %s" %(i, feq))
    i += 1

asg.write(":POW -10dBm")
asg.write("OUTP 0")    #1 is ON  0 is OFF







duration = time() - start
asg.close()
print("Done after %ss" %duration)
