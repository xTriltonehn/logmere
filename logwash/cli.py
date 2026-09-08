import argparse
import os
import tarfile
import time
from pathlib import Path

DAY = 86400


def find_logs(root, older_than=0, larger_than=0):
    # yield log files matching the age/size filters
    now = time.time()
    for path in Path(root).rglob("*.log"):
        try:
            st = path.stat()
        except OSError:
            continue
        if older_than and now - st.st_mtime < older_than * DAY:
            continue
        if larger_than and st.st_size < larger_than * 1024 * 1024:
            continue
        yield path


def archive(paths, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    bundle = out_dir / ("logs-%s.tar.gz" % stamp)
    with tarfile.open(bundle, "w:gz") as tar:
        for p in paths:
            tar.add(p, arcname=p.name)
    return bundle


def main(argv=None):
    ap = argparse.ArgumentParser(prog="logwash")
    ap.add_argument("root", help="directory to scan")
    ap.add_argument("--older-than", type=int, default=0, metavar="DAYS")
    ap.add_argument("--larger-than", type=int, default=0, metavar="MB")
    ap.add_argument("--archive", metavar="DIR")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    matched = list(find_logs(args.root, args.older_than, args.larger_than))
    if not matched:
        print("nothing matched")
        return 0
    for p in matched:
        print(p)
    if args.dry_run:
        print("dry-run: no files touched")
        return 0
    if args.archive:
        bundle = archive(matched, args.archive)
        print("archived %d files -> %s" % (len(matched), bundle))
        for p in matched:
            os.remove(p)
    return 0
