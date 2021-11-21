class chathon:
    def __init__(self, bot_name:str, prefix:str):
        cmd = input("You : ")
        self.cmd = cmd
        self.prefix = prefix
        self.bot_name = bot_name

    def command(self):
        def decorator(func):
            user_input = self.cmd
            prefix = self.prefix
            if prefix in user_input:
                get_cmd = user_input.replace(prefix, "")
                if func.__name__ in get_cmd:
                    response = func()
                    return response

            else:
                raise TypeError("Invalid Prefix")

        return decorator

    def send(self, message:str):
        print(f"{self.bot_name} [BOT] : {message}")
