import random
import string


class Robot(object):
    names = []

    def __init__(self):
        
        self._name = self.create_random_name()

        while self._name in Robot.names:
            self._name = self.create_random_name()
        Robot.names.append(self._name)

    @property
    def name(self):
        return self._name
    
    def reset(self):
        self.__init__()

    def create_random_name(self):
        return random.choice(string.ascii_uppercase) \
            + random.choice(string.ascii_uppercase) \
            + str(random.randint(100,999))