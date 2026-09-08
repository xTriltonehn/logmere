"""small shared helpers, stdlib only"""
import re


def chunks(seq, n):
    """yield seq in slices of size n"""
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def human_size(num):
    """1234567 -> '1.2 MB'"""
    for unit in ("B", "KB", "MB", "GB"):
        if num < 1024 or unit == "GB":
            return "%d B" % num if unit == "B" \
                else "%.1f %s" % (num, unit)
        num /= 1024


SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(text):
    return SLUG_RE.sub("-", text.lower()).strip("-")
