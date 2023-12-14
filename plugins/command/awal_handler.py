import config
import asyncio
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO 

from pyrogram import Client, types, enums
from plugins import Helper, Database
from pyrogram.types import (
    Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
)

async def start_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    fullname = f'{first} {last}' if last else first
    username = (
        f'@{msg.from_user.username}'
        if msg.from_user.username
        else '@vxnjul'
    )
    mention = msg.from_user.mention
    buttons = [
        [                       
            InlineKeyboardButton(
                "ʜᴇʟᴘ", callback_data="nsj"
            ),
InlineKeyboardButton(
                "ʀᴜʟᴇs", url="https://t.me/jawafes/27528"
            ),
        ],
  [            InlineKeyboardButton(
                "ᴄʟᴏsᴇ", callback_data="tutup"
            ),    
  ],

  ]
    await msg.reply_text(
        text=config.start_msg.format(
            id=msg.from_user.id,
            mention=mention,
            username=username,
            first_name=await helper.escapeHTML(first),
            last_name=await helper.escapeHTML(last),
            fullname=await helper.escapeHTML(fullname),
        ),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

async def status_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    db = Database(msg.from_user.id).get_data_pelanggan()
    keyboard = [
        [InlineKeyboardButton(                "ᴄᴀʀᴀ ᴛᴏᴘ ᴜᴘ ᴄᴏɪɴ ᴊᴀᴡᴀꜰᴇꜱꜱ", callback_data="tpp")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)        
    pesan = '<b>❏ User Info:</b>\n'
    pesan += f'├<b>Nama :</b> {db.mention}\n'
    pesan += f'├<b>User ID :</b> <code>{db.id}</code>\n'
    pesan += f'└<b>Status :</b> {db.status}\n\n'
    pesan += '<b>❏ User Stats:</b>\n'
    pesan += f'├<b>Saldo :</b> {helper.formatrupiah(db.coin)} Coin\n'
    pesan += f'├<b>Menfess Harian :</b> {db.menfess}/{config.batas_kirim}\n'
    pesan += f'├<b>Semua Menfess :</b> {db.all_menfess}\n'
    pesan += f'└<b>Bergabung :</b> {db.sign_up}\n\n'
    pesan += f'<b>Code topup anda</b> » <code>fess {db.id} </code>'
    await msg.reply(pesan, True, enums.ParseMode.HTML,reply_markup=reply_markup)

async def statistik_handler(client: Helper, id_bot: int):
    db = Database(client.user_id)
    bot = db.get_data_bot(id_bot)
    pesan = "<b>📊 STATISTIK BOT\n\n"
    pesan += f"▪️Pelanggan: {db.get_pelanggan().total_pelanggan}\n"
    pesan += f"▪️Admin: {len(bot.admin)}\n"
    pesan += f"▪️Talent: {len(bot.talent)}\n"
    pesan += f"▪️Banned: {len(bot.ban)}\n\n"
    pesan += f"🔰Status bot: {'AKTIF' if bot.bot_status else 'TIDAK AKTIF'}</b>"
    await client.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def list_admin_handler(helper: Helper, id_bot: int):
    db = Database(helper.user_id).get_data_bot(id_bot)
    pesan = "<b>Owner bot</b>\n"
    pesan += "• ID: " + str(config.id_admin) + " | <a href='tg://user?id=" + str(config.id_admin) + "'>Owner bot</a>\n\n"
    if len(db.admin) > 0:
        pesan += "<b>Daftar Admin bot</b>\n"
        ind = 1
        for i in db.admin:
            pesan += "• ID: " + str(i) + " | <a href='tg://user?id=" + str(i) + "'>Admin " + str(ind) + "</a>\n"
            ind += 1
    await helper.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def list_ban_handler(helper: Helper, id_bot: int):
    db = Database(helper.user_id).get_data_bot(id_bot)
    if len(db.ban) == 0:
        return await helper.message.reply_text('<i>Tidak ada user dibanned saat ini</i>', True, enums.ParseMode.HTML)
    else:
        pesan = "<b>Daftar banned</b>\n"
        ind = 1
        for i in db.ban:
            pesan += "• ID: " + str(i) + " | <a href='tg://openmessage?user_id=" + str(i) + "'>( " + str(ind) + " )</a>\n"
            ind += 1
    await helper.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def gagal_kirim_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    fullname = f'{first} {last}' if last else first
    username = (
        f'@{msg.from_user.username}'
        if msg.from_user.username
        else '@vxnjul'
    )
    mention = msg.from_user.mention
    buttons = [
        [InlineKeyboardButton(
                "ʜᴇʟᴘ", callback_data="nsj"),
InlineKeyboardButton(
                "ʀᴜʟᴇs", url="https://t.me/jawafes/27528"),
        ],
   [ InlineKeyboardButton(
                "ᴄʟᴏsᴇ", callback_data="tutup"),
   ],
        ]
    await msg.reply_text(
        text=config.gagalkirim_msg.format(
            id=msg.from_user.id,
            mention=mention,
            username=username,
            first_name=await helper.escapeHTML(first),
            last_name=await helper.escapeHTML(last),
            fullname=await helper.escapeHTML(fullname),
        ),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

async def topup_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    fullname = f'{first} {last}' if last else first
    username = (
        f'@{msg.from_user.username}'
        if msg.from_user.username
        else '@vxnjul'
    )
    mention = msg.from_user.mention
    buttons = [
        [                       
            InlineKeyboardButton(
                "ᴛᴏᴘ ᴜᴘ ᴄᴏɪɴ ᴊᴀᴡᴀꜰᴇꜱꜱ", url="https://telegra.ph//file/edae2f8b4a1453b8a6e52.jpg"        
            ),
        ],
    ]
    await msg.reply_text(
        text=config.topup_msg.format(
            id=msg.from_user.id,
            mention=mention,
            username=username,
            first_name=await helper.escapeHTML(first),
            last_name=await helper.escapeHTML(last),
            fullname=await helper.escapeHTML(fullname),
        ),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )



async def cb_help(client, callback_query):
    user_id = callback_query.from_user.id 
    username = (
        f'@{callback_query.from_user.username}'
        if callback_query.from_user.username
        else '@vxnjul'
  )
    buttons = [
        [
InlineKeyboardButton(
                "ʙᴀᴄᴋ", callback_data="bck"
            ),
            InlineKeyboardButton(
                "ᴄʟᴏsᴇ", callback_data="tutup"
            ),    
  ],
    ]
    await callback_query.edit_message_text(
        f"""
 <b>silahkan kirim pesan anda menggunakan hashtag:</b>
 
• <code>#mba</code> [ untuk identitas perempuan]
• <code>#mas</code> [ untuk identitas laki-laki ]
• <code>#spill</code> [ untuk spill masalah ]
• <code>#tanya</code> [ untuk bertanya ]
• <code>#story</code> [ untuk berbagi cerita/curhat ]
• <code>#pap</code> [ khusus media foto/video ] 

<b>Contoh pesan:</b> <code>#mas yang dari jogja. jalan yuk {username} </code>

<i>Pastikan pesanmu lebih dari 3 kata, ya</i>
""",
        disable_web_page_preview=True,
     reply_markup=InlineKeyboardMarkup(buttons),
)


async def help_handler(client, msg):
    db = Database(msg.from_user.id)
    member = db.get_data_pelanggan()

    pesan = "Supported commands\n" + '/start — kirim menfess\n'    
    if member.status == 'admin':
        pesan += '\nHanya Admin\n'
        pesan += '/tf_coin — transfer coin\n'
        pesan += '/settings — melihat settingan bot\n'
        pesan += '/list_admin — melihat list admin\n'
        pesan += '/list_ban — melihat list banned\n\n'
        pesan += 'Perintah banned\n'
        pesan += '/ban — ban user\n'
        pesan += '/unban — unban user\n'
    elif member.status == 'owner':
        pesan += '\n=====OWNER COMMAND=====\n'
        pesan += '/tf_coin — transfer coin\n'
        pesan += '/settings — melihat settingan bot\n'
        pesan += '/list_admin — melihat list admin\n'
        pesan += '/list_ban — melihat list banned\n'
        pesan += '/stats — melihat statistik bot\n'
        pesan += '/bot — setbot (on|off)\n'

        pesan += '\n=====BROADCAST OWNER=====\n'
        pesan += '/broadcast — mengirim pesan broadcast kesemua user\n'
        pesan += '/admin — menambahkan admin baru\n'
        pesan += '/unadmin — menghapus admin\n'
        pesan += '/list_ban — melihat list banned\n'
        pesan += '\n=====BANNED COMMAND=====\n'
        pesan += '/ban — ban user\n'
        pesan += '/unban — unban user\n'

    await msg.reply(pesan, True, enums.ParseMode.HTML)

async def cb_hapus(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [
        [
        InlineKeyboardButton(
                "🗑ʜᴀᴘᴜs ᴘᴏsᴛɪɴɢᴀɴ", url="https://t.me/GJNadminbot?start=start"
 ),          
        ],
[      InlineKeyboardButton(
                "ʙᴀᴄᴋ", callback_data="bck"
            ),
    ],
]
    await callback_query.edit_message_text(
        f"""
<b>Biaya menghapus postingan adalah 25 coin. Jika anda belum memiliki coin silahkan pergi ke menu top up.</b>

<b>❏Jika anda sudah memiliki coin, silahkan ketikkan salah satu code transfer dibawah ini:</b>
├<code>/tf_coin 1020381855 25</code>
├<code>/tf_coin 5422684990 25</code>
├<code>/tf_coin 1717010997 25</code>
└<code>/tf_coin 6188825810 25</code>

<b>Jika sudah, salin code transfer dan bukti transfer coin anda lalu pergi ke button hapus dibawah ini</b>
""",
        disable_web_page_preview=True,
     reply_markup=InlineKeyboardMarkup(buttons),
)

async def cb_back(client, callback_query):
    user_id = callback_query.from_user.id
    mention = callback_query.from_user.mention
    username = (
        f'@{callback_query.from_user.username}'
        if callback_query.from_user.username
        else '@vxnjul'
  )
    buttons = [
       [ InlineKeyboardButton(
                "ʜᴇʟᴘ", callback_data="nsj"
            ),
            InlineKeyboardButton(
                "ʀᴜʟᴇs", url="https://t.me/jawafes/27528"
 ),          
      ],
[           InlineKeyboardButton(
                "ᴄʟᴏsᴇ", callback_data="tutup"
            ),    
  ],
       ]
    await callback_query.edit_message_text(
        f"""
❏ Haii {mention}

𝗝𝗮𝘄𝗮𝗳𝗲𝘀𝘀 𝗔𝘂𝘁𝗼 𝗽𝗼𝘀𝘁 akan membantumu mengirimkan pesan secara anonim ke channel @JAWAFES.

silahkan baca help dan rules terlebih dahulu.
""",
        disable_web_page_preview=True,
     reply_markup=InlineKeyboardMarkup(buttons),
)

async def cb_topup(client, callback_query):
    user_id = callback_query.from_user.id 
    username = (
        f'@{callback_query.from_user.username}'
        if callback_query.from_user.username
        else '@vxnjul'
  )
    buttons = [
      [
  InlineKeyboardButton(
                "ᴛᴏᴘ ᴜᴘ ᴄᴏɪɴ ᴊᴀᴡᴀꜰᴇꜱꜱ", url="https://telegra.ph//file/edae2f8b4a1453b8a6e52.jpg"
            ),
    ],
]
    await callback_query.edit_message_text(
        f"""
Jawafess coin di gunakan untuk biaya mengirim menfess/promote ke @JAWAFES jika 5x batas kirim harian sudah habis. biaya untuk sekali mengirim adalah 25 coin.

❏ Cara Membeli Coin Jawafess
├1. klik button top up dibawah ini
├2. kirim bukti pembayaran anda <a href='https://t.me/GJNadminbot?start=start'>disini</a>
├3. nama [ nama telegram anda ]
└4. code topup anda: <code>fess {user_id}</code>

coin akan berkurang secara otomatis jika batas harian sudah habis. <b>harga 100 coin = 1000 rupiah</b>
""",
        disable_web_page_preview=True,
     reply_markup=InlineKeyboardMarkup(buttons),
)
