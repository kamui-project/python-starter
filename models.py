from datetime import datetime, timezone

from extensions import db


class Greeting(db.Model):
    __tablename__ = "greetings"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<Greeting {self.id}: {self.message}>"
