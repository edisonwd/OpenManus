import asyncio
import chainlit as cl
from app.agent.manus import Manus
from app.logger import logger


from chainlit import AskUserMessage, Message, on_chat_start

@cl.step
async def parent_step():
    await child_step()
    return "Parent step output"

@cl.step
async def child_step():
    return "Child step output"

@cl.on_chat_start
async def main():
    await parent_step()




@cl.on_message
async def main(message: cl.Message):
    agent = Manus()
    try:
        prompt = message.content

        if not prompt.strip():
            logger.warning("Empty prompt provided.")
            return
        response = '你好'
        async with cl.Step(name="manus") as step:
            step.output = '测试'
            response = await agent.run(prompt)
        # Send a response back to the user
        msg = cl.Message(
            content=f"Received: {response}",
        )

        await msg.send()

        await cl.sleep(2)

        msg.content = "Hello again!"
        await msg.update()

        await cl.sleep(2)
        await msg.remove()

    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")


# if __name__ == "__main__":
#     asyncio.run(main())
