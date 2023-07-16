from player_command_plus import globalVar
from mcdreforged.api.types import CommandSource

def SpawnBots(source:CommandSource,ctx):
    if len(ctx)<4:
        globalVar.Server.say("参数不足!")
        return
    if ctx["count"]<0 or ctx["count"]>15:
        globalVar.Server.say("参数错误!")
        return
    '''解析地址参数'''
    pos = ctx["location"][1:len(ctx["location"])-1].split(",")
    if ctx["count"] <=1:
        globalVar.Server.execute("player "+str(ctx["name"])+" spawn "+"at {} {} {} ".format(pos[0],pos[1],pos[2])+"facing 0 0 in "+{
            "end":"minecraft:the_end",
            "nether":"minecraft:the_nether",
            "overworld":"minecraft:overworld"
        }[ctx["dimension"]]+" in survival")
        return
    for i in range(ctx["count"]):
        globalVar.Server.execute("player "+str(ctx["name"])+str(i)+" spawn "+"at {} {} {} ".format(pos[0],pos[1],pos[2])+"facing 0 0 in "+{
            "end":"minecraft:the_end",
            "nether":"minecraft:the_nether",
            "overworld":"minecraft:overworld"
        }[ctx["dimension"]]+" in survival")
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