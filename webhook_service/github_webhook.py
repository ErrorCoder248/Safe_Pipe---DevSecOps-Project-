from fastapi import FastAPI, Request
from .db import Base, engine, SessionLocal
from .models import WebhookEvent

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.post("/webhook/github")
async def github_webhook(request: Request):
    payload = await request.json()
    headers = request.headers

    repo = payload.get("repository", {}).get("full_name", "unknown")
    event_type = headers.get("X-GitHub-Event", "unknown")

    db = SessionLocal()
    event = WebhookEvent(
        repo=repo,
        event_type=event_type,
        payload=str(payload)
    )
    db.add(event)
    db.commit()
    db.refresh(event)

    return {"status": "success", "event_id": event.id}
