# app/run.py (trimmed)
import os, json, time, feedparser, urllib.parse, requests
from datetime import datetime, timezone
from atproto import Client  # Bluesky
from mastodon import Mastodon

FEED = os.environ["SITE_FEED_URL"]
STATE_PATH = os.getenv("STATE_FILE", "/data/state.json")

def load_state():
    try: return json.load(open(STATE_PATH))
    except: return {"last_ids": []}

def save_state(s): json.dump(s, open(STATE_PATH,"w"))

def post_bsky(text):
    h, pw = os.getenv("BSKY_HANDLE"), os.getenv("BSKY_PASSWORD")
    if not (h and pw): return
    c = Client(); c.login(h, pw); c.send_post(text)

def post_masto(text):
    base, tok = os.getenv("MASTODON_BASE_URL"), os.getenv("MASTODON_ACCESS_TOKEN")
    if not (base and tok): return
    m = Mastodon(api_base_url=base, access_token=tok)
    m.status_post(text)

def push_intent(text):
    url = "https://twitter.com/intent/tweet?text=" + urllib.parse.quote(text)
    # Example: Pushover (swap with your notifier)
    if os.getenv("PUSH_WEBHOOK"):
        requests.post(os.environ["PUSH_WEBHOOK"], data={
            "token": os.getenv("PUSH_TOKEN"),
            "user": os.getenv("PUSH_USER"),
            "message": url,
            "title": "Approve tweet?",
        })

def main():
    state = load_state()
    while True:
        d = feedparser.parse(FEED)
        for e in reversed(d.entries[:5]):  # newest last → post in order
            eid = getattr(e, "id", e.link)
            if eid in state["last_ids"]: continue
            title = e.title.strip()
            url = e.link
            text = f"{title} {url}"
            # post to free networks
            post_bsky(text)
            post_masto(text)
            # send X intent link for 1-tap approval
            push_intent(text)
            state["last_ids"].append(eid)
            save_state(state)
        time.sleep(300)

if __name__ == "__main__":
    main()
