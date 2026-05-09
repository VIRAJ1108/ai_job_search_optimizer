from backend.database.connection import engine
from backend.database.models import Base


def init_database():

    Base.metadata.create_all(bind=engine)

    print("Database tables created successfully!")


if __name__ == "__main__":

    init_database()