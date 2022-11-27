from ..repository.authorRepository import AuthorRepository

class BasicService:
    def __init__(self):
        self.myAuthorRepository = AuthorRepository("mongodb://admin:admin@localhost:27017", "flask_api", "something")
        print("BasicService initialized")

    def insert_something(self, data):
        self.myAuthorRepository.insert_one(data)

    def get_something(self, id):
        return self.myAuthorRepository.find(id)
        