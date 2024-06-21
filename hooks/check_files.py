import argparse


def check_files(arguments: list[str]):
    for argument in arguments:
        print(f"Checking file: {argument}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    check_files(args.filenames)


if __name__ == "__main__":
    main()
