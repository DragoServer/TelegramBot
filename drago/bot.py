import os
import json
import asyncio
import aiomysql
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

api_id = '26427483'
api_hash = '263a44e6d6e49383da08ccb75a2345c2'
bot_token = '7141372015:AAF71BfKj6sRCtqd4cHmsl0C3R48JYYoxD8'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

db_host = 'localhost'
db_user = 'dragoxs1_bgcl'
db_password = 'dragoxs1_bgcl'
db_name = 'dragoxs1_bgcl'

admin_chat_id = '1543260546'

async def get_db_connection():
    return await aiomysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name
    )

async def check_user_exists(chat_id):
    conn = await get_db_connection()
    async with conn.cursor() as cur:
        await cur.execute("SELECT `chat_id` FROM `users` WHERE `chat_id` = %s", (chat_id,))
        result = await cur.fetchone()
        await conn.close()
        return result

async def add_new_user(username, chat_id):
    conn = await get_db_connection()
    async with conn.cursor() as cur:
        await cur.execute("INSERT INTO `users` (`username`, `chat_id`, `funds`) VALUES (%s, %s, 0)", (username, chat_id))
        await conn.commit()
        await conn.close()

def get_welcome_message(username):
    return f"""
<b>Welcome to BGCL BGMI LOADER the best place to buy injector and loader for BGMI

👑BGCL BGMI LOADER+MOD+INJECTOR👑

🌟𝗡𝗼 𝗔𝗻𝘆 𝗕𝗮𝗻 𝗜𝘀𝘀𝘂 ✅
🌟𝗡𝗼 𝗔𝗻𝘆 𝗖𝗿𝗮𝘀𝗵 𝗜𝘀𝘂𝗲 ✅
🌟𝗡𝗼 𝗔𝗻𝘆 𝗡𝗲𝘁𝘄𝗼𝗿𝗸 𝗘𝗿𝗿𝗼𝗿 ✅
🌟𝗠𝗮𝗶𝗻 𝗜𝗗 𝗼𝘁𝗮𝗹 𝗦𝗮𝗳 𝟭𝟬𝟬% ✅
🌟𝗔𝗹 𝗔𝗻𝗱𝗿𝗼𝗶 𝟵 𝗧𝗼 𝟭𝟱 𝗦𝗽𝗽𝗼𝗿𝘁 ✅
🌟𝗼𝘁𝗵 𝟯𝟮 𝗕𝘁 & 𝟲𝟰 𝗕𝗶𝘁 𝘂𝗽𝗽𝗼𝗿𝘁 ✅
🌟𝗕𝗼𝘁𝗵 𝗥𝗼𝗼𝘁 & 𝗡𝗼 𝗥𝗼𝗼𝘁 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ✅

⚡️𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌:-
➡️ Pʟᴀʏᴇʀ ESP ✅
➡️ Aʟʟ Iᴛᴇᴍs ESP ✅
➡️ Vᴇʜɪᴄʟᴇs ESP ✅
➡️ Sᴍᴏᴏᴛ Aɪᴍʙᴏᴛ ✅
➡️ Cᴏɴᴛʀᴏʟ Rᴇᴄᴏɪʟ ✅
➡️ Sᴍᴏᴏᴛʜ Gᴀᴍᴘʟᴀʏ ✅

👑𝗣𝗿𝗶𝗰𝗲 𝗟𝗶𝘀𝘁:-
✅ 𝟣 𝖣𝖺𝗒:- 𝖱𝗌. 150 ✅
✅ 3 𝖣𝖺𝗒s:- 𝖱𝗌. 300 ✅
✅ 𝟣 𝖶𝖾𝗄:- 𝖱𝗌. 400 ✅
✅ 𝟣 𝖬𝗈𝗇𝗍𝗁:- 𝖱𝗌. 1200 ✅


✔️ 𝘿𝙈 𝙏𝙤 𝘽𝙪𝙮:-
@Bgcltamil</b>
"""

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    chat_id = message.chat.id
    username = message.from_user.username

    # Define the keyboard layout
    keyboard = [
        ['Buy Injector (Android 10-13) Keys', 'Buy Mod Keys'],
        ['Buy Loader (Android 14) Keys', 'DDOS'],
        ['My Balance', 'Redeem Code'],
        ['Add Funds', 'Contact Admin']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Check if user exists
    user_exists = await check_user_exists(chat_id)
    if user_exists:
        welcome_message = get_welcome_message(username)
        await message.reply_text(welcome_message, parse_mode='HTML', reply_markup=reply_markup)
    else:
        welcome_message = get_welcome_message(username)
        await message.reply_text(welcome_message, parse_mode='HTML', reply_markup=reply_markup)

        await add_new_user(username, chat_id)

        # Update user count
        file_path = 'admin/users.txt'
        with open(file_path, 'r') as file:
            current_count = int(file.read())
        new_count = current_count + 1
        with open(file_path, 'w') as file:
            file.write(str(new_count))

        # Notify admin
        admin_message = f"<b>NEW USER JOINED THE BOT</b>\n\n<b>USER ID:</b> <pre>{chat_id}</pre>\n\n<b>USERNAME: @{username}</b>"
        await client.send_message(admin_chat_id, admin_message, parse_mode='HTML')

def main():
    app.run()

if __name__ == "__main__":
    main()

