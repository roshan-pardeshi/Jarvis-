music = {
        "sahiba"  : "https://www.youtube.com/watch?v=NW6Dgax2d6I&list=RDNW6Dgax2d6I&start_radio=1&pp=0gcJCZYEOCosWNin",
        "mala_radio=1": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "sahiba" : "https://www.youtube.com/watch?v=JGwWNGJdvx8",
}

def play_song_on_youtube(song_name):
    import webbrowser
    import requests

    query = song_name.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            import re
            m = re.search(r"/watch\?v=([\w-]{11})", resp.text)
            if m:
                video_url = f"https://www.youtube.com/watch?v={m.group(1)}"
                webbrowser.open(video_url)
                return video_url
        # fallback: open search results page
        webbrowser.open(url)
        return url
    except Exception as ex:
        print(f"YouTube search failed: {ex}")
        return None



