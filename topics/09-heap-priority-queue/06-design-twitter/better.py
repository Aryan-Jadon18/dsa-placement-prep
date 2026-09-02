# Per-user tweet lists, concatenate relevant lists and sort — Time: getNewsFeed O(k*m log(k*m)), Space: O(T+F)
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(list)  # userId -> list of (timestamp, tweetId)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        relevant_users = self.following[userId] | {userId}
        combined = []
        for u in relevant_users:
            combined.extend(self.user_tweets[u])
        combined.sort(key=lambda t: t[0], reverse=True)
        return [tweetId for _, tweetId in combined[:10]]

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
