import minecraft_data_api as api

def CheckBrackets(str:str):
    stack = []
    for i in range(len(str)):
        if str[i]=="[":
            stack.append(i)
            continue
        elif str[i]=="]":
            if not stack:
                return False
            else:
                stack.pop()
                continue
    return len(stack) == 0


def GetPlayerLocation(name):
    pos = api.get_player_coordinate(name)
    return pos

def GetPlayerDimesion(name):
    #return ["minecraft:overworld","minecraft:the_end","minecraft:the_nether"][api.get_player_dimension(name)]
    dimesion = api.get_player_info(name,"Dimension")
    return dimesion

def GetPlayerGamemode(name):
    return api.get_player_info(name,"playerGameType")

def GetPlayerRotation(name):
    return api.get_player_info(name,"Rotation")