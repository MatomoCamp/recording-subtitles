"""
fix a few common mistakes

based on
https://stackoverflow.com/a/15448887
"""
import re
from pathlib import Path

current_dir = Path(".")

replacements = {
    "Mitoma": "Matomo",
    "Matobo": "Matomo",
    "Matoma": "Matomo",
    "matoma": "matomo",
    "Matamow": "Matomo",
    "Matahomo": "Matomo",
    "Matomo Camp": "MatomoCamp",
    "matamocamp":"matomocamp",
    "matumocamp":"matomocamp",
    "motomocamp":"matomocamp",
    "Big Blue Button": "BigBlueButton",
    "Lucas": "Lukas"
}
search_strings = [re.escape(k) for k in sorted(replacements, key=len, reverse=True)]
pattern = re.compile("|".join(search_strings), flags=re.DOTALL)

for srt_file in current_dir.glob("**/*.srt"):
    text = srt_file.read_text()
    fixed_text = pattern.sub(lambda x: replacements[x.group(0)], text)
    srt_file.write_text(fixed_text)
