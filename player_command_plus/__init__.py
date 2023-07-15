from mcdreforged.api import command
import os
import json

from .callback import *
const ={
    "configFilePath":"config/player_command_plus.json",
}
config = {
        "prefix":"#none"
}
def on_load(server,info):
    GenerateConfigFile()
    config = ReadConfigFile()
    RegistCommand(server)

def GenerateConfigFile():
    if os.path.exists(const["configFilePath"]) == False:
        with open(const["configFilePath"],"x",-1) as file:
            file.write(json.dumps(config))
        return
    return

def ReadConfigFile():
    with open(const["configFilePath"],"r",-1) as file:
        config = json.loads(file.read())
        return config
    
def RegistCommand(server):
    b = command.SimpleCommandBuilder()
    '''command'''
    b.command("!!pcp spawn <name> <count>",callback.SpawnBots)
    '''//支持正则//'''
    b.command("!!pcp operate <name> <action>",callback.OperateBots)
    b.command("!!pcp list",callback.List)
    '''args'''
    b.arg("name",command.Text)
    b.arg("count",command.Integer)
    b.arg("action",command.Text)
    '''regist'''
    b.register(server)
    return