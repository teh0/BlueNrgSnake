class DataPosition(object):
    def __init__(self, data):
        self.pos_x = data[0]
        self.pos_y = data[1]

    def get_pos_x(self, in_float=True):
        return float(self.pos_x) if in_float else self.pos_x

    def get_pos_y(self, in_float=True):
        return float(self.pos_y) if in_float else self.pos_y
