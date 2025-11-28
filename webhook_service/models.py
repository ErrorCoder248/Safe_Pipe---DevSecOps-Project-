from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .db import Base

class WebhookEvent(Base):
    __tablename__ = "webhook_events"

    id = Column(Integer, primary_key=True, index=True)
    repo = Column(String(255))
    event_type = Column(String(50))
    payload = Column(Text)
    status = Column(String(50), default="received")
    received_at = Column(DateTime(timezone=True), server_default=func.now())
