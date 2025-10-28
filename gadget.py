class Gadget:
    def __init__(self):
        print("Gadget started")


class Phone(Gadget):
    def start(self):
        print("welcome")

class laptops(Gadget):
    def start(self):
        print("chipy welcome")

gadgets = [Phone(),laptops()]

for Gadget in gadgets:
    Gadget.start()



class Camera:
    def __init__(self):
        print("photo taken")

class WIFIEnabled:
    def connect_wifi(self):
        print("connected to WIFI")


class Smartphone(Phone,Camera,WIFIEnabled):
    def start(self):
        print("welcome human.....")

class SmartPrinter(Gadget,WIFIEnabled):
    def start(self):
        print("smartphone is starting")


devices = [Smartphone(), SmartPrinter()]

for device in devices:
    device.start()
    if isinstance(device,Camera):
        device.take_photo()
    if isinstance(device,WIFIEnabled):
        device.connect_wifi()    
        
        


        

        