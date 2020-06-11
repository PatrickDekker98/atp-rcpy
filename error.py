class error():
    def __init__(self, error_msg : str):
        self.error_msg = error_msg

    def __str__(self):
        return 'error(%s)' % self.error_msg

    def __repr__(self):
        return self.__str__()
