from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Category(Base):
    """Категория задач (работа, личное, учёба и т.д.)."""
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    color: Mapped[str | None] = mapped_column(String(7), nullable=True)  # HEX-цвет, например #FF5733
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    # Связь с владельцем
    owner: Mapped["User"] = relationship("User", back_populates="categories")
    # Связь один-ко-многим: одна категория — много задач
    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="category")
