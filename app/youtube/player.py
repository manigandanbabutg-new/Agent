import os
import re
import requests


YOUTUBE_API =
    "https://www.googleapis.com/youtube/v3/search"


def clean_query(command):

    text = command.strip()

    patterns = [
        r"play\s+song\s+(.+)",
        r"play\s+music\s+(.+)",
        r"play\s+(.+)",
        r"youtube\s+(.+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

    return text


def find_youtube_video(command):

    api_key = os.getenv("YOUTUBE_API_KEY")

    if not api_key:
        return None

    query = clean_query(command)

    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 1,
        "key": api_key
    }

    try:

        response = requests.get(
            YOUTUBE_API,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        items = data.get("items", [])

        if not items:
            return None

        item = items[0]

        return {
            "video_id":
                item["id"]["videoId"],

            "title":
                item["snippet"]["title"]
        }

    except Exception as error:

        print(
            "YouTube error:",
            error
        )

        return None
