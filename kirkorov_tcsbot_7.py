import asyncio
from asyncio import sleep
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, message
from aiogram.filters import Command
import random
from db import Database
from aiogram.enums import ParseMode
import config
import sys
import logging


bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
db = Database('database')


# /start
@dp.message(Command('start'))
async def start(message: Message):
    await update_bd(message)
    await bot.send_message(chat_id=message.chat.id, text='🎩 Бот Киркоров - отличное дополнение для вашего чата, чтобы поднять настроение в команде.\n\n\n🖐️ Доброго времени суток!\n💻 Разработчик бота - Алексей Самарин\n⚙️ Бот написан на языке Python\n🕹️ Хостится на оклад спеца\n🍽️ Поддержать проект <a href="https://www.tinkoff.ru/rm/samarin.aleksey61/jpgEd88277">можно здесь</a>\n💡 По вопросам и предложениям @Lesha_Samarin\n\n🗨️ Реагирует на следующий текст: Да, Нет, Можно(?), Пизда, Пидора ответ, Спасибо, Бля, Бл, Блять, Доброе утро, Доброе, Такси, Хорошо, Фуи, Fyi\n🎲 Шанс выпадения некоторых отговорок установлен на 70% (чтобы не надоедал бот).\n\n🚀 Бот будет развиваться и обновляться. О новых фичах жди сообщения.')
    await bot.send_message(chat_id=message.chat.id, text='🔥 Обновление от 16.11.2023. 🔥\n⚙️ Текущее обновление больше техническое.\n\n🧾 1. Обновлён словарь касаний:\n             - Новые отговорки (ищите сами🤞).\n🗯️ 2. Рандом ответов поднят до 70%.\n🤖 3. Технические улучшение:\n             - Реализована БД SQL,\n             - Реализована рассылка пушей по группам(для обновлений),\n             - Оптимизация кода.')


@dp.message(Command('sendall'))
async def sendall(message: Message):
    if message.chat.type == 'private':
        if message.from_user.id == 730189336:
            text = message.text[9:]
            users = db.get_chats()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                    await sleep(0.5)
                except:
                    db.set_active(row[0], 0)
            await bot.send_message(message.from_user.id, 'Рассылка окончена')


# Можно
@dp.message(F.text.lower() == 'можно')
async def mojno(message: Message):
    await update_bd(message)
    await message.reply(f'Нет, но можно Дашку за ляжку')  # ответ форвардом (.answer без форварда)



# Да
@dp.message((F.text.lower() == 'да') | (F.text.lower() == 'да)') | (F.text.lower() == 'да))'))
async def da(message: Message):
    await update_bd(message)
    rnd_number = random.randint(1, 100)
    if rnd_number <= 70:
        await message.reply(f'Пизда!')  # ответ форвардом (.answer без форварда)



# Нет
@dp.message((F.text.lower() == 'нет') | (F.text.lower() == 'нет)') | (F.text.lower() == 'нет))'))
async def net(message: Message):
    await update_bd(message)
    rnd_number = random.randint(1, 100)
    if rnd_number <= 70:
        rnd_otvet = random.randint(1, 2)
        if rnd_otvet == 1:
            await message.reply(f'Пидора ответ!')
        else:
            await message.reply(f'Нет! Согласен! Три хуя в жопу не засунешь!')


# Пидора ответ
@dp.message(F.text.lower() == 'пидора ответ')
async def pidora_otvet(message: Message):
    await update_bd(message)
    await message.reply(f'Шлюхи аргумент!')  # ответ форвардом (.answer без форварда)


# Блять
@dp.message((F.text.lower() == ('бл')) | (F.text.lower() == ('бля')) | (F.text.lower() == ('блять')))
async def blat(message: Message):
    await update_bd(message)
    await message.reply(f'Ирина! Ёп твою мать!')  # ответ форвардом (.answer без форварда)


# Спасибо
@dp.message((F.text.lower() == ('спасибо')) | (F.text.lower() == ('спс')))
async def sps(message: Message):
    await update_bd(message)
    rnd_number = random.randint(1, 100)
    if rnd_number <= 70:
        await message.reply(f'Задержись сегодня, отработаешь после смены')  # ответ форвардом (.answer без форварда)


# Contains!
# Доброе утро
@dp.message(F.text.lower().contains('доброе утро') | (F.text.lower() == 'доброе'))
async def dobroe(message: Message):
    await update_bd(message)
    rnd_number = random.randint(1, 100)
    if rnd_number <= 70:
        rnd_otvet = random.randint(1, 6)
        if rnd_otvet == 1:
            await message.reply(f'Доброе калеки!')  # ответ форвардом (.answer без форварда)
        elif rnd_otvet == 3:
            await message.reply(f'Сдобного дня крепыши!')  # ответ форвардом (.answer без форварда)
        elif rnd_otvet == 4:
            await message.reply(f'Приветствую хрезантемки')  # ответ форвардом (.answer без форварда)
        elif rnd_otvet == 5:
            await message.reply(f'Пока!')  # ответ форвардом (.answer без форварда)
        else:
            await message.reply(f'Пока то оно доброе, согласен. Но если сегодня накосячишь, начальство тебя выебет')  # ответ форвардом (.answer без форварда)


# taxi
@dp.message(F.text.lower().contains('такси'))
async def taxi(message: Message):
    await update_bd(message)
    rnd_number = random.randint(1, 100)
    if rnd_number <= 70:
        await message.reply(f'Смотри, опять потом без денег будешь хуй сосать')  # ответ форвардом (.answer без форварда)


# Хорошо
@dp.message(F.text.lower().contains('хорошо'))
async def good(message: Message):
    await update_bd(message)
    await message.reply(f'Чтобы в райдере остались фисташки - нужно не хорошо, а идеально!')


# fyi
@dp.message(F.text.lower().contains('fyi') | F.text.lower().contains('фуи'))
async def fyi(message: Message):
    await update_bd(message)
    await message.reply(f'Фуи - фор ю хуи')  # ответ форвардом (.answer без форварда)


# Пизда
@dp.message(F.text.lower().contains('пизда'))
async def pizda(message: Message):
    await update_bd(message)
    rnd_number = random.randint(1, 100)
    if rnd_number <= 70:
        rnd_otvet = random.randint(1, 5)
        if rnd_otvet == 1:
            await message.reply(f'Ты меня своей пиздой не пугай, могу и свою скинуть')  # ответ форвардом (.answer без форварда)
        elif rnd_otvet == 2:
            await message.reply(f'Согласен пизда пиздец')
        elif rnd_otvet == 3:
            await message.reply(f'Жду фото твоей пизды в личке')
        elif rnd_otvet == 4:
            await message.reply(f'Заебали вы этой пиздой. Всё, кидаю свою!')
        else:
            await message.reply(f'В поле ветер, а в пизде дым!')


async def update_bd(message):#update database
    if message.chat.type == 'private':
        if not db.user_exists(message.chat.id):
            db.add_user(message.chat.id, message.chat.type, message.chat.first_name, message.chat.last_name,
                        message.chat.username)
    else:
        if not db.chat_exists(message.chat.id):
            db.add_chat(message.chat.id, message.chat.type)


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
