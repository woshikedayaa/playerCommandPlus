from mcdreforged.api.types import ServerInterface
def SetGlobals(server :ServerInterface,config):
    global serverConfig
    serverConfig = config
    global customCommand
    customCommand = {}