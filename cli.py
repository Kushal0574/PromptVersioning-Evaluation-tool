import argparse
from versioning import add_prompt, list_prompts
from evaluation import run_evaluation

def main():
    parser = argparse.ArgumentParser(description="PromptOps CLI")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add")
    add.add_argument("--name", required=True)
    add.add_argument("--content", required=True)

    eval_p = subparsers.add_parser("eval")
    eval_p.add_argument("--name", required=True)

    args = parser.parse_args()

    if args.command == "add":
        add_prompt(args.name, args.content)
    elif args.command == "eval":
        run_evaluation(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()