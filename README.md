# cross_poster

A lightweight Python service to automatically cross-post updates from an RSS/Atom feed to social platforms like Bluesky and Mastodon, with optional manual approval via a push notification.

## Features

- Monitors a specified RSS/Atom feed for new entries
- Automatically posts new entries to Bluesky and Mastodon
- Sends a push notification containing a preformatted X (Twitter) intent link for quick manual approval
- Maintains state to avoid duplicate postings
- Runs as a Docker container for easy deployment

## Tech Stack

- Python 3.12 (using `python:3.12-slim` base image)
- Libraries: `feedparser`, `atproto` (Bluesky client), `mastodon.py`, `requests`
- Containerization: Docker, Docker Compose

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your system
- Access credentials for Bluesky and/or Mastodon if you want to enable posting
- A push notification service webhook (e.g., Pushover) if you want manual approval notifications

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

3. Start the service:

```bash
docker-compose up --build -d
```

4. Logs can be viewed with:

```bash
docker-compose logs -f
```

## Project Structure

```
├── app/
│   └── run.py          # Main application script
├── Dockerfile          # Docker image definition
└── docker-compose.yaml # Service orchestration and environment config
```

- `app/run.py` contains the main logic for polling the feed, posting to social platforms, and sending push notifications.
- `Dockerfile` defines the Python environment and dependencies.
- `docker-compose.yaml` configures the container, environment variables, volume mounts, and restart policy.

## Future Work / Roadmap

- Add support for more social platforms or notification services
- Improve error handling and logging
- Add configuration for polling interval
- Implement more granular state management to handle feed entry updates or deletions
- Provide a web interface for configuration and monitoring
- Add tests and CI pipeline

---

This project assumes the user has basic familiarity with Docker and environment variable configuration. The service is designed for simplicity and extensibility.
