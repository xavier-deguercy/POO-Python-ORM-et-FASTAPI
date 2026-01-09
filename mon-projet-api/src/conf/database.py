from sqlmodel import create_engine

# connextion string : mysql+pymysql


from sqlmodel import create_engine

sqlite_url = "sqlite:///./database.db"
engine = create_engine(sqlite_url, echo=True)
