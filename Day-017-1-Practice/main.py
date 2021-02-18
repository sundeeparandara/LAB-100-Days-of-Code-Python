class User:
    def __init__(self,user_id,username):
        #print("New user being created")
        self.id = user_id
        self.username = username
        self.followers = 0 #default value on initialisation of object
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1
        print(f"{self.username} is following {user.username}")


user_1 = User("001","Sundeep")
user_2 = User("002","Angela")

print(user_1.followers)
print(user_2.followers)
user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)
user_2.follow(user_1)
print(user_1.followers)
print(user_2.followers)