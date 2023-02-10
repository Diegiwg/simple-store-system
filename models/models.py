from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    pass


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

    in_stock: Mapped["Stock"] = relationship(back_populates="product")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, brand={self.brand}, reference={self.reference}, price={self.price})>"


class Stock(Base):
    __tablename__ = "stock"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped["Product"] = relationship(back_populates="in_stock")

    def __repr__(self):
        return f"<Stock(id={self.id}, quantity={self.quantity}, product_id={self.product_id})>"
