class Lamp:
    def __init__(self, color):
        self.color = color
        self.on = False

    def state(self):
        return "The lamp is off." if not self.on else "The lamp is on."

    def toggle_switch(self):
        self.on = not self.on
