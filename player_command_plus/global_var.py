from mcdreforged.api.types import ServerInterface
serverConfig = dict({})
vaild_action_dict =set({})
def SetGlobals(server :ServerInterface,config:dict):
    global serverConfig
    serverConfig = config
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