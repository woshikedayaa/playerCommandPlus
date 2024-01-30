from mcdreforged.api.types import ServerInterface
from player_command_plus import  custom_callback
def SetGlobals(server :ServerInterface,config:dict):
    global serverConfig
    serverConfig:dict = config
    global vaild_action_dict
    vaild_action_dict={
        "attack",
        "dismount",
        "drop",
        "dropStack",
        "hotbar",
        "jump",
        "kill",
        "look",
        "mount",
        "move",
        "shadow",
        "sneak",
        "spawn",
        "sprint",
        "stop",
        "swapHands",
        "turn",
        "unsneak",
        "unsprint",
        "use"
    }