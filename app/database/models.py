from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from datetime import datetime

Base = declarative_base()

# Таблицы можно создать с помощью миграций alembic без каких-либо лишних строк в коде

class Users(Base):
  __tablename__ = 'users'
  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
  username: Mapped[str] = mapped_column(unique=True, nullable=False)
  password: Mapped[str] = mapped_column(unique=False, nullable=False)
  register_time: Mapped[datetime] = mapped_column(unique=False, nullable=False)
