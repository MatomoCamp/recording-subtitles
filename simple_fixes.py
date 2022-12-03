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
    "Matamua": "Matomo",
    "Mitsuama": "Matomo",
    "Biwik": "Piwik",
    "Matomo Camp": "MatomoCamp",
    "Matomo camp": "MatomoCamp",
    "matamocamp": "matomocamp",
    "matumocamp": "matomocamp",
    "motomocamp": "matomocamp",
    "MatomoCam ": "MatomoCamp ",
    "MatomoCampp": "MatomoCamp",
    "Big Blue Button": "BigBlueButton",
    "Lucas": "Lukas"
}
search_strings = [re.escape(k) for k in sorted(replacements, key=len, reverse=True)]
pattern = re.compile("|".join(search_strings), flags=re.DOTALL)

for srt_file in current_dir.glob("**/*.srt"):
    text = srt_file.read_text()
    fixed_text, n = pattern.subn(lambda x: replacements[x.group(0)], text)
    if n:
        print(f"replaced {n} words in {srt_file}")
    srt_file.write_text(fixed_text)
