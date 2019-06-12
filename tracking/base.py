from collections import namedtuple

Path = namedtuple("Path", [
    "label",    # type label
    "id",       # box id
    "boxes",    # dict of frame -> boxes
])

Box = namedtuple("Box", [
    "xtl",
    "ytl",
    "xbr",
    "ybr",
    "frame",
    "generated"
])
class Online:
    def track(self, pathid, start, stop, basepath, paths):
        raise NotImplementedError("Must implement the tracking method")

class Bidirectional:
    def track(self, pathid, start, stop, basepath, paths):
        raise NotImplementedError("Must implement the tracking method")

class MultiObject:
    def track(self, start, stop, basepath, paths):
        raise NotImplementedError("Must implement the tracking method")
