import os
import asyncio
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.ai.chat_response_agent import OpenAIResponsesAgent
from semantic_kernel.skill_definition import SkillCollection

from plugins import SalonDbPlugin
from prompt import system_prompt

def create_agent() -> OpenAIResponsesAgent:
    load_dotenv()
    kernel = Kernel()
    kernel.add_service(
        OpenAIChatCompletion(
            service_id="openai",
            api_key=os.getenv("OPENAI_API_KEY"),
            model=os.getenv("gpt-3.5-turbo")
        )
    )
    skill = SkillCollection()
    skill.add_skill(SalonDbPlugin())
    kernel.import_skill(skill, skill_name="SalonDb")
    return OpenAIResponsesAgent(
        kernel=kernel,
        system_prompt=system_prompt
    )

async def main():
    agent = create_agent()
    print("🤖 Apple: Hello! Welcome to Studio Six. How may I help you today? (type 'exit' to quit)")
    while True:
        user_input = await asyncio.to_thread(input, "> ")
        if user_input.strip().lower() in ("exit", "quit"):
            print("🤖 Apple: Goodbye! Have a great day.")
            break
        response = await agent.invoke_async(user_input=user_input)
        print(f"🤖 Apple: {response}\n")

if __name__ == "__main__":
    asyncio.run(main())