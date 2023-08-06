from mcdreforged.api.types import ServerInterface
from player_command_plus import  custom_callback
def SetGlobals(server :ServerInterface,config):
    global serverConfig
    serverConfig = config
    global customCommands
    customCommands = {}