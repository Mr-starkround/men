import config
import re

from pyrogram import Client, types, enums
from plugins import Database, Helper
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def get_link():
    anu = str(config.channel_1).split('-100')[1]
    return "https://t.me/c/{anu}"

async def send_with_pic_handler(client: Client, msg: types.Message, key: str, hastag: list):
    db = Database(msg.from_user.id)
    helper = Helper(client, msg)
    user = db.get_data_pelanggan()   
    if msg.text or msg.photo or msg.video or msg.voice:
        menfess = user.menfess
        all_menfess = user.all_menfess
        coin = user.coin
        if menfess >= config.batas_kirim:
            if user.status == 'member' or user.status == 'talent':
                if coin >= config.biaya_kirim:
                    coin = user.coin - config.biaya_kirim   
                else:
                    return await msg.reply(f'Pesanmu gagal terkirim. kamu hari ini telah mengirim ke menfess sebanyak {menfess}/{config.batas_kirim} kali. Coin mu kurang untuk mengirim menfess diluar batas harian. \n\nwaktu reset jam 1 pagi \n\n<b>Kamu dapat mengirim menfess kembali pada esok hari atau top up coin untuk mengirim diluar batas harianmu. <b>Topup Coin silahkan klik</b> /topup ', True, enums.ParseMode.HTML)

        if key == hastag[0]:
            picture = config.pic_girl
        elif key == hastag[1]:
            picture = config.pic_boy

        link = await get_link()       
        caption = msg.text or msg.caption
        entities = msg.entities or msg.caption_entities

        kirim = await client.send_photo(config.channel_1, picture, caption, caption_entities=entities)
        await helper.send_to_channel_log(type="log_channel", link=link + str(kirim.id))
        await db.update_menfess(coin, menfess, all_menfess)
        await msg.reply(f"Pesan anda <a href='{link + str(kirim.id)}'>berhasil terkirim.</a> \n\nhari ini kamu telah mengirim pesan sebanyak {menfess + 1}/{config.batas_kirim}. kamu dapat mengirim pesan sebanyak {config.batas_kirim} kali dalam sehari. \n\nwaktu reset setiap jam 1 pagi", True, enums.ParseMode.HTML, reply_markup=reply_markup)
    else:
        await msg.reply('media yang didukung photo, video dan voice')

async def send_menfess_handler(c: Client, cb: CallbackQuery):
    m = cb.message
    match = int(cb.matches[0].group(1))
    message_id = m.reply_to_message.message_id
    if match == 1:
        channel_tujuan1 = config.channel_1
    elif match == 2:
        channel_tujuan2 = config.channel_2
    else:        
    x = await c.copy_message(
        channel_tujuan1,
        m.chat.id,
        message_id,
        caption=m.caption or None
    )
    if isinstance(x, Message):
        message_id = x.message_id
        chat_id = x.chat.id
    else:
        message_id = None
        chat_id = None
    await m.delete()
    await m.reply(
        "**Pesan berhasil terkirim, silakan lihat dengan klik tombol dibawah ini!**",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Klik disini", url=f"https://t.me/c/{str(chat_id)[4:]}/{message_id}")
            ]
        ])
    )
    fwd = await c.forward_messages(
        config.channel_log,
        m.chat.id,
        message_id
    )
    m = m.reply_to_message
    await fwd.reply(
        (
            "**User mengirim pesan**\n"
            f"Nama: {m.from_user.first_name}\n"
            f"Id: {m.from_user.id}\n"
            f"Username: {m.from_user.mention}"
        )
    )

async def transfer_coin_handler(client: Client, msg: types.Message):
    if re.search(r"^[\/]tf_coin(\s|\n)*$", msg.text or msg.caption):
        err = "<i>perintah salah /tf_coin [jmlh_coin]</i>" if msg.reply_to_message else "<i>perintah salah /tf_coin [id_user] [jmlh_coin]</i>"
        return await msg.reply(err, True)
    helper = Helper(client, msg)
    if re.search(r"^[\/]tf_coin\s(\d+)(\s(\d+))?", msg.text or msg.caption):
        x = re.search(r"^[\/]tf_coin\s(\d+)(\s(\d+))$", msg.text or msg.caption)
        if x:
            target = x.group(1)
            coin = x.group(3)
        y = re.search(r"^[\/]tf_coin\s(\d+)$", msg.text or msg.caption)
        if y:
            if msg.reply_to_message:
                if msg.reply_to_message.from_user.is_bot == True:
                    return await msg.reply('🤖Bot tidak dapat ditranfer coin', True)
                elif msg.reply_to_message.sender_chat:
                    return await msg.reply('channel tidak dapat ditranfer coin', True)
                else:
                    target = msg.reply_to_message.from_user.id
                    coin = y.group(1)
            else:
                return await msg.reply('sambil mereply sebuah pesan', True)

        if msg.from_user.id == int(target):
            return await msg.reply('<i>Tidak dapat transfer coin untuk diri sendiri</i>', True)

        user_db = Database(msg.from_user.id)
        anu = user_db.get_data_pelanggan()
        my_coin = anu.coin
        if my_coin >= int(coin):
            db_target = Database(int(target))
            if await db_target.cek_user_didatabase():
                target_db = db_target.get_data_pelanggan()
                ditransfer = my_coin - int(coin)
                diterima = target_db.coin + int(coin)
                nama = "Admin" if anu.status == 'owner' or anu.status == 'admin' else msg.from_user.first_name
                nama = await helper.escapeHTML(nama)
                try:
                    await client.send_message(target, f"Coin berhasil ditambahkan senilai {coin} coin, cek /status\n└Oleh <a href='tg://user?id={msg.from_user.id}'>{nama}</a>")
                    await user_db.transfer_coin(ditransfer, diterima, target_db.coin_full, int(target))
                    await msg.reply(f'<i>berhasil transfer coin sebesar {coin} coin💰</i>', True)
                except Exception as e:
                    return await msg.reply_text(
                        text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}", quote=True,
                        parse_mode=enums.ParseMode.HTML
                    )
            else:
                return await msg.reply_text(
                    text=f"<i><a href='tg://user?id={str(target)}'>user</a> tidak terdaftar didatabase</i>", quote=True,
                    parse_mode=enums.ParseMode.HTML
                )
        else:
            return await msg.reply(f'<i>coin kamu ({my_coin}) tidak dapat transfer coin.</i>', True)