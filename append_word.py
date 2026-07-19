from pathlib import Path

README = Path("README.md")
WORDS = Path("words.txt")

START = "<!-- POEM_START -->"
END = "<!-- POEM_END -->"

readme = README.read_text()
all_words = WORDS.read_text().splitlines()

start = readme.index(START) + len(START)
end = readme.index(END)

current_poem = readme[start:end].strip()
current_words = current_poem.split() if current_poem else []

if len(current_words) < len(all_words):
    current_words.append(all_words[len(current_words)])

new_poem = " ".join(current_words)

updated = (
    readme[:start]
    + "\n\n"
    + new_poem
    + "\n\n"
    + readme[end:]
)

README.write_text(updated)

print(f"Added: {current_words[-1]}")