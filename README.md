# cross_poster

A lightweight Python service that monitors an RSS/Atom feed and automatically cross-posts new entries to social platforms such as Bluesky and Mastodon. It also supports sending a push notification with a preformatted Twitter intent link for optional manual approval.

## Features

- Continuously monitors a specified RSS/Atom feed for new entries
- Automatically posts new entries to Bluesky and Mastodon if configured
- Sends a push notification containing a Twitter intent link to enable manual approval
- Maintains posting state to prevent duplicate posts
- Runs as a Docker container for straightforward deployment and management

## Tech Stack

- Python 3.12 (using the `python:3.12-slim` Docker base image)
- Python libraries: `feedparser`, `atproto` (Bluesky client), `mastodon.py`, `requests`
- Containerization with Docker and Docker Compose

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your system
- Optional: Access credentials for Bluesky and/or Mastodon
- Optional: Push notification service webhook (e.g., Pushover) for manual approval notifications

### Installation & Running

1. Clone the repository:

```bash
git clone https://github.com/justin-napolitano/cross_poster.git
cd cross_poster
```

2. Configure environment variables in `docker-compose.yaml`:

- `SITE_FEED_URL`: URL of the RSS/Atom feed to monitor
- `STATE_FILE`: Path to the JSON file to store state (default `/data/state.json`)
- Bluesky credentials (optional): `BSKY_HANDLE`, `BSKY_PASSWORD`
- Mastodon credentials (optional): `MASTODON_BASE_URL`, `MASTODON_ACCESS_TOKEN`
- Push notification webhook (optional): `PUSH_WEBHOOK`, `PUSH_TOKEN`, `PUSH_USER`

3. Build and start the service:

```bash
docker-compose up --build -d
```

4. To view logs:

```bash
docker-compose logs -f
```

## Project Structure

```
├── app/
│   └── run.py          # Main application script
├── Dockerfile          # Docker image definition
└── docker-compose.yaml # Service orchestration and environment configuration
```

- `app/run.py` contains the main logic for polling the feed, posting to social platforms, and sending push notifications.

## Future Work / Roadmap

- Add support for additional social platforms beyond Bluesky and Mastodon
- Implement more robust error handling and logging
- Provide configuration options for polling intervals and batch sizes
- Add unit and integration tests
- Support multiple feeds and customizable post formatting
- Improve security around credential management
