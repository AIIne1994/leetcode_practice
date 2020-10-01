class RecentCounter:
    def __init__(self):
        self.__requests = []


    def ping(self, t):
        self.__requests.append(t)
        minimum = t - 3000
        while self.__requests[0] < minimum:
            self.__requests.remove(self.__requests[0])
        return len(self.__requests)

if __name__ == '__main__':
    pass
