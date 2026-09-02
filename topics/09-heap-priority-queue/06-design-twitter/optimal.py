# Max-heap merge of per-user tweet lists (k-way merge) — Time: getNewsFeed O(k log k), Space: O(T+F)
import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(list)  # userId -> list of (timestamp, tweetId), append order
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        relevant_users = self.following[userId] | {userId}

        heap = []
        for u in relevant_users:
            tweets = self.user_tweets[u]
            if tweets:
                idx = len(tweets) - 1  # start from most recent
                ts, tweetId = tweets[idx]
                heapq.heappush(heap, (-ts, tweetId, u, idx))

        result = []
        while heap and len(result) < 10:
            neg_ts, tweetId, u, idx = heapq.heappop(heap)
            result.append(tweetId)
            if idx > 0:
                ts, next_tweetId = self.user_tweets[u][idx - 1]
                heapq.heappush(heap, (-ts, next_tweetId, u, idx - 1))

        return result

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
