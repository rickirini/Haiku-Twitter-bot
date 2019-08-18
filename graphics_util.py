# graphics_util.py


def is_within(point, rect):
    """takes a point and a rectangle as argument and
    returns true when certain point is within a rectangle and false if not"""
    x1 = rect.getP1().getX()
    y1 = rect.getP1().getY()
    x2 = rect.getP2().getX()
    y2 = rect.getP2().getY()
    if (x1 > x2):
        (x1, x2) = (x2, x1)
    if (y1 > y2):
        (y1, y2) = (y2, y1)
    return ((x1 < point.getX() < x2) and (y1 < point.getY() < y2))
