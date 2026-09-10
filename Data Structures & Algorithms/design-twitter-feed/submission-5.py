class Twitter:

    def __init__(self):
        self.followid = {}
        self.post = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post.append([userId,tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for item in self.post:
            #print(item[0],self.followid)
            if self.followid != [] and userId in  self.followid and item[0] in self.followid[userId]:
                res.append(item[1])
            elif item[0] == userId:
                res.append(item[1])
        res.reverse()
        return res[:10]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followid:
            self.followid[followerId]= [followeeId]
        elif followeeId not in self.followid[followerId]:
            self.followid[followerId].append(followeeId) 
        #print(self.followid)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #print("follow",self.followid , followerId ,followeeId)
        if followeeId in self.followid[followerId]:
            self.followid[followerId].remove(followeeId)
    
        
