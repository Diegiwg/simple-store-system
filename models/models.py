from dataclasses import dataclass
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy_serializer import SerializerMixin


@dataclass
class Base(DeclarativeBase, SerializerMixin):
    pass


@dataclass
class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )
    brand: Mapped[str] = mapped_column()
    reference: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()

    stock: Mapped["Stock"] = relationship(cascade="all, delete-orphan")


@dataclass
class Stock(Base):
    __tablename__ = "stock"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
