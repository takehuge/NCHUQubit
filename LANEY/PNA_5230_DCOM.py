from visa import ResourceManager
from time import time, sleep
from numpy import arange
from colorama import Fore, Back, init
init(autoreset=True)

start = time()
rm = ResourceManager()

ip = "192.168.0.12"
pna = rm.open_resource("TCPIP0::%s::hpib7,16::INSTR" %ip)

pna.read_termination = '\n' #omit termination tag from output 
pna.timeout = 8000 #set timeout

who = pna.query("*IDN?")
print("I am %s" %who)

#Clear buffer memory
pna.write(':SENS:CORR:COLL:CLE') 

# switch on pna
pna.write('OUTP OFF')

# turn on four windows
pna.write("DISP:WIND1:STATe ON")
pna.write("DISP:WIND2:STATe ON")
pna.write("DISP:WIND3:STATe ON")
pna.write("DISP:WIND4:STATe ON")
