import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    Author = os.getenv("AUTHOR")
    print(f"Author: {Author}")


if __name__ == "__main__":
    main()
