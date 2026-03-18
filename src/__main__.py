"""CLI for stylemirror."""
import sys, json, argparse
from .core import Stylemirror

def main():
    parser = argparse.ArgumentParser(description="StyleMirror — AI Personal Stylist. Personalized fashion recommendations based on body type, style, and wardrobe.")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = Stylemirror()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"stylemirror v0.1.0 — StyleMirror — AI Personal Stylist. Personalized fashion recommendations based on body type, style, and wardrobe.")

if __name__ == "__main__":
    main()
