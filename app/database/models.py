from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()


class Users(Base):
  __tablename__ = 'blank'

