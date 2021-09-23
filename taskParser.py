import json
from task import Task
class TaskParser:
    # Парсит строку с заданиями
    def parseTasksString(self, jsonString):
        dict = json.loads(jsonString)
        items = dict['data']['items']
        tasksId = []
        for item in items:
            tasksId.append(item['id'])
        return tasksId

    # Парсит строку для выполнения задания и возвращает объект задания
    def parseDoTaskString(self, jsonString):
        dict = json.loads(jsonString)
        if(dict['success'] == True):
            data = dict['data']
            return Task(data['service_type'], data['task_type'], data['url'], data['seconds'])
        return None
    def parseCheckTaskString(self, jsonString):
        dict = json.loads(jsonString)
        return dict['success']

