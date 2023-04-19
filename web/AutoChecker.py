import asyncio
from EdgeGPT import Chatbot, ConversationStyle


async def AutoChecker_p(data_essay, data_topic):
    demo_id = 0
    path_init_prompt = "AutoChecker/init_prompt.txt"
    path_format_prompt = "AutoChecker/format_prompt.txt"
    data_init_prompt = open(path_init_prompt, "r").readlines()
    data_format_prompt = open(path_format_prompt, "r").readlines()

    init_prompt = "".join(data_init_prompt)
    format_prompt = "".join(data_format_prompt)
    topic_essay = "Topic: \n" + "".join(data_topic) + "\nEssay: \n" + "".join(
        data_essay)
    print(init_prompt)
    print(topic_essay)
    print(format_prompt)
    bot = Chatbot(cookiePath='AutoChecker/cookies.json')
    flag = False
    while not flag:
        try:
            await bot.reset()
            data = await bot.ask(
                prompt=init_prompt,
                conversation_style=ConversationStyle.creative,
                wss_link="wss://sydney.bing.com/sydney/ChatHub")
            print("INIT PROMPT")
            data = await bot.ask(
                prompt=topic_essay,
                conversation_style=ConversationStyle.creative,
                wss_link="wss://sydney.bing.com/sydney/ChatHub")
            print("TOPIC & ESSAY")
            data = await bot.ask(
                prompt=format_prompt,
                conversation_style=ConversationStyle.creative,
                wss_link="wss://sydney.bing.com/sydney/ChatHub")
            print("JSON FORMAT")
            print(data['item']['messages'][1]['adaptiveCards'][0]['body'][0]
                  ['text'])
            flag = True
        except Exception as e:
            print("Error: ", e)


def autochecker(data_essay, data_topic):
    asyncio.run(AutoChecker_p(data_essay, data_topic))


if __name__ == "__main__":
    autochecker("test", "test")