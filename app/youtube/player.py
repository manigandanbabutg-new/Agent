import re
import urllib.parse


def create_youtube_url(command):

    text = command.lower().strip()

    patterns = [
        r"play\s+(.+)",
        r"play\s+song\s+(.+)",
        r"play\s+music\s+(.+)",
        r"youtube\s+(.+)"
    ]

    query = command

    for pattern in patterns:
        match = re.search(
            pattern,
            text
        )

        if match:
            query = match.group(1)
            break

    query = query.strip()

    return (
        "https://www.youtube.com/results"
        "?search_query="
        + urllib.parse.quote(query)
    )
