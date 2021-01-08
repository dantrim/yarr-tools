from yarr_tools.utils import retriever

from argparse import ArgumentParser
import sys
from pathlib import Path


def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="Input file")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists() or not input_path.is_file():
        print(f"bad input: {input_path}")
        sys.exit(1)

    histo = retriever.from_yarr(args.input)
    print(f"histo shape: {histo.histogram.shape}, histo name: {histo.name}")


if __name__ == "__main__":
    main()
