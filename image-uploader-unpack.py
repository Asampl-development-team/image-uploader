from PIL import Image
import numpy as np
import sys

def bytes_to_num(bts):
    snd, fst = bts
    return (snd << 8) | fst

def read_packet(stream):
    try:
        width = bytes_to_num(stream.read(2))
        height = bytes_to_num(stream.read(2))
        channels = stream.read(1)[0]

        full_size = width * height * channels
        data = stream.read(full_size)
        data = np.array(list(data), dtype='uint8')
        data = data.reshape((width, height, channels))
        return data
    except:
        return None


with open(sys.argv[1], 'br') as f:
    i = 0
    while True:
        img = read_packet(f)
        if img is None:
            break

        Image.fromarray(img).save('unpack/%s.png' % i)
        i += 1
