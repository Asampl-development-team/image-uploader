import numpy as np

class Upload:
    def __init__(self):
        self.packets = []

    def pull(self):
        if len(self.packets) != 0:
            ret = self.packets[0]
            self.packets = self.packets[1:]
            return ret

    def upload(self, image):
        width, height, channels = image.shape

        packet = np.concatenate((
            self.num_to_bytes(width),
            self.num_to_bytes(height),
            np.array([channels], dtype='uint8'),
            image.flatten()))

        self.packets.append(packet)

    def num_to_bytes(self, num):
        fst = num & 0xFF
        snd = (num >> 8) & 0xFF

        return np.array([snd, fst], dtype='uint8')
