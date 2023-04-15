import time

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def request_resource(self, resource):
        print(f"User {self.user_id} is requesting resource {resource}")
        time.sleep(1)
        print(f"User {self.user_id} has acquired resource {resource}")

class Minicomputer:
    def __init__(self, computer_id):
        self.computer_id = computer_id
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f"User {user.user_id} has logged on to Computer {self.computer_id}")

    def process_request(self, user, resource):
        print(f"Minicomputer {self.computer_id} is processing request from User {user.user_id} for resource {resource}")
        time.sleep(2)
        print(f"Minicomputer {self.computer_id} has processed request from User {user.user_id} for resource {resource}")

def main():
    # Create three Minicomputers
    minicomputer1 = Minicomputer(1)
    minicomputer2 = Minicomputer(2)
    minicomputer3 = Minicomputer(3)

    # Create 3 users
    user1 = User(1)
    user2 = User(2)
    user3 = User(3)

    # Add users to minicomputers
    minicomputer1.add_user(user1)
    minicomputer1.add_user(user2)

    minicomputer3.add_user(user3)

    # Simulate user requests and Minicomputer processing

    # Request for a resource in local computer
    user1.request_resource("database1")
    minicomputer1.process_request(user1, "database1")

    # Request for a shared resource in remote computer
    user2.request_resource("database2")
    minicomputer2.process_request(user2, "database2")

    user3.request_resource("database2")
    minicomputer2.process_request(user3, "database2")

if __name__ == '__main__':
    main()

