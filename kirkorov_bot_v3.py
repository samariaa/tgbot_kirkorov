import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, message
from aiogram.filters import Command, CommandStart
import random
import emoji
from aiogram.enums import ParseMode
import test_token

bot = Bot(test_token.TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


#/start
@dp.message(Command('start'))
async def start(message: Message):
    await bot.send_message(chat_id=message.chat.id, text=(emoji.emojize(':top_hat: ')) + 'Бот Киркоров - отличное дополнение для вашего чата, чтобы поднять настроение в команде.\n\n\n' + (emoji.emojize(':hand_with_fingers_splayed: ')) + 'Доброго времени суток!\n' + (emoji.emojize(':gear: ')) + 'Разработчик бота - Алексей Самарин\n' + (emoji.emojize(':brick: ')) + 'Бот написан на языке Python\n' + (emoji.emojize(':money_with_wings: ')) +'Хостится на оклад спеца\n' + (emoji.emojize(':pushpin: ')) + 'Поддержать проект <a href="https://www.tinkoff.ru/rm/samarin.aleksey61/jpgEd88277">можно здесь\n</a>' + (emoji.emojize(':incoming_envelope: ')) + 'По вопросам и предложениям @Lesha_Samarin\n\n' + (emoji.emojize(':check_mark_button: ')) + 'Реагирует на следующий текст: Да, Нет, Можно(?), Пизда, Пидора ответ, Спасибо.\n' + (emoji.emojize(':bar_chart: ')) + 'Шанс выпадения отговорок на: Да, Нет, Пизда, Спасибо - составляет 40% (чтобы не надоедал бот).\n\n' + (emoji.emojize(':thread: ')) + 'Бот будет развиваться и обновляться. О новых фичах жди сообщения.')
    await bot.send_message(chat_id=message.chat.id, text=(emoji.emojize(':collision: ')) + 'Обновление от 10.10.2023' + (emoji.emojize(' :collision:')) + '\n\n' + (emoji.emojize(':computer_mouse: ')) + '1. Отключение учёта регистра - теперь бот реагирует на ваши сообщения, вне зависимости написано сообщение с маленькой или большой буквы.\n\n' + (emoji.emojize(':robot: ')) + '2. Обновлены касания:\n' + (emoji.emojize(':chart_increasing: ')) + '2.1 Переработан старый словарь взаимодействий.\n' + (emoji.emojize(':chart_increasing: ')) + '2.2 Новый словарь взаимодействий. Новые слова: бля, бл, блять, доброе утро, доброе, такси, хорошо, фуи, fyi.\n' + (emoji.emojize(':chart_increasing: ')) + '2.3 На некоторые взаимодействия, например на доброе утро сделан рандом из 4-х разных ответов.\n' + (emoji.emojize(':chart_increasing: ')) + '2.4 Некоторые взаимодействия учитываются в контексте. Например, бот среагирует на любое сообщение если в нем используется фраза "Доброе утро".\n' + (emoji.emojize(':chart_increasing: ')) + '2.5 На некоторые новые взаимодействия также включен рандом 40% шанса выпадения ответа.\n' + (emoji.emojize(':chart_increasing: ')) + '2.6 На некоторые взаимодействия, например на доброе утро сделан рандом из 4-х разных ответов.\n\n' + (emoji.emojize(':writing_hand: ')) + '3. Оптимизация кода и использование новых методов.\n')



#Можно
@dp.message(F.text.lower() == 'можно')
async def mojno(message: Message):
    await message.reply(f'Нет, но можно Дашку за ляжку')  # ответ форвардом (.answer без форварда)


#Да
@dp.message((F.text.lower() == 'да') | (F.text.lower() == 'да)') | (F.text.lower() == 'да))'))
async def da(message: Message):
    rnd_number = random.randint(1, 100)
    if rnd_number <= 40:
     await message.reply(f'Пизда!')  # ответ форвардом (.answer без форварда)


#Нет
@dp.message((F.text.lower() == 'нет') | (F.text.lower() == 'нет)') | (F.text.lower() == 'нет))'))
async def net(message: Message):
    rnd_number = random.randint(1, 100)
    if rnd_number <= 40:
     await message.reply(f'Пидора ответ!')  # ответ форвардом (.answer без форварда)


#Пидора ответ
@dp.message(F.text.lower() == 'пидора ответ')
async def pidora_otvet(message: Message):
     await message.reply(f'Шлюхи аргумент!')  # ответ форвардом (.answer без форварда)


#Блять
@dp.message((F.text.lower() == ('бл')) | (F.text.lower() == ('бля')) | (F.text.lower() == ('блять')))
async def blat(message: Message):
     await message.reply(f'Ирина! Ёп твою мать!')  # ответ форвардом (.answer без форварда)


#Спасибо
@dp.message((F.text.lower() == ('спасибо')) | (F.text.lower() == ('спс')))
async def sps(message: Message):
    rnd_number = random.randint(1, 100)
    if rnd_number <= 40:
     await message.reply(f'Задержись сегодня, отработаешь после смены')  # ответ форвардом (.answer без форварда)

#Contains!
#Доброе утро
@dp.message(F.text.lower().contains('доброе утро') | (F.text.lower() == 'доброе'))
async def dobroe(message: Message):
    rnd_number = random.randint(1, 100)
    if rnd_number <= 40:
     rnd_otvet = random.randint(1, 4)
     if rnd_otvet == 1:
         await message.reply(f'Доброе калеки!')  # ответ форвардом (.answer без форварда)
     elif rnd_otvet == 3:
         await message.reply(f'Сдобного дня крепыши!')  # ответ форвардом (.answer без форварда)
     elif rnd_otvet == 4:
         await message.reply(f'Приветствую хрезантемки')  # ответ форвардом (.answer без форварда)
     else:
         await message.reply(f'Пока!')  # ответ форвардом (.answer без форварда)


#taxi
@dp.message(F.text.lower().contains('такси'))
async def taxi(message: Message):
    rnd_number = random.randint(1, 100)
    if rnd_number <= 40:
     await message.reply(f'Смотри, опять потом без денег будешь хуй сосать')  # ответ форвардом (.answer без форварда)


#Хорошо
@dp.message(F.text.lower().contains('хорошо'))
async def good(message: Message):
    await message.reply(f'Чтобы в райдере остались фисташки - нужно не хорошо, а идеально!')  # ответ форвардом (.answer без форварда)


#fyi
@dp.message(F.text.lower().contains('fyi') | F.text.lower().contains('фуи'))
async def fyi(message: Message):
    await message.reply(f'Фуи - фор ю хуи')  # ответ форвардом (.answer без форварда)


#Пизда
@dp.message(F.text.lower().contains('пизда'))
async def pizda(message: Message):
    rnd_number = random.randint(1, 100)
    if rnd_number <= 40:
     await message.reply(f'Ты меня своей пиздой не пугай, могу и свою скинуть')  # ответ форвардом (.answer без форварда)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())