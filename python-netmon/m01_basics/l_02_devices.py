import string
from random import choice
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list()
for index in range(10):
    device = dict()

    device["name"] = (
        choice(["r2", "r3", "r4", "r5", "r6"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )

    device["vendor"] = choice(["cisco", "juniper", "arista"])
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(
            ["12.1(T).84", "14.07X", "8.12(S).010", "2045"])

    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["36.23.1", "8.43.12", "6.45", "6.03"])

    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(
            ["2.45", "2.55", "2.92", "2.92.145", "3.01"])

    device["ip"] = "10.0.0." + str(index)

    for key, values in device.items():
        print(f"{key:>16s} : {values}")

    devices.append(device)
print(".............Printed in Table Form...............")
print(tabulate(sorted(devices, key=itemgetter(
    "vendor", "os", "version")), headers="keys"))
