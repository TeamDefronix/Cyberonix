#!/usr/bin/env python3
import os
import sys
import subprocess

# --- locate JS_VOYAGER dir and main.py ---
THIS_DIR = os.path.dirname(os.path.abspath(__file__))        # .../main/JS_Voyager
MAIN_PY = os.path.join(THIS_DIR, "main.py")

# --- Import banner from project if available (optional) ---
# allow importing banner from main/tools by adding project root to path
PROJECT_ROOT = os.path.abspath(os.path.join(THIS_DIR, "..", ".."))
TOOLS_PATH = os.path.join(PROJECT_ROOT, "main", "tools")
if TOOLS_PATH not in sys.path:
    sys.path.insert(0, TOOLS_PATH)

try:
    import banner
    import colors
except Exception:
    banner = None
    colors = None

def interactive_flow():
    """Original interactive prompt flow (unchanged behavior)."""
    if banner:
        banner.main()
    print("Please provide the following input:")

    # URL or file
    option = input("Enter 'u' for URL or 'f' for file path: ").strip().lower()
    if option == 'u':
        url = input("Enter the URL to scan (e.g. https://example.com): ").strip()
        base_args = ['-u', url]
    elif option == 'f':
        file_path = input("Enter the file path (containing list of URLs): ").strip()
        base_args = ['-f', file_path]
    else:
        print("Invalid input! Try again.")
        return interactive_flow()

    # additional options
    options = []
    secrets = input("Do you want to run secrets scan? (Y/N): ").strip().lower()
    if secrets == 'y':
        options.append('--secrets')

    download = input("Do you want to download JS files? (Y/N): ").strip().lower()
    if download == 'n':
        options.append('--no-download')

    report = input("Do you want to save the report? (Y/N): ").strip().lower()
    if report == 'y':
        options.append('--report')

    limit = input("Do you want to limit the number of JS targets? (Y/N): ").strip().lower()
    if limit == 'y':
        limit_value = input("Enter the limit number: ").strip()
        options.extend(['--limit', limit_value])

    out_dir = input("Enter output directory to save reports: ").strip()
    options.extend(['--out-dir', out_dir])

    return base_args + options

def forward_args_mode(argv):
    """
    If argv contains args, normalize and return them.
    `argv` is sys.argv[1:].
    Remove a leading '--' if present (common separator).
    """
    args = list(argv)
    if len(args) > 0 and args[0] == "--":
        args = args[1:]
    return args

def run_main_with_args(arg_list):
    if not os.path.exists(MAIN_PY):
        print(f"Error: {MAIN_PY} not found. Ensure you're running from the project's JS_Voyager folder.")
        return 1

    cmd = [sys.executable, MAIN_PY] + arg_list
    print("\n[+] Launching JS-Voyager (forwarding args):\n    " + " ".join(cmd) + "\n")
    # Run with cwd so relative imports/files inside main.py work
    return subprocess.run(cmd, cwd=THIS_DIR).returncode

def main():
    # If runner was called with arguments, use them (non-interactive)
    # sys.argv[1:] will contain forwarded args (possibly including a leading '--')
    forwarded = forward_args_mode(sys.argv[1:])
    if forwarded:
        # direct non-interactive mode
        returncode = run_main_with_args(forwarded)
        sys.exit(returncode)

    # otherwise use interactive prompts
    args_to_pass = interactive_flow()
    returncode = run_main_with_args(args_to_pass)
    sys.exit(returncode)

if __name__ == "__main__":
    main()

