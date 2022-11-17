import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5695746454:AAGoZ9hApZ9fxo3PxdL-58IrcJbhG2cMr5I'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Вас приветствует ruslan_23_3_hw')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.chat.id, '/my_info\n/download_photo\n/show_movies\n/send_my_info')


@dp.message_handler(commands=['my_info'])
async def my_info(message: types.Message):
    await message.answer(
        f'id: {message.from_user.id}, first_name: {message.from_user.first_name}, last_name: {message.from_user.last_name}')


@dp.message_handler(commands=['download_photo'])
async def download_photo(message: types.Message):
    photos = (await bot.get_user_profile_photos(message.from_user.id))
    photo_file = await bot.get_file(photos['photos'][0][0]['file_id'])


@dp.message_handler(commands='show_movies')
async def show_movies(message: types.Message):
    await message.answer(
        'Фильмы:\nИнопланетянин (2022)\nБилет в рай (2022)\nКасабланка (2022)\nhttps://kinogo.io/')


@dp.message_handler(commands=['send_my_info'])
async def send_my_info(mesage: types.Message):
    arguments = mesage.text.split('\n')
    name = arguments[1]
    surname = arguments[2]
    age = arguments[3]
    hobby = arguments[4]
    movies = arguments[5]
    await mesage.answer(
        f'1. Вас зовут {name} {surname}\n2. Вам {age} лет\n3. Вы занимаетесь {hobby}\n4. Список ваших любимых фильмов {movies}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=Trulse)
