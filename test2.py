import logging
import asyncio
from telethon import TelegramClient, events

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Вводимо id та hash нашого телеграм клієнта
api_id = 28066055
api_hash = 'b5a2b6ee3f38a2e6e99e10a5ef9dea18'

# Збираємо клієнта до купи
client = TelegramClient("Test", api_id, api_hash)

# Вводимо id каналу, в який будемо пересилати повідомлення
target_channel_id = -1002154302487

# Вводимо ключові слова, які будемо шукати в повідомленнях
key_words = ["#Київська_область"]

@client.on(events.NewMessage(chats=[-1002166312019]))
async def normal_handler(event):
    try:
        for keyword in key_words:
            if keyword in event.message.message:
                logger.info(f"Found message: {event.message.message}")
                await client.send_message(target_channel_id, event.message)
    except Exception as e:
        logger.error(f"Error handling message: {e}")

async def main():
    while True:
        try:
            await client.start()
            logger.info("Client started successfully")
            await client.run_until_disconnected()
        except Exception as e:
            logger.error(f"Connection error: {e}")
            logger.info("Attempting to reconnect in 10 seconds...")
            await asyncio.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())
