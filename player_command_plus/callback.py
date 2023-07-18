from player_command_plus import globalVar
from mcdreforged.api.types import CommandSource
import minecraft_data_api as api
from mcdreforged.api.all import *
import time
def SpawnBots(source,ctx):
    if source.is_player==False:
        return
    #time.sleep(0.5)
    if ctx["count"]<0 or ctx["count"]>15:
        globalVar.Server.say("数量过大或过小!")
        return
    #解析地址参数
    #pos = ctx["location"][1:len(ctx["location"])-1].split(",")
    # if len(globalVar.whoCall)==0:
    #     globalVar.Server.say("未知错误")
    #     globalVar.Server.logger.error("未知错误")
    #     return
    print(source)
    
    name = source.player
    location = GetPlayerLocation(name)
    dimension = GetPlayerDimesion(name)
    time.sleep(1)
    
    for i in range(ctx["count"]):
        print(i,location)
       #globalVar.Server.execute("player {}{} spawn at {} {} {} facing 0 0 in {} in survival".format(ctx["prefix"],str(i),location.x,location.y,location.z,dimension))
    return

def OperateBots(source,ctx):
    if len(ctx)<3:
        globalVar.Server.say("参数不足!")
        return
    if ctx["count"]<0:
        globalVar.Server.say("参数错误!")
        return
    for i in range(ctx["count"]):
        globalVar.Server.execute("player "+ctx["name"]+str(i)+" "+ctx["action"][1:len(ctx["action"])-1])
    return

def Help():
    globalVar.Server.say("PCP使用指南")
    globalVar.Server.say("!!pcp spawn <数量> <名字> <维度> <坐标>")
    globalVar.Server.say("维度:overworld-主世界:nether-地狱:end-末地")
    globalVar.Server.say("例:!!pcp spawn 10 hello overworld [0,100,0]")
    globalVar.Server.say("该指令将会在主世界[0,100,0]召唤10个 hello开头的假人")
    globalVar.Server.say("!!pcp operate <数量> <名字> <操作>")
    globalVar.Server.say("例:!!pcp operate 10 hello [kill]")
    globalVar.Server.say("该指令会把10个hello开头的假人下线")

@new_thread('PlayerCommandPlus')
def GetPlayerLocation(name):
    return api.get_player_coordinate(name)

@new_thread('PlayerCommandPlus')
def GetPlayerDimesion(name):
    return ["minecraft:overworld","minecraft:the_end","minecraft:the_nether"][api.get_player_dimension(name)]