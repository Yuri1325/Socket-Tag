class Constants:
    def __init__(self):
        devices = ["(0)Laptop","(1)PC"]
        deviceIps=["192.168.1.11","192.168.1.10"]
        self.SERVER = deviceIps[int(input("What device are you using "+str(devices)+": "))]
        self.PORT = 5050
