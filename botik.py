import telebot
from telebot import types
import random
import praw

bot = telebot.TeleBot("1162478993:AAGA5BQ4Sl0X1ZqcdoSBuMaZBfDthrUGTKo")
reddit = praw.Reddit(
    client_id='W7sixqSWXLXIow',
    client_secret='31MTHYwM_OhGMVtflj2pOpnp384',
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15',
    )
jokes = [
    "Plokhiye limony posle smerti popadayut v limonad.",
    "Est takaya lyubov, ot kotoroy sled v dushe ostayetsya na vsyu zhizn…",
    "Skachal knigu iz interneta – spas derevo.",
    "V zhizni nado byt upertym, no ne baranom.",
    "Lysyy ezhik nosit yablochki v ryukzachke.",
    "Ulybku daryu vsem. Vzglyad — nemnogim. Serdtse — odnoy.",
    "Tak byvayet, dazhe silnykh zhizn lomayet...",
    "Molchaniye — samyy gromkiy krik, potomu chto on rvet ne ushi, a serdtse.",
    "Brat, zapomni! Ya vstanu za teby, dazhe esli ty ne prav...",
    "Ya uzhe privykla k tomu, chto tebya tak mnogo v moikh mechtakh i tak malo v moyey zhizni.",
    "Lyubov prikhodit na tsypochkakh, a ukhodit, gromko khlopnuv dveryu.",
    "A ya ne ishchu svoyu vtoruyu polovinku… tak uzh vyshlo chto ya rodilas tseloy.",
    "Pust my zasypayem v raznykh krovatyakh — glavnoye, chto my zasypayem s myslyu drug o druge…",
    "Odnazhdy ty zaglyanesh v moi smeyushchiyesya glaza i zaplachesh.",
    "Sredi vsekh zapakhov sigaret v mire ona mogla nayti ego, tot, s aromatom vanili.",
    "V skazku khochu… Sakharnoye utro, marmeladnyy den i shokoladnaya noch…",
    "Tak khochetsya nochyu tebe pozvonit i skazat, chto ne spitsya.",
    ]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("/meme")
    markup.add(item1)
    bot.send_message(
        message.chat.id,
        f"Hi, <b>{message.from_user.first_name}</b>! \nWhat are we going to do 😏? You can press the button /meme or type something.",
        parse_mode='html',
        reply_markup=markup,
        )


def take_meme():
    mem = reddit.subreddit('memes').random()
    return mem


@bot.message_handler(commands=['meme'])
def send_meme(message):
    memu =take_meme()
    title = memu.title
    url = memu.url
    bot.send_photo(
        message.chat.id,
        url,
        title,
        )


@bot.message_handler(content_types=['text'])
def send_joke(message):
    bot.send_message(
        message.chat.id,
        random.choice(jokes),
        )


bot.polling()
