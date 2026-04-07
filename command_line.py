import argparse

def main():
    parser = argparse.ArgumentParser(description="My CLI Tool")

    parser.add_argument("name", help="Your name")
    parser.add_argument("--age", type=int, help="Your age")

    args = parser.parse_args()

    print(f"Hello {args.name}!")
    if args.age:
        print(f"You are {args.age} years old.")

if __name__ == "__main__":
    main()