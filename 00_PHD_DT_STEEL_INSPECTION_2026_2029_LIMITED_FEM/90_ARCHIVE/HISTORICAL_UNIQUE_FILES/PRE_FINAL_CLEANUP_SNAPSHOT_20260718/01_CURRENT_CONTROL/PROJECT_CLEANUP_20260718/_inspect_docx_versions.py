import html
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
}

sys.stdout.reconfigure(encoding="utf-8")


for path in sorted((Path(__file__).resolve().parents[2] / "Paper 1").glob("*.docx")):
    with zipfile.ZipFile(path) as archive:
        core = ET.fromstring(archive.read("docProps/core.xml"))
        document = archive.read("word/document.xml").decode("utf-8", errors="ignore")
    value = lambda query: core.find(query, NS).text if core.find(query, NS) is not None else ""
    text = " ".join(html.unescape(part) for part in re.findall(r"<w:t[^>]*>(.*?)</w:t>", document))
    print(f"FILE={path.name}")
    print(f"MODIFIED={value('dcterms:modified')} CREATOR={value('dc:creator')}")
    print(f"WORDS={len(text.split())} CHARS={len(text)}")
    print(f"START={text[:500]}")
