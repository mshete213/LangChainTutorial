import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def main():
    print("Hello from langchaintutorial!")


if __name__ == "__main__":
    main()
