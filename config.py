import os

api_id = int(os.environ.get("API_ID", "22132140"))
api_hash = os.environ.get("API_HASH", "326ba61167a7513e85c9d8699b345b75")
bot_token = os.environ.get("BOT_TOKEN", "6383063886:AAFfUkOPAYulvGGK5b8javiqkf8geDGmj98")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://agathanokos7:agatha@cluster0.kkrnzjx.mongodb.net/True?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1002059058977"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001997635982"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002001435040"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1020381855"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_hapus = int(os.environ.get("BIAYA_HAPUS", "25"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#mas #mba #story #spill #story #pap").replace(" ").lower()
# =========================================================== #

start_msg = os.environ.get("START_MSG", """
<b>❏ Haii</b> {mention}

<b>𝗝𝗮𝘄𝗮𝗳𝗲𝘀𝘀 𝗔𝘂𝘁𝗼 𝗽𝗼𝘀𝘁 akan membantumu mengirimkan pesan secara anonim ke channel @JAWAFES.

silahkan baca help dan rules terlebih dahulu</b>""")
# =========================================================== #

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, <b>Pesan anda gagal terkirim.\nsilahkan klik button help bila butuh bantuan</b>
""")
# =========================================================== #

topup_msg = os.environ.get("PESAN_TOPUP", """
Jawafess coin di gunakan untuk biaya mengirim menfess/promote ke @JAWAFES jika 3x batas kirim harian sudah habis. biaya untuk sekali mengirim adalah 25 coin.

❏ Cara Membeli Coin Jawafess
├1. klik button top up dibawah ini
├2. kirim bukti pembayaran anda <a href='https://t.me/GJNadminbot?start=start'>disini</a>
├3. nama [ nama telegram anda ]
└4. code topup anda » <code>jawafess {id} </code>

coin akan berkurang secara otomatis jika batas harian sudah habis. <b>harga 100 coin = 1000 rupiah</b>
""")
