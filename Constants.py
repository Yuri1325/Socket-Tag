class Constants:
    def __init__(self):
        devices = ["(0)Laptop","(1)PC","(2)Laptop@Hotspot","(3)Laptop@School","(4)Enter your own ip"]
        deviceIps=["192.168.1.6","192.168.1.10","172.20.10.2","10.111.0.46",str(input("Enter the ipv4: "))]
        self.SERVER = deviceIps[int(input("What device are you using "+str(devices)+": "))]
        self.PORT = 5050
       