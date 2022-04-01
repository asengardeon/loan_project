class ParamMissedException(Exception):
    param_name: str
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.param_name = args[0]


    def get_param(self):
        return self.param_name

