import telebot
bot = telebot.TeleBot('1430146186:AAGCeO9FFaRsSEh8wLa0C1nJKABZ_9F302w')
from telebot import types
@bot.message_handler(commands=['help'])
def helper(message):
	bot.send_message(message.from_user.id, "Make sure that you have no contraindications to sports. You are responsible for your actions. Always warm up before training. Follow the safety instructions.")

@bot.message_handler(commands=['start'])
def start_handler(message):
	bot.send_message(message.from_user.id, "Well, let's get started")
	keyboard1 = telebot.types.ReplyKeyboardMarkup()
	keyboard1.row('Go', 'help')
	bot.send_message(message.chat.id, 'Press on one of these button', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def get_goal(message):
	if message.text == 'Next' or message.text == 'next' or message.text == 'Go':

		bot.send_message(message.from_user.id, "Hello my friend. Well, you decided to improve yourself.")

		keyboard = types.InlineKeyboardMarkup()

		key_weight_loss = types.InlineKeyboardButton(text='Weight loss (FOR MALE)', callback_data='weight')
		keyboard.add(key_weight_loss)
		key_build_muscle = types.InlineKeyboardButton(text='Build Muscle (FOR MALE)', callback_data='muscle')
		keyboard.add(key_build_muscle)
		key_weight_loss = types.InlineKeyboardButton(text='Weight loss (FOR FEMALE)', callback_data='weight_f')
		keyboard.add(key_weight_loss)
		key_build_muscle = types.InlineKeyboardButton(text='Build Muscle (FOR FEMALE)', callback_data='muscle_f')
		keyboard.add(key_build_muscle)

		bot.send_message(message.from_user.id, text='What is your goal?', reply_markup=keyboard)
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "Type 'Next' or 'next'")
	else:
		pass


