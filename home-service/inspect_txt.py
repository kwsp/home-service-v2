import glob
import struct
import binascii
from datetime import datetime


def unpack(fmat, data, index):
    unpackedStuff = struct.unpack_from(fmat, data, index)
    index += struct.Struct(fmat).size
    return idx, unpackedStuff

files = glob.glob('../data/*.txt')

files.sort()
breakpoint()

inFileName = files[5]
inFile = open(inFileName, 'rb')

timestamp = []
datetime_ = []
temperature = []
activity = []

for i, line in enumerate(inFile):
    data = binascii.a2b_base64(line)

    idx = 0
    idx, (time, temp, acti) = unpack('<IfI', data, idx)
    timestamp.append(time)
    datetime_.append(datetime.fromtimestamp(time))
    temperature.append(temp)
    activity.append(acti)
    print(str(time) + " T: " + str(temp) + " A:" + str(acti))

breakpoint()
