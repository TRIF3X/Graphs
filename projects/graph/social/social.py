import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            # add friendship to both users
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name) #creates a user in self.users using the lastID created
        self.friendships[self.lastID] = set() #creates a set for the user in self.friendships that will hold all connected friends

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """

        # perform check if we can populate graph
        if numUsers < avgFriendships:
            print('need more users than friendships')

        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for x in range(0,numUsers):
            self.addUser(x+1)

        # Create friendships
        friendship = []
        friends_left = numUsers * avgFriendships
        total_friends = numUsers * avgFriendships

        for i in range(numUsers):
            if friends_left > 0:
                friends = round(random.random() * (avgFriendships*2))
                friends_left -= friends
                friendship.append(friends)
            elif friends <= 0:
                friendship.append(0)

        # ensure we get to the total number of friendships we need
        while sum(friendship) < total_friends:
            for i in range(len(friendship)):
                if friends_left:
                    friendship[i] += 1
                    friends_left -= 1

        while sum(friendship) > total_friends:
            for j in range(len(friendship)):
                if friends_left:
                    friendship[j] -= 1
                    friends_left += 1

        for user in self.users:
            if len(friendship) > user - 1:
                if friendship[user - 1]:
                    for new_friend_index in range(len(friendship)):
                        if friendship[new_friend_index] == friendship[user - 1]:
                            pass
                        elif friendship[new_friend_index] and friendship[user - 1]:
                            if new_friend_index+1 not in self.friendships[user]:
                                self.addFriendship(user, new_friend_index+1)
                                friendship[new_friend_index] -= 1
                                friendship[user -1] -= 1
 


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
