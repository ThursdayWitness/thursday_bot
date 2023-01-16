import asyncio
from pyrogram import Client, filters
from config.config import api_id, api_hash
from pyrogram.types import Message
import sticker_set
from chat_ids import ids as chats

stickers = sticker_set.stickers
app = Client("my_account", api_id, api_hash)


def __init__():
    print("UserBot is online")


@app.on_message(filters.me & filters.command("chatId", prefixes="."))
async def get_id(client: Client, message: Message):
    await client.send_message("me", f"Chat id: {message.chat.id}")
    await asyncio.sleep(16)
    await message.delete()


# @app.on_message(filters.me & filters.sticker)
# async def get_sticker_id(client: Client, message: Message):
#     newMessage = await client.send_message("me", f"Sticker id: {message.sticker.file_id}\n")
#     await asyncio.sleep(16)
#     await message.delete()
#     await newMessage.delete()


@app.on_message(filters.me & filters.command("жмуписю", prefixes="."))
async def send_handshake(client: Client, message: Message):
    await message.delete()
    await client.send_message(message.chat.id, "🤝")


@app.on_message(filters.me & filters.command("kws"))
async def help_keywords(client: Client, message: Message):
    await client.delete_messages(message.chat.id, message.id)
    keywords = (','.join(stickers.keys())).split(',')
    result = []
    for i in range(len(stickers)):
        result.append(f"{keywords[i]}")
    msg = await client.send_message("me", '\n'.join(result))
    await asyncio.sleep(16)
    await msg.delete()


@app.on_message(filters.me & filters.text)
async def words_to_stickers_handler(client: Client, message: Message):
    if message.chat.id != chats['saved'] and message.chat.id != chats['ls']:
        return
    text = message.text.lower()
    if text in stickers:
        await message.delete()
        await client.send_sticker(message.chat.id, stickers[text], reply_to_message_id=message.reply_to_message_id)


app.run(__init__())
