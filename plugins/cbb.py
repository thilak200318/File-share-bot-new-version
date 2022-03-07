#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>╭━━━━━━━━━━━━━━━🛸\n┣⪼ Cʀᴇᴀᴛᴏʀ 👉 <a href='tg://user?id={OWNER_ID}'>Mᴇ</a>\n┣⪼ Lᴀɴɢᴜᴀɢᴇ 👉 Pʏᴛʜᴏɴ𝟹\n┣⪼ Lɪʙʀᴀʀʏ 👉 <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ {__version__}</a>\n┣⪼ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ 👉 <a href='https://t.me/MVFILESHAREbot?start=Z2V0LTE1MTU0NDM5ODg0NTU4NzI='>MV - ғɪʟᴇ sʜᴀʀᴇ ʙᴏᴛ ✨</a>\n┣⪼ Cʜᴀɴɴᴇʟ 👉 <a href='https://t.me/MLAVIB'>MLᴀVIB</a>\n┣⪼ Bᴏᴛ ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ 👉 Fᴇʙʀᴜᴀʀʏ 2022\n┣⪼ Sᴇʀᴠᴇʀ 👉 Hᴇʀᴏᴋᴜ / Rᴀʏɪʟᴡᴀʏ\n┣⪼ Rᴇᴘᴏ ᴜᴘᴅᴀᴛᴇ 👉 Lᴀsᴛ ᴜᴘᴅᴀᴛᴇ 𝟸𝟶𝟸𝟸-𝟹-𝟽-𝟷𝟸𝟶𝟶\n╰━━━━━━━━━━━━━━━🛸</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤞 𝘾𝙡𝙤𝙨𝙚 🤞", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
