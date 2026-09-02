# Global tweet list, filter + sort on every feed request — Time: getNewsFeed O(T log T), Space: O(T+F)
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = []  # list of (timestamp, userId, tweetId)
        self.following = defaultdict(set)  # userId -> set of followed userIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((self.time, userId, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        relevant = self.following[userId] | {userId}
        matches = [t for t in self.tweets if t[1] in relevant]
        matches.sort(key=lambda t: t[0], reverse=True)
        return [tweetId for _, _, tweetId in matches[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


if __name__ == "__main__":
    tw = Twitter()
    tw.postTweet(1, 5)
    print("Expected: [5]  Actual:", tw.getNewsFeed(1))
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    print("Expected: [6, 5]  Actual:", tw.getNewsFeed(1))
    tw.unfollow(1, 2)
    print("Expected: [5]  Actual:", tw.getNewsFeed(1))

    tw2 = Twitter()
    tw2.postTweet(1, 1)
    tw2.postTweet(1, 2)
    tw2.postTweet(1, 3)
    print("Expected: [3, 2, 1]  Actual:", tw2.getNewsFeed(1))

    tw3 = Twitter()
    tw3.follow(1, 1)
    tw3.postTweet(1, 9)
    print("Expected: [9]  Actual:", tw3.getNewsFeed(1))
