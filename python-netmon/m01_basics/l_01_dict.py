from pprint import pprint
from operator import itemgetter
from tabulate import tabulate
# list

device = ["cisco", "juniper", "nexus", "arista"]

for devices in device:

    print(f"{devices:>16s} : {device.index(devices)}")

# dictionary

device = [
    {
        "name": "r2Xj",
        "vendor": "cisco",
        "os": "ios",
        "version": "1900-1(T)",
        "ip": "10.0.0.1"
    },
    {
        "name": "r3XJ",
        "vendor": "arista",
        "os": "iosxe",
        "version": "1900-1(S)-9",
        "ip": "10.0.0.2"
    },
]
print("\n###...Simple Print...###")
print(device)

print("\n###...Pretty Print...###")
pprint(device)


print("\n###...Table form & sorted...###")
print(tabulate(sorted(device, key=itemgetter(
    "vendor", "os", "version")), headers="keys"))
