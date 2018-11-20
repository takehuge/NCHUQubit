# Communicating via LAN using SCPI

from visa import ResourceManager
from time import time, sleep
from numpy import arange
from colorama import Fore, Back, init
init(autoreset=True)

start = time()
rm = ResourceManager()

ip = "192.168.0.6"
pna = rm.open_resource("TCPIP0::%s::hpib7,16::INSTR" %ip)

pna.read_termination = '\n' #omit termination tag from output 
pna.timeout = 8000 #set timeout

who = pna.query("*IDN?")
print("I am %s" %who)

#Clear buffer memory
pna.write(':SENS:CORR:COLL:CLE')
# Performs a standard Preset, then deletes the default trace, measurement, and window.
# The PNA screen becomes blank.
pna.write('SYST:FPReset')

# switch on pna
pna.write('OUTP ON')

# turn on two windows (can up to 4?)
pna.write("DISP:WIND1:STATe ON")
pna.write("DISP:WIND2:STATe ON")

# Create a trace called "sdd21", and for that trace turn on the balanced transformation
# and set the balanced transformation to BBAL SDD21.
# Trace sdd21
pna.write("CALC:PAR:DEF:EXT ""sat11"",S11")
pna.write("CALC:PAR:SEL ""sat11""")
pna.write("CALC:FSIM:BAL:PAR:STATe ON")
pna.write("CALC:FSIM:BAL:PAR:BBAL:DEF SAT11")
# Feed the sdd21 trace to window 1, trace 1
pna.write("DISP:WIND1:TRAC1:FEED ""sat11""")

pna.write("CALC:PAR:DEF:EXT ""sdd22"",S22")
pna.write("CALC:PAR:SEL ""sdd22""")
pna.write("CALC:FSIM:BAL:PAR:STATe ON")
pna.write("CALC:FSIM:BAL:PAR:BBAL:DEF SDD22")
# Feed the sdd21 trace to window 1, trace 1
pna.write("DISP:WIND1:TRAC2:FEED ""sdd22""")


# switch off pna
pna.write('OUTP OFF')
