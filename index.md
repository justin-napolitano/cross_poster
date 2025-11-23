---
slug: "github-cross-poster"
title: "cross_poster"
repo: "justin-napolitano/cross_poster"
githubUrl: "https://github.com/justin-napolitano/cross_poster"
generatedAt: "2025-11-23T08:31:40.891027Z"
source: "github-auto"
---


# Technical Overview of cross_poster

## Motivation

The project addresses a common need to automate the distribution of content updates from a single source feed to multiple social platforms. Instead of manually reposting or relying on platform-specific tools, this service centralizes the process, reducing friction and ensuring consistent presence across networks.

## Problem Statement

Content creators and site maintainers often publish updates via RSS or Atom feeds but lack a streamlined way to propagate those updates to decentralized or federated social platforms like Bluesky and Mastodon. Manual reposting is tedious and error-prone, and existing tools may not support all platforms or require complex setup. Additionally, some users prefer to approve posts before publishing, which requires a lightweight approval mechanism.

## Architecture and Implementation

The core of the system is a Python script (`app/run.py`) that:

- Polls a configured RSS/Atom feed at fixed intervals (every 5 minutes).
- Parses the latest entries using `feedparser`.
- Maintains a local state file (`state.json`) to track which entries have already been posted.
- For each new entry:
  - Constructs a post text combining the entry title and URL.
  - Posts directly to Bluesky using the `atproto` client if credentials are provided.
  - Posts directly to Mastodon using the `mastodon.py` client if credentials are provided.
  - Sends a push notification containing a preformatted X (formerly Twitter) intent URL to facilitate one-tap manual approval.

### State Management

State is persisted in a JSON file mounted into the container. This file stores a list of IDs of feed entries that have already been processed, preventing duplicate posts across restarts.

### Posting Logic

- **Bluesky:** Uses the `atproto` client to login with handle and password, then sends a post.
- **Mastodon:** Uses the `mastodon.py` client with base URL and access token to post a status.
- **Push Notification:** Sends a POST request to a configured webhook URL (e.g., Pushover) with a message containing the X intent link.

### Containerization

The service is packaged as a Docker container based on the official Python 3.12 slim image. Dependencies are installed via pip in the Dockerfile. The container exposes no ports but runs continuously, orchestrated via `docker-compose`.

Environment variables provide all configuration, including feed URL, credentials, and notification settings.

## Practical Considerations

- The polling interval is hardcoded to 5 minutes; this could be parameterized.
- Error handling is minimal; failures in posting or network errors are silently ignored or cause retries on the next cycle.
- The push notification mechanism is generic and can be replaced with any service that accepts HTTP POST.
- The service assumes that feed entries have unique IDs or URLs.

## Summary

This project exemplifies a minimal, practical approach to cross-posting feed content to multiple social platforms with optional manual approval. It leverages existing Python clients and containerization to provide a deployable, extensible tool. Future enhancements could improve robustness, configurability, and platform support.
