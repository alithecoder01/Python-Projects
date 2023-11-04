
from PublicRoom import PublicRoom
from PrivateRoom import PrivateRoom
from deviceType import DeviceType

name =input("Enter your name: ")
age = int(input("Enter Age: "))
numPers = int(input("Enter Number of Persons: "))
numHour = int(input("Enter Number of Hours: "))
deviceType = int(input("Which device do you want? \n 1-PS4\n 2-PS5 \n 3-Xbox \n 4-Pc \n Enter the number of the device: "))
roomType = int(input("Which room do you want? \n 1-Private room \n 2-Public Room \n Enter the number: "))

if deviceType == 1:
    deviceType = DeviceType.PS4.name
elif deviceType == 2:
    deviceType = DeviceType.PS5.name
elif deviceType == 3:
    deviceType = DeviceType.Xbox.name
elif deviceType == 4:
    deviceType = DeviceType.Pc.name


if roomType ==1:
    private = PrivateRoom(name,age,numPers,numHour,deviceType)
    private.toString()
elif roomType == 2:
    public = PublicRoom(name,age,numPers,numHour,deviceType)
    public.toString()

