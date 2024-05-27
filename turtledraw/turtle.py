import math

from pyaxidraw import axidraw


class TurtleDraw:
    def __init__(self, model, units):
        self._h = 0

        # TODO: connection method
        self.axidraw = axidraw.AxiDraw()
        self.axidraw.interactive()

        if not self.axidraw.connect():
            quit()

        # TODO: options method
        self.axidraw.options.model = model
        self.axidraw.options.units = units
        self.axidraw.update()

    def _to_degrees(self, x):
        return math.degrees(x) % 360

    def setheading(self, heading) -> None:
        self._h = heading

    def goto(self, x, y) -> None:
        self.axidraw.goto(x, y)

    def home(self) -> None:
        self.axidraw.block()
        self.goto(0, 0)

    def pendown(self) -> None:
        self.axidraw.pendown()

    def penup(self) -> None:
        self.axidraw.penup()

    def position(self) -> tuple:
        return self.axidraw.turtle_pos()

    def forward(self, distance) -> None:
        x = distance * math.cos(math.radians(self._h))
        y = distance * math.sin(math.radians(self._h))
        self.axidraw.go(x, y)

    def backward(self, distance) -> None:
        x = -distance * math.cos(math.radians(self._h))
        y = -distance * math.sin(math.radians(self._h))
        self.axidraw.go(x, y)

    def right(self, angle) -> None:
        self.setheading(self._h + angle)

    def left(self, angle) -> None:
        self.setheading(self._h - angle)

    def circle(self, radius, extent=None, steps=None):
        if extent is None:
            extent = 360
        if steps is None:
            steps = int(round(abs(2 * math.pi * radius * extent / 360)))
            steps = max(steps, 4)
        cx = self.position()[0] + radius * math.cos(math.radians(self._h + 90))
        cy = self.position()[1] + radius * math.sin(math.radians(self._h + 90))
        a1 = self._to_degrees(
            math.atan2(self.position()[1] - cy, self.position()[0] - cx)
        )
        a2 = a1 + extent if radius >= 0 else a1 - extent
        for i in range(steps):
            p = i / float(steps - 1)
            a = a1 + (a2 - a1) * p
            x = cx + abs(radius) * math.cos(math.radians(a))
            y = cy + abs(radius) * math.sin(math.radians(a))
            self.goto(x, y)
        if radius >= 0:
            self.setheading(self._h + extent)
        else:
            self.setheading(self._h - extent)

    seth = setheading
    pd = down = pendown
    pu = up = penup
    pos = position
    fd = forward
    bk = back = backward
    rt = right
    lt = left
