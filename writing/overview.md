---
slug: github-cross-poster-writing-overview
id: github-cross-poster-writing-overview
title: 'Cross Poster: Automatically Share Your RSS Feeds'
repo: justin-napolitano/cross_poster
githubUrl: https://github.com/justin-napolitano/cross_poster
generatedAt: '2025-11-24T17:14:41.324Z'
source: github-auto
summary: >-
  I created **cross_poster** to help streamline sharing content across different
  social platforms. It’s a lightweight Python service designed to automatically
  post entries from an RSS/Atom feed to Bluesky and Mastodon. Plus, it sends out
  a push notification with a Twitter intent link, giving you the option to
  approve posts before they go live.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: writing
entryLayout: writing
showInProjects: false
showInNotes: false
showInWriting: true
showInLogs: false
---

I created **cross_poster** to help streamline sharing content across different social platforms. It’s a lightweight Python service designed to automatically post entries from an RSS/Atom feed to Bluesky and Mastodon. Plus, it sends out a push notification with a Twitter intent link, giving you the option to approve posts before they go live. 

## Why Does Cross Poster Exist?

Social media can make or break the visibility of content. Manually sharing new blog posts or updates across platforms is a pain, especially when you're managing multiple feeds. I wanted to automate this process without the complexity of heavyweight solutions. Cross poster monitors a designated RSS/Atom feed, handles new entries, and posts them to selected social channels. It cuts down the time spent sharing, letting creators focus more on their content.

## Core Features

Here’s what you can expect from cross_poster:

- **Continuous Monitoring:** Keeps tabs on your specified RSS/Atom feed for any new entries.
- **Cross-Posting:** Automatically shares new content to Bluesky and Mastodon as soon as it's detected.
- **Push Notifications:** Sends a preformatted Twitter intent link, enabling manual approval before posting.
- **State Management:** Tracks what’s been posted to avoid duplicates.
- **Dockerized:** Runs smoothly as a Docker container, making deployment dead easy.

## Tech Stack

Let’s dive into how I built it. Here’s the tech stack:

- **Python 3.12**: The core of the application, leveraging the `python:3.12-slim` Docker base.
- Essential libraries:
  - `feedparser` for easy RSS/Atom parsing.
  - `atproto` as the client for Bluesky.
  - `mastodon.py` to interact with Mastodon.
  - `requests` for HTTP requests.
- **Containerization**: Uses Docker and Docker Compose for seamless setup and management.

## Getting Started 

Ready to take it for a spin? Setting it up is pretty straightforward.

### Prerequisites

- You’ll need Docker and Docker Compose installed.
- If you want to automate cross-posting on Bluesky or Mastodon, grab those access credentials.
- For push notifications, you might want to set up a webhook using something like Pushover.

### Installation Steps

1. Clone the repo and dive in:
    ```bash
    git clone https://github.com/justin-napolitano/cross_poster.git
    cd cross_poster
    ```

2. Configure the `docker-compose.yaml` with your environment variables:
    - `SITE_FEED_URL`: Point this to your RSS/Atom feed.
    - `STATE_FILE`: Path for the JSON file that stores state (default is `/data/state.json`).
    - Bluesky optional creds: `BSKY_HANDLE`, `BSKY_PASSWORD`.
    - Mastodon optional creds: `MASTODON_BASE_URL`, `MASTODON_ACCESS_TOKEN`.
    - Push notification optional vars: `PUSH_WEBHOOK`, `PUSH_TOKEN`, `PUSH_USER`.

3. Build and run the service:
    ```bash
    docker-compose up --build -d
    ```

4. Check logs for any issues:
    ```bash
    docker-compose logs -f
    ```

## Project Structure

Here’s a quick rundown of the project structure:

```
├── app/
│   └── run.py          # Main application logic
├── Dockerfile          # Docker image instructions
└── docker-compose.yaml # Service orchestration and environment configs
```

The main logic lives in `app/run.py`, which handles polling the feed, posting to social platforms, and sending out those important push notifications.

## Key Design Decisions

While building cross_poster, I kept a few principles in mind:

- **Simplicity**: I avoided complexity in favor of a straightforward flow. If you can set up Docker, you can run this service.
- **Flexibility**: With the Docker setup, it’s easy to spin up or take down as needed. Plus, the optional features allow you to customize it based on your needs.
- **Manual Approval**: The push notification with a Twitter intent link gives users an extra layer of control, which is essential for maintaining brand voice and oversight.

## Future Work

I’m already dreaming up what’s next for cross_poster. Here’s what’s on my wishlist:

- **More Platforms**: It'd be nice to support more social networks to broaden reach.
- **Enhanced Error Handling**: I want to refine error management and logging to diagnose issues easier.
- **Custom Polling Options**: It would help to give users control over how often they want to check feeds.
- **Testing**: Implementing unit and integration tests to ensure the code remains robust.
- **Multiple Feeds**: Support for more than one feed, with options for customizing the format of posts.
- **Security Improvements**: Tightening up how credentials are managed.

## Closing Thoughts

Cross_poster has been a fun project to work on. It effectively automates a tedious part of sharing content while giving you control over how it gets posted. I’m eager to see where I can take it next.

For updates on cross_poster and other projects, connect with me on social media. You can find me on Mastodon, Bluesky, and Twitter/X. Let’s keep the conversation going!
