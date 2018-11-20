import subprocess
import platform
platinfo = platform.system()
print("THIS PLATFORM is %s" %platinfo)

IPlist, active = [], []
for i in range(10):
    IPlist.append("169.254.0." + str(i))

if platinfo == "Windows":
    pass
elif platinfo == "Darwin":
    for ip in IPlist:
        p = subprocess.Popen(["ping", "-c", "1", "-W" "1", ip], stdout=subprocess.PIPE)
        msg = [i for i in p.stdout]
        a = 0
        for msg in msg:
            b = int("ttl" in str(msg))
            a += b
        print("Scanning %s", ip)
        if a == 1:
            active.append(ip)

print("Active IP:")
for active in active:
    print(active)
