
class Usuario:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


class Postagem:
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body