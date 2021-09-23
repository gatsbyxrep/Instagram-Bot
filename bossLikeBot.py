import requests, json
from taskParser import TaskParser
from instagramBot import InstagramBot
from time import sleep


class BossLikeBot:
    def __init__(self, key, version):
        self.key = key
        self.version = version
        self.apiUrl = 'https://api-public.bosslike.ru'
        self.headers = {'X-Api-Key':self.key}
        self.falseCount = 0
        self.taskParser = TaskParser()
        self.instagramBot = InstagramBot('login', 'password')

    # Возаращает ответ сервера на GET запрос    
    def sendRequestGet(self, url, data):
        request = self.apiUrl + '/' + self.version + '/' + url
        result = requests.get(request, params = data, headers = self.headers)
        return result.text

    # Возвращает ID заданий
    def getTasks(self, serviceType, taskType):
        data = {'service_type':serviceType, 'task_type':taskType} 
        result = self.sendRequestGet('bots/tasks/', data)
        return self.taskParser.parseTasksString(result)
    
    def doTask(self, taskId):
         task = self.taskParser.parseDoTaskString(self.sendRequestGet('bots/tasks/' + taskId + '/do/', {}))
         if(task != None):
             task.print()
             sleep(task.seconds)
             self.instagramBot.putLike(task.link)
             return True
         return False
    
    def checkTask(self, taskId):
        result = self.sendRequestGet('bots/tasks/' + taskId + '/check/', {})   
        print(self.taskParser.parseCheckTaskString(result))
     
    def doTasks(self, tasksId):
        for taskId in tasksId:
            if(self.doTask(taskId)):
                self.checkTask(taskId)            
        
            
    def run(self, serviceType, taskType, iterations):
        for i in range(iterations):
            self.doTasks(self.getTasks(serviceType, taskType))
        self.instagramBot.close()
        

def main():
    bossLikeBot = BossLikeBot("api-key", "v1")
    bossLikeBot.run('3', '1', 10000)
    
if __name__ == "__main__":
    main()
    
