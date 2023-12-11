import asyncio

from pyrogram import Client
from pyrogram.types import (
    Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
)
from pyrogram.errors import (
    FloodWait, PeerIdInvalid, UserIsBlocked, InputUserDeactivated
)
from plugins import Database

async def broadcast_handler(client: Client, msg: Message):
    if msg.reply_to_message is None:
        await msg.reply('Harap reply sebuah pesan', True)

    else:
        anu = msg.reply_to_message
        anu = await anu.copy(msg.chat.id, reply_to_message_id=anu.id)
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('Ya', 'ya_confirm'), InlineKeyboardButton('Tidak', 'tidak_confirm')]
        ])
        await anu.reply('apakah kamu akan mengirimkan pesan broadcast ?', True, reply_markup=markup)

async def broadcast_ya(client: Client, query: CallbackQuery):
    msg = query.message
    db = Database(msg.from_user.id)
    if not msg.reply_to_message:
        await query.answer('Pesan tidak ditemukan', True)
        await query.message.delete()
        return
    message = msg.reply_to_message
    user_ids = db.get_pelanggan().id_pelanggan

    berhasil = 0
    dihapus = 0
    blokir = 0
    gagal = 0
    await msg.edit('Broadcast sedang berlangsung, tunggu sebentar', reply_markup = None)
    for user_id in user_ids:
        try:
            await msg.copy(user_id)
            berhasil += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await msg.copy(user_id)
            berhasil += 1
        except UserIsBlocked:
            blokir += 1
        except PeerIdInvalid:
            gagal += 1
        except InputUserDeactivated:
            dihapus += 1
            await db.hapus_pelanggan(user_id)
    text = f"""<b>Broadcast selesai</b>
    
Jumlah pengguna: {len(user_ids)}
Berhasil terkirim: {str(berhasil)}
Pengguna diblokir: {str(blokir)}
Akun yang dihapus: {str(dihapus)} (<i>Telah dihapus dari database</i>)
Gagal terkirim: {str(gagal)}"""

    await msg.reply(text)
    await msg.delete()
    await message.delete()

async def broadcast_ya(client: Bot, message: Message):
    if message.reply_to_message:
        query = await query_msg()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0

        pls_wait = await message.reply(
            "<code>Broadcasting Message Tunggu Sebentar...</code>"
        )
        for row in query:
            chat_id = int(row[0])
            if chat_id not in ADMINS:
                try:
                    await broadcast_msg.copy(chat_id, protect_content=PROTECT_CONTENT)
                    successful += 1
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await broadcast_msg.copy(chat_id, protect_content=PROTECT_CONTENT)
                    successful += 1
                except UserIsBlocked:
                    await delete_user(chat_id)
                    blocked += 1
                except InputUserDeactivated:
                    await delete_user(chat_id)
                    deleted += 1
                except BaseException:
                    unsuccessful += 1
                total += 1
        status = f"""<b><u>Berhasil Broadcast</u>
Jumlah Pengguna: <code>{total}</code>
Berhasil: <code>{successful}</code>
Gagal: <code>{unsuccessful}</code>
Pengguna diblokir: <code>{blocked}</code>
Akun Terhapus: <code>{deleted}</code></b>"""
        return await pls_wait.edit(status)
    else:
        msg = await message.reply(
            "<code>Gunakan Perintah ini Harus Sambil Reply ke pesan telegram yang ingin di Broadcast.</code>"
        )
        await asyncio.sleep(8)
        await msg.delete()


async def close_cbb(client: Client, query: CallbackQuery):
    try:
        await query.message.reply_to_message.delete()
    except:
        pass
    try:
        await query.message.delete()
    except:
        pass
