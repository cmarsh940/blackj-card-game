class Card(object):
    def __init__(self, face, value, suite):
        self.value = value
        self.face = face
        self.suite = suite

    def __str__(self):
        return "Face: {}, Value: {} Suite: {}".format(
            self.face,
            self.value,
            self.suite,
        )