class DataHandler(object):
    SENSIBILITY_THRESHOLD = 500
    RIGHT_DIRECTION = 'RIGHT'
    LEFT_DIRECTION = 'LEFT'
    FORWARD_DIRECTION = 'FORWARD'
    BACKWARD_DIRECTION = 'BACKWARD'
    CHANGE_COLOR_ACTION = 'CHANGE_COLOR'

    def get_direction(self, data_position):
        direction = ''
        if data_position.get_pos_x() > self.SENSIBILITY_THRESHOLD:
            direction = self.RIGHT_DIRECTION

        if data_position.get_pos_x() < -self.SENSIBILITY_THRESHOLD:
            direction = self.LEFT_DIRECTION

        if data_position.get_pos_y() > self.SENSIBILITY_THRESHOLD:
            direction = self.FORWARD_DIRECTION

        if data_position.get_pos_y() < -self.SENSIBILITY_THRESHOLD:
            direction = self.BACKWARD_DIRECTION

        return direction

    def get_action(self, data):
        action = ''
        if data == 'Secouer':
            action = self.CHANGE_COLOR_ACTION

        return action
