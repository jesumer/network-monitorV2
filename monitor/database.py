from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class PacketLog(Base):
    __tablename__ = 'packet_logs'

    id = Column(Integer, primary_key=True)
    source_ip = Column(String)
    destination_ip = Column(String)
    protocol = Column(String)
    length = Column(String)


def init_db():
    Base.metadata.create_all(engine)