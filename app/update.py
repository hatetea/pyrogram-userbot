from app.log import Logger
logger = Logger()
async def add_user(group_users):
	user_list = ""
	counter = 0
	for user in group_users:
		counter += 1
		user_list += f"{user}\n"
	with open('locales/users.txt', 'a+', encoding='utf-8') as f:
		f.write(user_list)
		logger.log_info(f"file updated.")
	return counter

# ---------------------------
async def get_chat_usernames(chat_id, app):
	usernames = set()
	counter = 0
	with open('locales/users.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
		async for message in app.get_chat_history(chat_id):
			if message.from_user and message.from_user not in lines:
				counter += 1
				usernames.add(message.from_user.id)
				logger.log_info(f"{len(message.from_user.id)} new usernames added to the file.")
				if counter == 100:
					break
	return usernames