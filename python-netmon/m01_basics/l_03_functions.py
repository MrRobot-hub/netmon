from tabulate import tabulate
import string
from random import choice


def create_device(devices=1, subnets=1):

    created_devices = list()

    if devices > 254 or subnets > 254:
        print("Error: Too many devices and/or subnets requested!")
        return created_devices, "Sorry"

    for subnet_index in range(subnets+1):
        for device_index in range(devices+1):

            device = dict()

            device["name"] = (
                choice(["r1", "r2", "r3", "r4", "r5"])
                + choice(["U", "L"])
                + choice(string.ascii_letters)
            )
            device["vendor"] = choice(["cisco", "juniper", "arista"])
            if device["vendor"] == "cisco":
                device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
                device["version"] = choice(
                    ["12.1(T).84", "14.07X", "8.12(S).010", "2045"])

            elif device["vendor"] == "juniper":
                device["os"] = "junos"
                device["version"] = choice(
                    ["36.23.1", "8.43.12", "6.45", "6.03"])

            elif device["vendor"] == "arista":
                device["os"] = "eos"
                device["version"] = choice(
                    ["2.45", "2.55", "2.92", "2.92.145", "3.01"])

            device["ip"] = "10.0." + \
                str(subnet_index) + "." + str(device_index)

            created_devices.append(device)
    return created_devices, "you did it!"


obj, stringReturned = create_device(devices=255, subnets=255)

with open("devices.conf", "w") as f:
    f.write(tabulate(obj, headers="keys"))
print(stringReturned)
# print(tabulate(obj, headers="keys"))  # printing devices * subnets = devices
