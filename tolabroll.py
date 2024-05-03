import shutil
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import avb


def main():
    
    usage = f"Usage: {__file__} paths/to/bins"

    if not len(sys.argv) > 1:
        sys.exit(usage)
    print("Duplicating Name to Labroll...")
    for avid_bin in sys.argv[1:]:
        handle_bin(avid_bin)


def handle_bin(avid_bin):
    avid_bin_path = Path(avid_bin)
    bin_name = avid_bin_path.stem
    with TemporaryDirectory() as tmp_dir:
        tmp_dir_path = Path(tmp_dir)
        tmp_bin_path = tmp_dir_path / bin_name
        with avb.open(avid_bin) as f:
            for mob in f.content.mastermobs():
                mob.attributes["_USER"]["Labroll"] = mob.name
            f.write(tmp_bin_path)

        shutil.move(tmp_bin_path, avid_bin_path)
        print(f"Done: {avid_bin_path}")


if __name__ == "__main__":
    main()
