from player_command_plus import global_var
from mcdreforged.api.types import CommandSource
from mcdreforged.api.all import *
from player_command_plus import utils
from player_command_plus import custom_callback

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
        if len(ranges)!=2:
            source.reply("数字过多或过少")
            return
        start = int(ranges[0])
        end = int(ranges[1])+1

        for i in range(end-start):
            BotList.append(botName[:Index]+str(i+start))
    else:
        if botName.find("]")>0:
            source.reply("名称错误")
            return
        BotList.append(botName)
    
    #处理下action
    actionArray = action.split(".")
    #生成假人
    # 2024-1-30 加一个set就能让用户知道错了
    if actionArray[0] == "spawn":
        #只有生成假人获取坐标才有意义
        pos = utils.GetPlayerLocation(source.player)
        dimesion = utils.GetPlayerDimesion(source.player)
        Rotation = utils.GetPlayerRotation(source.player)
        gamemode = ["survival","creative","adventure","spectator"][utils.GetPlayerGamemode(source.player)]
        
        for elem in BotList:
            #报错让他自己憋去吧
            spawnStr = "player {} spawn at {} {} {} facing {} {} in {} in {}".format(elem,pos.x,pos.y,pos.z,Rotation[0],Rotation[1],dimesion,gamemode)
            server.execute(spawnStr)
    else:
        #把action变成carpet看得懂的样子
        if actionArray[0] not in global_var.vaild_action_dict:
            source.reply("未知的action")
            return
        action = action.replace("."," ",-1)
        prefix = "" if global_var.serverConfig["prefix"]=="#none" else global_var.serverConfig["prefix"]
        suffix = "" if global_var.serverConfig["suffix"]=="#none" else global_var.serverConfig["suffix"]
        for elem in BotList:
            #报错让他自己憋去吧
            
            server.execute("player {} {}".format(prefix+elem+suffix,action))
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