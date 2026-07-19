import os
from pathlib import Path

README = Path("README.md")

START = "<!-- POEM_START -->"
END = "<!-- POEM_END -->"

poem = os.environ["POEM"]
all_words = poem.split()

readme = README.read_text()

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

if len(current_words) > 0:
    print(f"Added: {current_words[-1]}")
else:
    print("Poem complete!")