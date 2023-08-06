# from player_command_plus import global_var

# class Task:
#     # Second
#     Duracation = 0
#     def __init__(self,time:int,actionArray,source,bots) -> None:
#         Task.Duracation = int(time)
#         self.Action = actionArray
#         self.source = source
#         self.bots = bots
    
#     def Run(self):
#         print("执行一次")
#         if len(self.Action)==0:
#             return
#         fullAction = ""
#         for s in self.Action:
#             fullAction +=" {}".format(s)
#         server = self.source.get_server()
#         for name in self.Action:
#             server.execute("player {}{}".format(name,fullAction))

#     def checkSelf(self):
#         if Task.Duracation == 0:
#             self.Run()
#             return True
#         return False

# def After(source,ctx,botList,actionArray):
#     global_var.TaskQueue.append(Task(actionArray[1],actionArray[2:],source,botList))