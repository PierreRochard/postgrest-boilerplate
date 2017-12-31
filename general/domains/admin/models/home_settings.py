from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    text,
    UniqueConstraint
)
from sqlalchemy.dialects.postgresql import UUID

from general.database.base import Base


class HomeSettings(Base):
    __tablename__ = 'home_settings'
    __table_args__ = (UniqueConstraint('user_id',
                                       name='home_settings_unique_constraint'),
                      {'schema': 'admin'},
                      )

    id = Column(UUID,
                server_default=text('auth.gen_random_uuid()'),
                primary_key=True)

    headline = Column(String)
    sub_headline = Column(String)
    supporting_image = Column(String)

    user_id = Column(UUID,
                     ForeignKey('auth.users.id',
                                onupdate='CASCADE',
                                ondelete='CASCADE'),
                     nullable=False)
