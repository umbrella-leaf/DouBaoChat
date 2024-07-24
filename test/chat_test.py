import asyncio
from DouBaoChat.bot import ChatBot


async def main():
    chatbot = ChatBot(
        api_key="70f78b22-8f4e-42ef-a98f-0d6b1b6b2cd3",
        endpoint="doubao_pro_32k"
    )
    print(await chatbot.ask(message="请你告诉我1+1等于几？"))
    print(await chatbot.ask(message="我刚才问你什么？"))
    print(await chatbot.ask(message="我刚才问你的数学题的答案是多少？"))


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())