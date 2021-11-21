class chathon:
    def __init__(self, bot_name:str, prefix:str):
        cmd = input("You : ")
        self.cmd = cmd
        self.prefix = prefix
        self.bot_name = bot_name

    def command(self):
        def decorator(func, **kwargs):
            if self.cmd.startswith(f"{self.prefix}{func.__name__}"):
                response = func(**kwargs)
                return response
            else:
                raise TypeError("Command not found")

        return decorator

    def send(self, message:str):
        print(f"{self.bot_name} [BOT] : {message}")
