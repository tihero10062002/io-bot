import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject

from aiogram.enums.dice_emoji import DiceEmoji  # для эмоджи кубиков баскетбола и т д
from aiogram.types import Message

bot = Bot("6910038738:AAGMUECVTr7KkhD8_wS7JbGC0K72GmTAcVk", parse_mode="HTML")
dp = Dispatcher()


# @dp.message(F.text == "/start")
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Hello,{message.from_user.first_name}", parse_mode="HTML")

# игра в кости с записью значения в переменные
@dp.message(F.text== "play")
async def play_games(message:Message):
    x = await message.answer_dice(DiceEmoji.DICE)
    await message.reply(f"У вас выпало - {x.dice.value}")

@dp.message(Command(commands=["rn", "random-number"]))
async def get_random_number(message: Message, command: CommandObject):
    if command.args:
        a, b = [int(n) for n in command.args.split("-")]
        rnum = random.randint(a, b)
    else:
        await message.answer(f"Need two number , example :'10-20'")
    await message.reply(f"Random number: {rnum}")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
