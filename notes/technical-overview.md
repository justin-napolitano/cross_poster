---
slug: github-cross-poster-note-technical-overview
id: github-cross-poster-note-technical-overview
title: cross_poster
repo: justin-napolitano/cross_poster
githubUrl: https://github.com/justin-napolitano/cross_poster
generatedAt: '2025-11-24T18:34:11.057Z'
source: github-auto
summary: >-
  `cross_poster` is a lightweight Python service that monitors an RSS/Atom feed
  and automatically cross-posts new entries to Bluesky and Mastodon. It can also
  send push notifications for manual approval via Twitter.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

`cross_poster` is a lightweight Python service that monitors an RSS/Atom feed and automatically cross-posts new entries to Bluesky and Mastodon. It can also send push notifications for manual approval via Twitter.

### Key Features
- Monitors RSS/Atom feeds for new entries.
- Auto-posts to Bluesky and Mastodon.
- Sends push notifications with Twitter intent links.
- Prevents duplicate posts.
- Runs easily in a Docker container.

### Tech Stack
- **Python 3.12** with essential libraries: `feedparser`, `atproto`, `mastodon.py`, `requests`.
- **Docker** and **Docker Compose** for deployment.

### Getting Started
1. Clone the repo:
   ```bash
   git clone https://github.com/justin-napolitano/cross_poster.git
   cd cross_poster
   ```
2. Configure `docker-compose.yaml` for environment variables.
3. Start the service:
   ```bash
   docker-compose up --build -d
   ```
4. View logs:
   ```bash
   docker-compose logs -f
   ```

**Gotcha**: Make sure to set up your credentials for Bluesky and Mastodon if you plan to use those features.
