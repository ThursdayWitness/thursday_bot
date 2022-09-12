from pyrogram import Client, filters
from config.config import api_id, api_hash
from pyrogram.types import Message
import sticker_set


stickers = sticker_set.stickers
app = Client("my_account", api_id, api_hash)


@app.on_message(filters.me)
async def words_to_stickers_handler(client: Client, message: Message):
    text = message.text
    if text in stickers:
        await message.delete()
        await client.send_sticker(message.chat.id, stickers[text], reply_to_message_id=message.reply_to_message_id)


# @app.on_message(filters.me)
# async def help_keywords(client: Client, message: Message):
#     print(message.text)
#     if "забыл" in message.text:
#         output = stickers.keys()
#         print(output)


app.run()
