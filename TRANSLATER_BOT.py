from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import telebot
from googletrans import Translator
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN environment variable not set")

bot = telebot.TeleBot(BOT_TOKEN)
translator = Translator()

# Store user data
user_data = {}


@bot.message_handler(commands=['start'])
def start_command(message):
    markup = InlineKeyboardMarkup()
    btn_translate = InlineKeyboardButton("🗣️ Start Translation", callback_data='start_translation')
    markup.add(btn_translate)
    bot.send_message(message.chat.id, "💝 Welcome to the bot 💝"
                    "\n\n\n\nHello, we are so happy to join you.we can support you at translate your texts in 9 lnaguages :"
                    "\n\n🔎How can I help you about this options?"
                    "\n\n\n❗️AT first, you choose your own language.after that choose translated language, please.", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'start_translation')
def start_translation(call):
    translate_command(call.message)


@bot.message_handler(commands=['translate'])
def translate_command(message):
    markup = InlineKeyboardMarkup()
    btn_en = InlineKeyboardButton("🇺🇸 English", callback_data='src_lang_en')
    btn_fa = InlineKeyboardButton("🇮🇷 فارسی", callback_data='src_lang_fa')
    btn_fr = InlineKeyboardButton("🇫🇷 French", callback_data='src_lang_fr')
    btn_ko = InlineKeyboardButton("🇰🇷 Korea", callback_data='src_lang_ko')
    btn_es = InlineKeyboardButton("🇪🇸 Spanish", callback_data='src_lang_es')
    btn_sv = InlineKeyboardButton("🇸🇪 Swedish", callback_data='src_lang_sv')
    btn_zh = InlineKeyboardButton("🇨🇳 Chinese", callback_data='src_lang_zh')
    btn_tr = InlineKeyboardButton("🇹🇷 Turkish", callback_data='src_lang_tr')
    btn_ar = InlineKeyboardButton("🇸🇦 Arabic", callback_data='src_lang_ar')

    markup.add(btn_en, btn_fa, btn_fr, btn_ko, btn_es, btn_sv, btn_zh, btn_tr, btn_ar)
    bot.send_message(message.chat.id, "⭐️ Please select the source language ⭐️", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('src_lang_'))
def callback_source_language_selection(call):
    source_lang = call.data.split('_')[2]
    user_data[call.message.chat.id] = {'source': source_lang}

    # Prepare for target language selection
    markup = InlineKeyboardMarkup()
    btn_en = InlineKeyboardButton("🇺🇸 English", callback_data='tgt_lang_en')
    btn_fa = InlineKeyboardButton("🇮🇷 فارسی", callback_data='tgt_lang_fa')
    btn_fr = InlineKeyboardButton("🇫🇷 French", callback_data='tgt_lang_fr')
    btn_ko = InlineKeyboardButton("🇰🇷 Korea", callback_data='tgt_lang_ko')
    btn_es = InlineKeyboardButton("🇪🇸 Spanish", callback_data='tgt_lang_es')
    btn_sv = InlineKeyboardButton("🇸🇪 Swedish", callback_data='tgt_lang_sv')
    btn_zh = InlineKeyboardButton("🇨🇳 Chinese", callback_data='tgt_lang_zh')
    btn_tr = InlineKeyboardButton("🇹🇷 Turkish", callback_data='tgt_lang_tr')
    btn_ar = InlineKeyboardButton("🇸🇦 Arabic", callback_data='tgt_lang_ar')

    markup.add(btn_en, btn_fa, btn_fr, btn_ko, btn_es, btn_sv, btn_zh, btn_tr, btn_ar)
    bot.send_message(call.message.chat.id, "⭐️ Right now select the target language ⭐️", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('tgt_lang_'))
def callback_target_language_selection(call):
    target_lang = call.data.split('_')[2]
    user_data[call.message.chat.id]['target'] = target_lang

    bot.send_message(call.message.chat.id, "‼️Please send the text you want to translate:")


@bot.message_handler(func=lambda message: message.chat.id in user_data)
def receive_text_to_translate(message):
    user_info = user_data[message.chat.id]
    source_lang = user_info['source']
    target_lang = user_info['target']

    text_to_translate = message.text.strip()

    if text_to_translate:  # Check for empty input
        try:
            detected_lang = translator.detect(text_to_translate).lang

            # Check if the detected language matches the selected source language
            if detected_lang != source_lang:
                bot.reply_to(message, f"⚠️ Please send the text in {source_lang} for translation to {target_lang}.")
                return

            translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang).text
            bot.reply_to(message, f"🌍 Translation: {translation}")

        except Exception as e:
            bot.reply_to(message, f"❗️ An error occurred: {str(e)}")
    else:
        bot.reply_to(message, "⚠️ Please send a valid text to translate! ")


@bot.message_handler(func=lambda message: message.chat.id not in user_data)
def default_message(message):
    bot.reply_to(message, "❓ Please start by typing /translate to select a language.")


bot.infinity_polling()
