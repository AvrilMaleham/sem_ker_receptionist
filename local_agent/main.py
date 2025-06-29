import os
import asyncio
#from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.agents import ChatCompletionAgent                                  # :contentReference[oaicite:0]{index=0}
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.contents import FunctionCallContent, FunctionResultContent  

from plugins import SalonDbPlugin
from prompt import SYSTEM_PROMPT

def create_agent() -> ChatCompletionAgent:
    
    kernel=Kernel()
    kernel.add_service(
        OpenAIChatCompletion(
            ai_model_id=os.getenv("OPENAI_CHAT_MODEL_ID","gpt-3.5-turbo"),
            service_id="openai",
            api_key=os.getenv("OPENAI_API_KEY")
        )
    )

    return ChatCompletionAgent(
        kernel=kernel,
        instructions=SYSTEM_PROMPT,
        plugins=[SalonDbPlugin()]
    )


async def main():
    agent = create_agent()
    print("🤖 Assistant: Hello! Welcome to Studio Six. How may I help you today? (type 'good bye !' to quit)")
    thread = None

    while True:
        user_input = await asyncio.to_thread(input, "> ")
        if user_input.strip().lower() == "good bye !":
            print("🤖 Assistant: Goodbye! Have a great day.")
            break
        #result = await agent.get_response(messages=user_input, thread=thread)
        async for response in agent.invoke(messages=user_input, thread=thread):
            content = response.content
            # Function call
            if isinstance(content, FunctionCallContent):
                print(f"[🔧 Calling function] {content.function_name}({content.arguments})")
            # Function result
            elif isinstance(content, FunctionResultContent):
                print(f"[✅ Function result] {content.result}")
            # Regular assistant message
            else:
                print(f"🤖 Assistant (thinking): {content}")

            # Keep using the same thread so context accumulates
            thread = response.thread

        print()  # blank line before next prompt

if __name__ == "__main__":
    asyncio.run(main())