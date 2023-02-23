from pyrogram import filters
from app.log import Logger
from app.update import add_user, get_chat_usernames
from loader import app

logger = Logger()

@app.on_message(filters.command(['help'], prefixes=['/', '!', '.']) & filters.me)
async def help(_, message):
	"""
	## Handler for the message help
	
	"""
	await message.edit('📄help\n\n/getusers - update list of users\n/run - run script')
	


@app.on_message(filters.command(['getusers'], prefixes=['/', '!', '.']) & filters.me)
async def get_users_from_group(_, message):
	"""
	## Handler for the message getusers
	
	"""
	group_users = await get_chat_usernames('chat_id', app)
	counter = await add_user(group_users)
	await message.edit(f"**🤖List of user updated**\n📄__Was added: ```{counter}``` usesrs__\n\n❕type ```{message.text}``` to continue")

@app.on_message(filters.command(['run'], prefixes=['/', '!', '.']) & filters.me)
async def run(_, message):
	"""
	## Handler for the message run
	
	"""

	text = "Just text"
	

	with open('locales/users.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for user_id in lines:
			await app.send_message(int(user_id), text)


	await message.edit("🤖Script finished!")

"""
by consentantanneity

"""

app.run()
