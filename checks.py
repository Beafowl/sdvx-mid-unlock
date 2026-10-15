"""Checks the patch files before they are published.

- every patches/*.json is a spice2x patch list whose header matches its file name
- every memory patch has an offset, a DLL name and hex data of equal length
- SUPPORTED.md lists exactly the files in patches/, with the version from each header

Usage: python checks.py   (exits with code 1 and lists the problems if any check fails)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROW = re.compile(r"^\| ([^|]*) \| ([^|]*) \| ([^|]*) \| \[([^\]]*)\]\(([^)]*)\) \|$")
HEX = re.compile(r"^(?:[0-9A-Fa-f]{2})+$")


def check_patch_file(path, errors):
    name = path.stem
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        errors.append(f"{path.name}: not valid JSON ({e})")
        return None
    if not isinstance(data, list) or not data or "name" in data[0]:
        errors.append(f"{path.name}: the first entry must be the header (gameCode, version, ...)")
        return None
    header = data[0]
    if header.get("peIdentifier", name) != name:
        errors.append(f"{path.name}: header peIdentifier {header.get('peIdentifier')} does not match the file name")
    if header.get("gameCode") != name.split("-")[0]:
        errors.append(f"{path.name}: header gameCode {header.get('gameCode')} does not match the file name")
    for entry in data[1:]:
        label = f"{path.name}: {entry.get('name', entry.get('id', '?'))}"
        if entry.get("type") != "memory":
            continue
        patches = entry.get("patches")
        if not isinstance(patches, list) or not patches:
            errors.append(f"{label}: memory patch without patches")
            continue
        for p in patches:
            old, new = p.get("dataDisabled", ""), p.get("dataEnabled", "")
            if not isinstance(p.get("offset"), int) or not p.get("dllName"):
                errors.append(f"{label}: patch without offset or dllName")
            elif not (HEX.match(old) and HEX.match(new)) or len(old) != len(new):
                errors.append(f"{label}: bad data at offset {p['offset']}")
    return header


def main():
    errors = []
    headers = {p.stem: check_patch_file(p, errors) for p in sorted((ROOT / "patches").glob("*.json"))}

    listed = set()
    for line in (ROOT / "SUPPORTED.md").read_text(encoding="utf-8").splitlines():
        m = ROW.match(line.strip())
        if not m:
            continue
        version, ident, link = m.group(3).strip(), m.group(4).strip(), m.group(5).strip()
        listed.add(ident)
        if link != f"patches/{ident}.json":
            errors.append(f"SUPPORTED.md: {ident} links to {link}")
        if ident not in headers:
            errors.append(f"SUPPORTED.md: {ident} has no file in patches/")
            continue
        header = headers[ident] or {}
        stamp = header.get("version", "")[4:12]  # KFC-YYYYMMDDxx -> YYYYMMDD
        if stamp and version.replace("-", "") != stamp:
            errors.append(f"SUPPORTED.md: {ident} is listed as {version}, its header says {header.get('version')}")
    for ident in sorted(set(headers) - listed):
        errors.append(f"patches/{ident}.json is not listed in SUPPORTED.md")

    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"{len(headers)} patch file(s) OK")


if __name__ == "__main__":
    main()
