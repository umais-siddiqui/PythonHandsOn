import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    message = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Only produce json in the format for a random user stroy you can create only JSON as ouptut use GHERKIN for Acceptance criteria and dont have more than 6 acceptance crietria and cover atleast 2 edge cases  {\"ItemNumber\":1,\"Description\":\"A description of the item\",\"AcceptanceCriteria\":\"Acceptance criteria for the user story\"}"}, 
        ],
    )

    for block in message.content:
        if block.type == "text":
            print(block.text)
            break


if __name__ == "__main__":
    main()
