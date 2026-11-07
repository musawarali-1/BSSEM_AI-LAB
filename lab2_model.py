COLD_LIMIT = 18
HOT_LIMIT = 26
def choose_mode(temperature, occupied):
    # occupancy has the highest priority, an empty room is always ECO
    if not occupied:
        return "ECO"
    if temperature < COLD_LIMIT:
        return "HEAT"
    if temperature > HOT_LIMIT:
        return "COOL"
    return "OFF"

class ReflexAgent:
   def act(self, percept):
     target = choose_mode(percept["temperature"], percept["occupied"])
    return target, True

class StatefulAgent:

    def __init__(self):
    self.previous_mode = None
     def act(self, percept):
        target = choose_mode(percept["temperature"], percept["occupied"])
        send = target != self.previous_mode
        self.previous_mode = target
        return target, send
