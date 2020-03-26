from position import Position
#ship class
class Ship():
  def __init__(self, position_type, start_position_x, start_position_y):
    self.position_type = position_type
    #create a position for ship
    position = Position(start_position_x, start_position_y)
    self.position = position
