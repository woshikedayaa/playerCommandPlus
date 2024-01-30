from mcdreforged.api.types import ServerInterface
from player_command_plus import  custom_callback
def SetGlobals(server :ServerInterface,config:dict):
    global serverConfig
    serverConfig:dict = config