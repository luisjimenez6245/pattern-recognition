class BaseModel():

    def __init__(self, **args):
        super().__init__()
        self.__dict__.update(args)