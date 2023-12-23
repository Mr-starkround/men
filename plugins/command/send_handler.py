import config, sys, os, requests
import re

from pyrogram import Client, types, enums
from plugins import Database, Helper
from pyrogram.types import (
    Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
)

async def send_with_pic_handler(client: Client, msg: types.Message, key: str, hastag: list):
db = Database(msg.from_user.id)
helper = Helper(client, msg)
user = db.get_data_pelanggan()
# Check if the sender has a username
if msg.from_user.username is None:
return await msg.reply('Anda harus memiliki username untuk mengirim menfess.', quote=True)
# Check if the message mentions the sender's username
username = f"@{msg.from_user.username}".lower() if msg.from_user.username else None
if username and username not in msg.text.lower():
return await msg.reply('Anda hanya dapat mengirim menfess dengan menggunakan username Anda sendiri.', quote=True)
# Check if the user is authorized to send messages
if user.status not in ['owner', 'admin', 'talent', 'daddy sugar']:
# Check if the message mentions usernames from the admin list
admin_usernames = ["@ownneko", "@satt329", "@nekojoyy", "@winnieewwe", "@mwehehe0j", "@ikeenandrasw", "@sasaanmf", "@lordmudaid", "@towirg", "@suunshiinneee", "@kjitten"]
for admin_username in admin_usernames:
if admin_username in msg.text.lower():
return await msg.reply(f'Maaf, Anda tidak diizinkan mengirim pesan yang mengandung username member premium {admin_username}.', quote=True)
# Check for URLs in the message
if re.search(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", msg.text or ""):
return await msg.reply("Tidak diizinkan mengirimkan tautan.")
if msg.text or msg.photo or msg.video or msg.voice:
menfess = user.menfess
all_menfess = user.all_menfess
coin = user.coin
if menfess >= config.batas_kirim and user.status in ['member', 'talent']:
if coin >= config.biaya_kirim:
coin = user.coin - config.biaya_kirim
else:
return await msg.reply(f'🙅🏻‍♀️ post gagal terkirim. kamu hari ini telah mengirim ke menfess sebanyak {menfess}/{config.batas_kirim} kali.serta coin mu kurang untuk mengirim menfess diluar batas harian., kamu dapat mengirim menfess kembali pada hari esok.\n\n waktu reset jam 1 pagi. \n\n\n\n Info: Topup Coin Hanya ke @OwnNeko', quote=True)
if key == hastag[0]:
picture = config.pic_girl
elif key == hastag[1]:
picture = config.pic_boy
if user.status == 'talent':
picture = config.pic_talentgirl
if user.status == 'owner':
picture = config.pic_owner
if user.status == 'admin':
if key == hastag[0]:
picture = config.pic_admingirl
elif key == hastag[1]:
picture = config.pic_adminboy
if user.status == 'daddy sugar':
picture = config.pic_daddysugar
if user.status == 'boyfriend rent':
picture = config.pic_bfrent
elif user.status == 'moans boy':
picture = config.pic_moansboy
link = await get_link()
caption = msg.text or msg.caption
entities = msg.entities or msg.caption_entities