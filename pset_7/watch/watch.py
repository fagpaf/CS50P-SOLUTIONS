import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Procura a tag iframe com o atributo src contendo o link do YouTube
    match = re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"[^>]*>', s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
