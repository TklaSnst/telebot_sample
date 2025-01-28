from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int]
    username: Mapped[str] = mapped_column(nullable=False)


class Item(Base):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    dsc: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int] = mapped_column()


class Cart(Base):
    __tablename__ = 'carts'
    deal_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    uid: Mapped[int] = mapped_column(ForeignKey(User.id), nullable=False)
    item_id: Mapped[int] = mapped_column(ForeignKey(Item.id), nullable=False)
