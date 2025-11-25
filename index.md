---
slug: github-cross-poster
title: Automate Social Media Cross-Posting with cross_poster
repo: justin-napolitano/cross_poster
githubUrl: https://github.com/justin-napolitano/cross_poster
generatedAt: '2025-11-23T08:47:33.033983Z'
source: github-auto
summary: >-
  Learn how to implement cross_poster for automated social media updates from
  RSS feeds to Bluesky and Mastodon.
tags:
  - rss-feed
  - cross-posting
  - bluesky
  - mastodon
  - docker
  - python
  - rss
  - feedparser
  - automation
seoPrimaryKeyword: automated social media cross-posting
seoSecondaryKeywords:
  - rss feed automation
  - bluesky posting
  - mastodon integration
  - docker deployment
  - push notifications
seoOptimized: true
topicFamily: automation
topicFamilyConfidence: 0.95
topicFamilyNotes: >-
  The post focuses on automating cross-posting from RSS feeds to social media
  using a Python service containerized with Docker, matching well the
  'Automation' family description and example slugs.
kind: project
id: github-cross-poster
---

# cross_poster: Technical Overview and Implementation Notes

## Motivation and Problem Statement

Managing multiple social media accounts and keeping them up to date with content from a single source can be cumbersome. Manual cross-posting is inefficient and error-prone. This project addresses the need for an automated, lightweight service that monitors an RSS or Atom feed and posts new entries to social platforms without duplication. It also offers a mechanism for manual approval via push notifications, balancing automation with control.

## Architecture and Components

The core of cross_poster is a Python script (`app/run.py`) that runs an infinite loop to poll a configured RSS/Atom feed at fixed intervals (every 5 minutes). It uses the `feedparser` library to parse feed entries and compares them against a stored state to avoid reposting the same content.

Posting to social platforms is abstracted into separate functions:

- `post_bsky(text)`: Uses the `atproto` client to authenticate and post to Bluesky. Requires environment variables `BSKY_HANDLE` and `BSKY_PASSWORD`.
- `post_masto(text)`: Uses the `mastodon.py` library to post to Mastodon instances. Requires `MASTODON_BASE_URL` and `MASTODON_ACCESS_TOKEN`.

For optional manual approval, the service generates a Twitter intent URL with the post text and sends it as a push notification. This is implemented in `push_intent(text)`, which posts to a configured webhook (e.g., Pushover) using environment variables `PUSH_WEBHOOK`, `PUSH_TOKEN`, and `PUSH_USER`.

State management is handled by reading and writing a JSON file (`/data/state.json` by default) that tracks the IDs of posts already processed. This prevents duplicate postings across restarts.

## Deployment and Configuration

The service is containerized using Docker, with a `Dockerfile` based on the `python:3.12-slim` image. Dependencies are installed via pip (`feedparser`, `atproto`, `mastodon.py`, `requests`). The application code is copied into the container and executed via `python run.py`.

Docker Compose is used for orchestration, allowing environment variables to be set for feed URL, credentials, and notification settings. A volume is mounted to persist the state JSON file.

## Implementation Details

- The main loop parses the feed and processes up to the five most recent entries in chronological order, ensuring posts appear in the correct sequence.
- The code uses environment variables extensively for configuration, promoting flexibility and security.
- Posting functions check for the presence of required credentials before attempting to post, allowing partial configuration (e.g., only Bluesky or only Mastodon).
- The push notification sends a preformatted Twitter intent link, enabling quick manual approval or editing before posting on Twitter.
- Error handling is minimal and could be improved; exceptions during state loading default to an empty state.

## Practical Considerations

- The service assumes reliable access to the feed URL and social platform APIs.
- Credentials are stored as environment variables; secure handling is the responsibility of the deployer.
- The polling interval is fixed at 5 minutes; this could be parameterized.
- The state file is stored on a mounted volume to persist across container restarts.

## Summary

cross_poster is a straightforward, extensible tool for automating cross-posting from RSS/Atom feeds to Bluesky and Mastodon, with optional manual approval notifications. Its design favors simplicity and containerized deployment, making it suitable for personal or small-scale use. Future improvements could enhance robustness, platform support, and configurability.


