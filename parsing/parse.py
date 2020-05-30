class Parser:

    def __init__(self, console):
        self._console = console

    def command(self, message):

        split = message.split(' ')

        command = split[0]

        if command == 'HELP':
            self.help()

    def help(self):

        self._console.push("this is a help message.")




