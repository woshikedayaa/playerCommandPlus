from mcdreforged.api.types import ServerInterface
def SetGlobals(server :ServerInterface,config):
    global Server
    Server = server
    global serverConfig
    serverConfig = config