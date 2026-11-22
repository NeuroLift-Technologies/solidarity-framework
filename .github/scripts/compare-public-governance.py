"""Check imported files against their source revision and report upstream changes."""

import json
from pathlib import Path
import subprocess
import sys


def git(upstream, *args):
    return subprocess.check_output(["git", "-C", str(upstream), *args])


def main(source, upstream):
    manifest = json.loads((source / "nltotoi.json").read_text(encoding="utf-8"))
    config = manifest["upstream_governance"]
    revision = config["revision"]
    files = config["imported_files"]
    if not files:
        sys.exit("No upstream imports are listed in nltotoi.json.")
    upstream_head = git(upstream, "rev-parse", "HEAD").decode().strip()
    git(upstream, "cat-file", "-e", f"{revision}^{{commit}}")
    scope = [
        "CONTRIBUTING.md", "AGENTS.md", "GOVERNANCE.md",
        "governance.yaml", "governance.json", "SOPs", *files,
    ]
    print(f"Public governance baseline: {revision}")
    print(f"Upstream revision compared: {upstream_head}")
    print("\nImported file provenance:\n")
    mismatch = False
    for name in files:
        path = (source / name).resolve()
        if not path.is_relative_to(source.resolve()):
            sys.exit(f"Invalid imported file path: {name}")
        expected = git(upstream, "show", f"{revision}:{name}")
        matches = path.is_file() and path.read_bytes() == expected
        print(f"- {'Matches' if matches else 'MISMATCH'}: `{name}`")
        mismatch |= not matches
    print("\nUpstream changes since the imported revision (A/M/D and paths):\n")
    changes = git(upstream, "diff", "--name-status", "--no-renames", revision, upstream_head, "--", *scope)
    print(f"```text\n{changes.decode().rstrip()}\n```" if changes else "No changes in the compared paths.")
    return int(mismatch)


if __name__ == "__main__":
    sys.exit(main(*(Path(arg) for arg in sys.argv[1:])))
