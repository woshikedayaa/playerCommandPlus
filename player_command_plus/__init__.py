from mcdreforged.api import command
from mcdreforged.api.types import PluginServerInterface,Info
import os
import json
from .callback import *
'''from .globalVar import '''
from .globalVar import *

const ={
    "configFilePath":"config/player_command_plus.json",
}
DefaultConfig = {
        "prefix":"#none"
}

def on_load(server:PluginServerInterface,old):
    GenerateConfigFile()
    SetGlobals(server,ReadConfigFile())
    RegistCommand(server)
    server.register_help_message("!!pcp","你的批量假人助手")

def on_info(server:PluginServerInterface,info:Info):
    # if info.is_player == True and "!!pcp " in info.content:
    #     globalVar.whoCall.append(info.player)
    #     print(globalVar.whoCall)
    return

def GenerateConfigFile():
    if os.path.exists(const["configFilePath"]) == False:
        with open(const["configFilePath"],"x",-1) as file:
            file.write(json.dumps(DefaultConfig))
        return
    return

def ReadConfigFile():
    with open(const["configFilePath"],"r",-1) as file:
        config = json.loads(file.read())
        return config
    
def RegistCommand(server):
    b = command.SimpleCommandBuilder()
    '''command'''
    b.command("!!pcp spawn <count> <prefix>",callback.SpawnBots)
    '''//支持正则//'''
    b.command("!!pcp operate <count> <prefix> <action>",callback.OperateBots)
    
    b.command("!!pcp help",callback.Help)
    b.command("!!pcp",callback.Help)
    '''args'''
    b.arg("prefix",command.Text)
    b.arg("count",command.Integer)
    b.arg("action",command.Text)
    '''regist'''
    b.register(server)
    return