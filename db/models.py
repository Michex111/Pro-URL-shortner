from sqlalchemy.orm import Mapped, mapped_column

from db.session import Base

class URL(Base):
    """Database model for storing URL mappings."""
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    original_url: Mapped[str] = mapped_column(nullable=False)
    short_url: Mapped[str] = mapped_column(unique=True, default="")