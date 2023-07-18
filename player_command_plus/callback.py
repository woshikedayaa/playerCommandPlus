from player_command_plus import globalVar
from mcdreforged.api.types import CommandSource
import minecraft_data_api as api
from mcdreforged.api.all import *
from player_command_plus import utils

@new_thread('PlayerCommandPlus')
def OperateBots(source:CommandSource,ctx):
    if source.is_player==False:
        source.reply("只有玩家可使用")
        return
    action:str = ctx["action"]
    botName = ctx["name"]
    server = source.get_server()
    #处理假人列表
    BotList = []
    #初始化假人列表
    Index = botName.find("[")
    if Index>0:
        #检测是否完整括号
        if utils.CheckBrackets(botName[Index:len(botName)])==False:
            source.reply("不完整的括号")
            return
        
        ranges = botName[Index+1:-1].split("-")
        start = int(ranges[0])
        end = int(ranges[1])+1
        
        for i in range(end-start):
            BotList.append(botName[:Index]+str(i+start))
    else:
        BotList.append(botName)
    
    #处理下action
    actionArray = action.split(".")
    
    if actionArray[0] in globalVar.customCommand:
        #这里处理插件自定义的命令
        return
    else:
        #生成假人
        if action == "spawn":
            #只有生成假人获取坐标才有意义
            # pos = GetPlayerLocation(source.player).get_return_value(block=True)
            # dimesion = GetPlayerDimesion(source.player).get_return_value(block=True)
            pos = GetPlayerLocation(source.player)
            dimesion = GetPlayerDimesion(source.player)
            gamemode = ["survival","creative","adventure","spectator"][GetPlayerGamemode(source.player)]
            #print(pos)
            for elem in BotList:
                #提升效率(偷懒)不弄facing了
                #报错让他自己憋去吧
                server.execute("player {} spawn at {} {} {} facing 0 0 in {} in {}".format(elem,pos.x,pos.y,pos.z,dimesion,gamemode))
        else:
            #把action变成carpet看得懂的样子
            action = action.replace("."," ",-1)
            for elem in BotList:
                #报错让他自己憋去吧
                server.execute("player {} {}".format(elem,action))
            return
    return

def Help(source:CommandSource):
    source.reply(
'''
------------PlayerCommandPlus
1-!!pcp help 显示该消息
2-!!pcp name[范围] [操作]
  例1-!!pcp hello spawn 
  召唤名为hello假人
  例2-!!pcp hello[0-2] spawn 
  召唤名为 hello0,hello1,hello2的假人
  例3-!!pcp hello[0-2] jump.interval.10
  让hello0,hello1,hello2假人每10gt跳一次
  -----------------------------''')


def GetPlayerLocation(name):
    pos = api.get_player_coordinate(name)
    return pos

def GetPlayerDimesion(name):
    #return ["minecraft:overworld","minecraft:the_end","minecraft:the_nether"][api.get_player_dimension(name)]
    dimesion = api.get_player_info(name,"Dimension")
    return dimesion

def GetPlayerGamemode(name):
    return api.get_player_info(name,"playerGameType")