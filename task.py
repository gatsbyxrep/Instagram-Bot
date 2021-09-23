class Task:
    def __init__(self, serviceType, taskType, link, seconds):
        # 1 - vk, 2 - fb, 3 - inst, 4 - yt, 5- twitter, 7 - ok, 8 - tg
        self.serviceType = serviceType
        # 0 - all, 1 - like, 2 - repost, 3- subscribe, 4 - comment, 8 - vote
        self.taskType = taskType 
        self.link = link
        self.seconds = seconds
    def print(self):
        print(self.serviceType, self.taskType, self.link, self.seconds, sep = ' ')