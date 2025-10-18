class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
    # There are n people
    # Each person has unique id b/n 0 and n-1 
    # array watchVideos  and friends
    # watchedvideos[i]==>friends[i]  

        queue = deque()
        visited = set()

        queue.append(id)
        visited.add(id)
        current_level = level

        while queue and current_level > 0:
            for _ in range(len(queue)):
                friend_no = queue.popleft()
                for x in friends[friend_no]:
                    if x not in visited:
                        queue.append(x)
                        visited.add(x)
            current_level -= 1

        vid_set = defaultdict(int)
        for x in queue:
            for video in watchedVideos[x]:
                vid_set[video] += 1

        return sorted(vid_set.keys(), key=lambda key: (vid_set[key], key))



