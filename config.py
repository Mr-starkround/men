import os

api_id = int(os.environ.get("API_ID", "21484185"))
api_hash = os.environ.get("API_HASH", "42589444b3ee86b1286f01d966989214")
bot_token = os.environ.get("BOT_TOKEN", "6872017467:AAFx_RzH9bGA13iolTAYJNJlDWUfLjQ_C14")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://Alexa:alexa@cluster0.h0zqfue.mongodb.net/true?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1002089195394"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1002098707945"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002088952110"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "6725628980"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_hapus = int(os.environ.get("BIAYA_HAPUS", "20"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#pft #pftt #mas|#mba|#story|#spill|#story|#pap").replace(" ", "|").lower()
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "<b>Hallo {mention}\n\nAnda harus bergabung di Channel & Group terlebih dahulu untuk mengirim pesan ke channel @JAWAFES. \n\nSilakan Join Ke Channel & Group dulu ⤵️</b>")
start_msg = os.environ.get("START_MSG", """
<b>❏ Haii {mention}

𝗝𝗮𝘄𝗮𝗳𝗲𝘀𝘀 𝗔𝘂𝘁𝗼 𝗽𝗼𝘀𝘁 akan membantumu mengirimkan pesan secara anonim ke channel @JAWAFES.

silahkan baca help dan rules terlebih dahulu</b>""")
# =========================================================== #

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, <b>Pesan anda gagal terkirim.\nsilahkan klik button help bila butuh bantuan</b>
""")
# =========================================================== #

topup_msg = os.environ.get("PESAN_TOPUP", """
❏ Haii {mention} \n\nJawafess coin di gunakan untuk biaya mengirim menfess/promote ke @JAWAFES jika batas kirim harian sudah habis. biaya untuk sekali mengirim adalah 25 coin. \ncoin akan berkurang secara otomatis jika batas harian sudah habis. <b>harga 100 coin = 1000 rupiah</b> \n\napabila batas kirim harian belum habis. coin tidak akan berkurang \n\n<b>❏ Cara Membeli Coin Jawafess:</b> \n├ 1. Salin format top up dibawah👇🏻👇🏻 \n├ 2. Klik /belicoin \n├ 3. save qris dan lakukan pembayaran. \n├ 4. kirimkan bukti pembayaran beserta format topup \n└ <b>BENEFIT TOPUP COIN JAWAFESS:</b> bisa kirim menfess sebanyak-banyaknya diluar batasan harian
""")