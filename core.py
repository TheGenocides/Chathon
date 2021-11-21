class Chathon:
    def __init__(self, bot_name:str, prefix:str):
        cmd = input("You : ")
        self.cmd = cmd
        self.prefix = prefix
        self.bot_name = bot_name

    def command(self):
        def decorator(func):
            prefix = self.prefix
            if prefix in self.cmd:
                if func.__name__ in self.cmd:
                    arguments = self.cmd.split(" ")[1:]
                    try:
                        response = func(*arguments)
                    except TypeError:
                        print("You put too much/less arguments")
                    else:    
                        return response

            else:
                raise TypeError("Invalid Prefix")

        return decorator

    def send(self, message:str):
        print(f"{self.bot_name} [BOT] : {message}")