@bot.callback_query_handler(func=lambda call: True)
def callback_work(call):
	if call.data == "weight":
		bot.send_message(call.message.chat.id, "The presented weight loss training at home is intended for people who do not have sports equipment. Despite the lack of shells, classes are no less effective and productive. The most important thing is to warm up well and strictly follow the techniques of each exercise."
			   "You'll find 9 exercises (8 exercises in total, but the last exercise is performed first on the right side, then on the left) + 1 minute of rest after completion. This means about 10 min for 1 lap.\nPerform the exercises for the specified time sequentially one after another, then repeat the training from the beginning in 3-4 circles. Beginners can complete 2 laps."
			   "\nOptions for performing circular training:\n>>>>>>>>>>By time:\n45 seconds of work / 15 seconds of rest\n>>>>>>>>>>By number of repetitions:\nspecified in the article after each exercise"
			   "\n1. PUSH-UPS + PULL-UPS:\nTaking the emphasis lying down, press down, almost touching the surface of the floor. Keep your back straight and look straight ahead. When you return to the starting phase, pull your arms up to your chest one at a time, pulling your elbows back. After lifting your hands, repeat the process again. If you find it difficult to perform push-UPS, get down on your knees or push-UPS from the bench.)"
			   "\n2. LUNGES FORWARD:\nPut your hands on your waist and your feet a little narrower than your shoulders. Step forward, bending the leg at the knee to a right angle. The foot stands firmly on the foot. The foot behind stands on the toe, and the knee does not touch the floor. The back is tense, fixed straight, does not slouch. Get up and repeat with the other leg.)"
			   "\n3. 'GOOD MORNING':\nStand with your hands behind your head. Bend your knees slightly and tilt your body forward to a 90-degree angle. At the same time, do not slouch, straighten your shoulders, keep a natural deflection in the lower back. Stretching from the lower point to the upper, rely only on the work of the back muscles.)"
			   "\n5. KNEE-ELBOW TWIST:\nIn the standing position, place your hands on the back of your head. Feet are shoulder-width apart. Alternately stretch the opposite elbows and knees to each other at the level below the chest, turning the body. Take your time, making short pauses at the peak point.)"
			   "\n6. STATIC SQUAT:\nDo this with your back straight and your feet shoulder-width apart. Hold in the lower position, observing the right angle in the knee joint. Extend your arms forward for better balance.)"
			   "\n7. SPIDER PLANK:\nTake the position of the bar at arm's length, put your feet next to each other. Now alternately stretch your right and left knees to the elbows of your hands, emphasizing the work of the lateral abdominal muscles. The back and lower back do not bend, forming a straight line.)"
			   "\n8. HAND TOUCH OF THE FOOT:\nLie down on the gym carpet and spread your arms out to the sides. The legs are also slightly apart. Now pull your right leg up while reaching for her foot with your left hand. Look directly at the ceiling without turning your head. Back in the starting phase, switch sides.)")
		# sendPhoto
		photo1 = open("PUSH-PULL.png", 'rb')
		bot.send_photo(call.from_user.id, photo1)
		bot.send_message(call.message.chat.id, "1. PUSH-UPS + PULL-UPS")
		#
		photo2 = open("LUNGES FORWARD.png", 'rb')
		bot.send_photo(call.from_user.id, photo2)
		bot.send_message(call.message.chat.id, "2. LUNGES FORWARD")
		#
		photo3 = open("GOOD MORNING.png", 'rb')
		bot.send_photo(call.from_user.id, photo3)
		bot.send_message(call.message.chat.id, "3. 'GOOD MORNING'")
		#
		photo4 = open("KNEE-ELBOW TWIST.png", 'rb')
		bot.send_photo(call.from_user.id, photo4)
		bot.send_message(call.message.chat.id, "5. KNEE-ELBOW TWIST")
		#
		photo5 = open("STATIC SQUAT.png", 'rb')
		bot.send_photo(call.from_user.id, photo5)
		bot.send_message(call.message.chat.id, "6. STATIC SQUAT")
		#
		photo6 = open("SPIDER PLANK.png", 'rb')
		bot.send_photo(call.from_user.id, photo6)
		bot.send_message(call.message.chat.id, "7. SPIDER PLANK")
		#
		photo7 = open("HAND TOUCH OF THE FOOT.png", 'rb')
		bot.send_photo(call.from_user.id, photo7)
		bot.send_message(call.message.chat.id, "8. HAND TOUCH OF THE FOOT")

	elif call.data == "muscle":
		bot.send_message(call.from_user.id, "What are we going to pump today?")

		keyboard = types.InlineKeyboardMarkup()

		key_legs = types.InlineKeyboardButton(text='Leg training', callback_data='leg')
		keyboard.add(key_legs)
		key_press = types.InlineKeyboardButton(text='Press training', callback_data='press')
		keyboard.add(key_press)
		key_chest = types.InlineKeyboardButton(text='Back training', callback_data='back')
		keyboard.add(key_chest)
		bot.send_message(call.from_user.id, text='Choose what you want', reply_markup=keyboard)
	elif call.data == "leg":
		bot.send_message(call.message.chat.id, "Exercise 'Pistol':\nApproaches: 3\nReplays: 14\nRest: 30 seconds\n(We stand with our legs narrowly apart and lift one of them off the floor. After that, bend the leg on which we stand at the knee and squat as low as possible, trying to keep your back straight. Now push off and return to the starting position, change the leg and repeat)."
											   "\n============================="
											   "\nBurpee:\nApproaches: 3\nReplays: 20\nRest: 30 seconds"
											   "\n============================="
											   "\n\nWalking on your hands against the wall:\nApproaches: 3\nReplays: 10\nRest: 30 seconds\n(We take a position on our hands (standing on our hands) with our feet leaning against the wall. Now move your hands forward and 'go' down the wall until your feet reach the floor.)"
											   "\n============================="
											   "\n\nJumping to the side:\nApproaches: 3\nReplays: 30\nRest: 30 seconds\n(We stand with our feet shoulder-width apart. Then we go down and abruptly push off from the floor with our right foot in order to jump to the left side and land on the left foot. Immediately after landing, push off with your left foot and repeat the movement, this time to the right Side)"
											   "\n============================="
											   "\n\nThe long jump from the place:\nApproaches: 3\nReplays: 8\nRest: 30 seconds\n(We go down to the squat position with our feet shoulder-width apart. We pull our arms back and use them to push ourselves forward when jumping, and for additional inertia, we throw our legs in front of us. We jump as far as possible and land on the soles of our feet.)")
		photo0 = open("Pistol.png", 'rb')
		bot.send_photo(call.from_user.id, photo0)
		bot.send_message(call.message.chat.id, "Exercise 'Pistol'")
		###########################################################
		photo1 = open("one.png", 'rb')
		bot.send_photo(call.from_user.id, photo1)
		############################################################
		photo2 = open("two.png", 'rb')
		bot.send_photo(call.from_user.id, photo2)
		###############################################################
		photo3 = open("three.png", 'rb')
		bot.send_photo(call.from_user.id, photo3)
		bot.send_message(call.message.chat.id, "Exercise 'Burpee'")
		############################################################
		photo4 = open("w1.png", 'rb')
		bot.send_photo(call.from_user.id, photo4)
		################################################################
		photo5 = open("w2.png", 'rb')
		bot.send_photo(call.from_user.id, photo5)
		bot.send_message(call.message.chat.id, "Walking on your hands against the wall")
		###########################################################
		photo6 = open("j1.png", 'rb')
		bot.send_photo(call.from_user.id, photo6)
		####################################################################
		photo7 = open("j2.png", 'rb')
		bot.send_photo(call.from_user.id, photo7)
		bot.send_message(call.message.chat.id, "Jumping to the side")
		##################################################################
		photo8 = open("l1.png", 'rb')
		bot.send_photo(call.from_user.id, photo8)
		###############################################################
		photo9 = open("l2.png", 'rb')
		bot.send_photo(call.from_user.id, photo9)
		bot.send_message(call.message.chat.id, "Jumping to the side")

	elif call.data == "press":
		bot.send_message(call.message.chat.id, "Reverse twists:\nApproaches: 5\nReplays: 60\nRest: 120 seconds\n(lie on your back with your hands on the floor at your sides, palms facing down. We bend the knees and pull them to the chest, squeezing the abdominal muscles. At the same time, lift your hips off the floor. In the upper position of the movement, squeeze the muscles, and then slowly lower until the hips are perpendicular to the floor.)"
											   "\n============================="
											   "\n\nSit-UPS:\nApproaches: 5\nReplays: 60\nRest: 120 seconds\n(We lie down on the floor and bend our knees. If possible, fix the feet under any object, so that the legs do not move when performing the exercise. Hold your hands behind your head and lift your torso, straining your abdominal muscles. As a result, the upper body and thighs should have the shape of the Latin letter V.)"
											   "\n============================="
											   "\n\n'Rock climber':Approaches: 5\nReplays: 60\nRest: 120 seconds\n(We take a position on the floor (similar to the position of a Sprinter on the starting lane - one leg is bent at the knee so that the foot is directly under the waist, and the other is straightened behind. Now abruptly change the position of the legs)")
	elif call.data == "back":
		bot.send_message(call.message.chat.id, "Exercise 'Superman':\nApproaches: 3\nReplays: 30\nRest: 30 seconds\n(Lie on your stomach, stretch your arms above your head, stretch out and lift your chest and knees off the floor. Hold for 3-5 seconds and return to the starting position)")
	elif call.data == "weight_f":
		bot.send_message(call.message.chat.id,  "The presented weight loss training at home is intended for people who do not have sports equipment. Despite the lack of shells, classes are no less effective and productive. The most important thing is to warm up well and strictly follow the techniques of each exercise."
			   "You'll find 9 exercises (8 exercises in total, but the last exercise is performed first on the right side, then on the left) + 1 minute of rest after completion. This means about 10 min for 1 lap.\nPerform the exercises for the specified time sequentially one after another, then repeat the training from the beginning in 3-4 circles. Beginners can complete 2 laps."
			   "\nOptions for performing circular training:\n>>>>>>>>>>By time:\n45 seconds of work / 15 seconds of rest\n>>>>>>>>>>By number of repetitions:\nspecified in the article after each exercise"
			   "\n1. PUSH-UPS + PULL-UPS:\nTaking the emphasis lying down, press down, almost touching the surface of the floor. Keep your back straight and look straight ahead. When you return to the starting phase, pull your arms up to your chest one at a time, pulling your elbows back. After lifting your hands, repeat the process again. If you find it difficult to perform push-UPS, get down on your knees or push-UPS from the bench.)"
			   "\n2. LUNGES FORWARD:\nPut your hands on your waist and your feet a little narrower than your shoulders. Step forward, bending the leg at the knee to a right angle. The foot stands firmly on the foot. The foot behind stands on the toe, and the knee does not touch the floor. The back is tense, fixed straight, does not slouch. Get up and repeat with the other leg.)"
			   "\n3. 'GOOD MORNING':\nStand with your hands behind your head. Bend your knees slightly and tilt your body forward to a 90-degree angle. At the same time, do not slouch, straighten your shoulders, keep a natural deflection in the lower back. Stretching from the lower point to the upper, rely only on the work of the back muscles.)"
			   "\n5. KNEE-ELBOW TWIST:\nIn the standing position, place your hands on the back of your head. Feet are shoulder-width apart. Alternately stretch the opposite elbows and knees to each other at the level below the chest, turning the body. Take your time, making short pauses at the peak point.)"
			   "\n6. STATIC SQUAT:\nDo this with your back straight and your feet shoulder-width apart. Hold in the lower position, observing the right angle in the knee joint. Extend your arms forward for better balance.)"
			   "\n7. SPIDER PLANK:\nTake the position of the bar at arm's length, put your feet next to each other. Now alternately stretch your right and left knees to the elbows of your hands, emphasizing the work of the lateral abdominal muscles. The back and lower back do not bend, forming a straight line.)"
			   "\n8. HAND TOUCH OF THE FOOT:\nLie down on the gym carpet and spread your arms out to the sides. The legs are also slightly apart. Now pull your right leg up while reaching for her foot with your left hand. Look directly at the ceiling without turning your head. Back in the starting phase, switch sides.)")
	elif call.data == "muscle_f":
		bot.send_message(call.message.chat.id, "Exercise 'Pistol':\nApproaches: 3\nReplays: 14\nRest: 30 seconds\n(We stand with our legs narrowly apart and lift one of them off the floor. After that, bend the leg on which we stand at the knee and squat as low as possible, trying to keep your back straight. Now push off and return to the starting position, change the leg and repeat)."
											   "\n============================="
											   "\n\nWalking on your hands against the wall:\nApproaches: 3\nReplays: 10\nRest: 30 seconds\n(We take a position on our hands (standing on our hands) with our feet leaning against the wall. Now move your hands forward and 'go' down the wall until your feet reach the floor.)"
											   "\n============================="
											   "\n\nJumping to the side:\nApproaches: 3\nReplays: 30\nRest: 30 seconds\n(We stand with our feet shoulder-width apart. Then we go down and abruptly push off from the floor with our right foot in order to jump to the left side and land on the left foot. Immediately after landing, push off with your left foot and repeat the movement, this time to the right Side)"
											   "\n============================="
											   "\n\nThe long jump from the place:\nApproaches: 3\nReplays: 8\nRest: 30 seconds\n(We go down to the squat position with our feet shoulder-width apart. We pull our arms back and use them to push ourselves forward when jumping, and for additional inertia, we throw our legs in front of us. We jump as far as possible and land on the soles of our feet.)")



bot.polling(none_stop=True, interval=0)

