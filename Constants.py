class Constants:
    def __init__(self):
        devices = ["(0)Laptop","(1)PC","(2)Laptop@Hotspot","(3)Laptop@School"]
        deviceIps=["192.168.1.4","192.168.1.10","172.20.10.2","10.111.0.46"]
        self.SERVER = deviceIps[int(input("What device are you using "+str(devices)+": "))]
        self.PORT = 5050
       