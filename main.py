from openai import OpenAI
from prompt import SCRATCH_KNOWLEDGE, CODE_AGENT_PROMPTV1
import json
import argparse
client = OpenAI()


def parse_content(content):
    content = json.loads(content)
    code = content["code"]
    code = code.replace("[scratchblocks]", "")
    code = code.replace("[/scratchblocks]", "")
    code.strip('\n')
    return code


def get_code(prompt):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": CODE_AGENT_PROMPTV1.format(knowledge=SCRATCH_KNOWLEDGE)},
            {"role": "user", "content": prompt},
        ],
    )
    content = response.choices[0].message.content
    code = parse_content(content)
    return code


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str)
    args = parser.parse_args()
    prompt = args.prompt
    code = get_code(prompt)
    print(code)


if __name__ == "__main__":
    main()