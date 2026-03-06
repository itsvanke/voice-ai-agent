from openai import OpenAI
import json
from agent.prompt.system_prompt import SYSTEM_PROMPT
from agent.tools.tool_executor import execute_tool

client = OpenAI()

def process_request(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ]
    )

    intent_json = response.choices[0].message.content
    data = json.loads(intent_json)

    return execute_tool(data)