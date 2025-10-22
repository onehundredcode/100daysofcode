# A simple design for a chat server using object-oriented principles.

# Common Challenges Addressed:
# 1. Class Relationships: User, Message, ChatServer - defining clear relationship and designing the responsibilities of each class.
# 2. Data Flow: Managing user registration, message sending, and retrieval.
# 3. Data Integrity: Ensuring messages are sent and received by valid users.
# 4. Extensibility: Allowing for future features like group chats, media messages, etc.


class User:
    """
    Represents a single user in the chat server.

    Attributes:
        user_id (int): Unique identifier for the user.
        username (str): The user's display name.
        friends (set): Set of user IDs representing the user's friends.
    """
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.friends = set()

    # Method to manage friends
    def add_friend(self, friend_user_id):
        self.friends.add(friend_user_id)

    # Method to remove a friend
    def remove_friend(self, friend_user_id):
        self.friends.discard(friend_user_id)

class Message:
    """
    Represents a single message in the chat server.

    Attributes:
        message_id (int): Unique identifier for the message.
        sender_id (int): User ID of the sender.
        receiver_id (int): User ID of the receiver.
        content (str): The message content.
        timestamp (str): The time the message was sent.
    """
    def __init__(self, message_id, sender_id, receiver_id, content, timestamp):
        self.message_id = message_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = timestamp


class ChatServer:
    """
    Represents the chat server managing users and messages.

    Attributes:
        users (dict): A dictionary mapping user IDs to User objects.
        messages (list): A list of Message objects.
        next_user_id (int): The next available unique user ID.
        next_message_id (int): The next available unique message ID.
    """
    def __init__(self):
        self.users = {}  
        self.messages = [] 
        self.next_user_id = 1
        self.next_message_id = 1

    """
    Method to register a new user

    Returns:
        int: The user ID of the newly registered user.
    """
    def register_user(self, username):
        user = User(self.next_user_id, username)
        self.users[self.next_user_id] = user
        self.next_user_id += 1
        return user.user_id

    """
    Method to send a message from one user to another

    Returns:
        int: The message ID of the newly sent message.
    """
    def send_message(self, sender_id, receiver_id, content, timestamp):
        if sender_id not in self.users or receiver_id not in self.users:
            raise ValueError("Sender or receiver does not exist")
        message = Message(self.next_message_id, sender_id, receiver_id, content, timestamp)
        self.messages.append(message)
        self.next_message_id += 1
        return message.message_id

    """
    Method to retrieve messages between two users
    
     Returns:
        list: A list of Message objects exchanged between the two users.
    """
    def get_messages(self, user_id1, user_id2):
        convo_messages = [msg for msg in self.messages if 
                          (msg.sender_id == user_id1 and msg.receiver_id == user_id2) or 
                          (msg.sender_id == user_id2 and msg.receiver_id == user_id1)]
        return convo_messages

    """
    Method to add a friend relationship between two users

    Returns:
        None
    """
    def add_friend(self, user_id, friend_user_id):
        if user_id in self.users and friend_user_id in self.users:
            self.users[user_id].add_friend(friend_user_id)
            self.users[friend_user_id].add_friend(user_id)
        else:
            raise ValueError("One or both users do not exist")

    """
    Method to remove a friend relationship between two users
    
     Returns:
        None
    """
    def remove_friend(self, user_id, friend_user_id):
        if user_id in self.users and friend_user_id in self.users:
            self.users[user_id].remove_friend(friend_user_id)
            self.users[friend_user_id].remove_friend(user_id)
        else:
            raise ValueError("One or both users do not exist")


