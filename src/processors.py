import json
from pathlib import Path

def load_processor(path):
    """Load hardware processor definition from a JSON file."""
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)
