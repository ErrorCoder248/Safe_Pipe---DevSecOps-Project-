import argparse
from safe_pipe_core import scan_folder

def main():
    parser = argparse.ArgumentParser(description="SafePipe Headless Scanner")
    parser.add_argument("--folder", required=True, help="Folder containing files to scan")
    parser.add_argument("--output", default="scan_results.json", help="Output JSON file")
    args = parser.parse_args()

    scan_folder(args.folder, args.output)

if __name__ == "__main__":
    main()
