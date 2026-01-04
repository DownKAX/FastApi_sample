from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from datetime import datetime

Base = declarative_base()

# Таблицы можно создать с помощью миграций alembic без каких-либо лишних строк в коде

class Example(Base):
  __tablename__ = 'example'
  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
  username: Mapped[str] = mapped_column(unique=True, nullable=False)
  register_time: Mapped[datetime] = mapped_column(unique=False, nullable=False)
  item_id: Mapped[int] = mapped_column(ForeignKey('example_items.id', ondelete='SET NULL', onupdate='CASCADE'), unique=False, nullable=False) # RESTRICT(у аргумента ondelete) Запрещает удаление родительской записи, если существуют дочерние.

class ExampleItems(Base):
    __tablename__ = 'example_items'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)