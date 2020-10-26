## = ok
### = not ok
from datetime import datetime

class Commands:
	# simple starter/ender commands
	greetings = ["hello", "hey", "hi"]
	thankCom = ["thank", "thanks", "appriciate"]
	fairwells = ["bye", "see you later", "i'm out", "by", "buy", "cya"]
	smallTalkA = ["how", "how's", "hows", "whats", "what's"] # 2 part (A)
	smallTalkB = ["going", "you", "day", "today", "life", "up", "goes", "it", "doing"] # 2 part (B)
	smallTalkC = ["howdy", "whatsapp"] # Independant
	
	# appology command
	appologyCom = ["sorry", "appologise"]
	
	# timely command
	morningCom = ["morning", "goodmorning"]
	afternoonCom = ["afternoon", "goodafternoon"]
	nightCom = ["night", "goodnight"]
	
	# rude command
	rudeCom = ["stupid", "asshole", "useless", "worthless", "dumb", "shit", "ass", "go away", "trash", "fuck", "fuk", "idiot", "arsehole", "bitch", "s***", "f***", "cunt","c***"]
	
	# interactions
	question = ["what", "whats", "what's", "who", "whos", "who's", "when", "whens", "when's", "is", "how", "hows", "how's"]
	confirm = ["yes", "yea", "yeah", "ya", "ok", "cool", "nice", "yep", "awesome", "sweet"]
	unconfirm = ["no", "na", "nah", "nar", "dont", "don't", "not"]
	goodCom = ["good", "happy", "great", "fantastic", "extatic", "cheerful", "delight", "delighted", "delightful", "ecstatic", "joyful", "joy", "lively", "wonderful", "grateful"]
	neutralCom = ["not bad", "im ok", "alright", "fine", "neutral", "so so", "calm", "cool", "easy", "relaxed"]
	badCom = ["bad", "unhappy", "sad", "depressed", "miserable", "heartbroken", "mournful", "distressed", "down", "hurt", "grief", "disappoint", "disappointed"]
	
	# casual conversation
	singCom = ["sing", "sings"]
	
	# informative
	creatorCom = ["creator", "created", "born", "made", "old"]
	nameCom = ["name"]
	purposeCom = ["purpose"]
	
	# mood
	moodAngry = ["retard", "angry", "furious", "hate", "anger", "heated", "Iritated", "Iritate", "mad", "outraged", "rage", "raging", "wrath", "wrathful"]
	
	moodConfused = ["sure", "know"]
	
	# help
	helpCom = ["help"]
	
	
class Responses:
	# simple starter/ender responses
	greetings = ["Hello", "Hey", "Hi", "How's it going?"]
	thankResp = ["You're welcome", "Anytime", "Happy to help"]
	fairwells = ["Bye", "See you later", "Have a good day!"]
	smallTalk = ["I'm great, how are you?", "I'm quite well", "Not too bad thanks, and yourself?"]
	
	# forgiveness responses
	appologyResp = ["Apology accepted", "Ok, I will let you off this time"]
	
	# timely responses
	morningResp = ["Good Morning. Dont forget to drink your coffee"]
	afternoonResp = ["Good Afternoon"]
	nightResp = ["Good Night, Sleep tight"]
	
	# rude Responses
	rudeResp = ["That was very rude", "That was uncalled for", "Learn some manners"]
	
	# interactions
	unconfirmResp = ["Ok then", "Understood"]
	okResp = ["Ok then", "Got it"]
	goodResp = ["Thats good", "Im happy to hear that"]
	badResp = ["Oh no", "Im sorry to hear that"]
	
	# casual conversation
	singResp = ["Me? Sing? How about no"]
	
	# informative responses
	creatorResp = ["I was created on 20 Febuary 2020"]  ### add I was created by?
	nameResp = ["My name is SmartBot and I am your personal assistant"]
	purposeResp = ["My only purpose is to assist you"]
	
	#fun
	drunkResp = ["Let's party up", "party time"]
	soberResp = ["I'm not doing that again", "Oh what a nighttt"] # extra t's for exageration
	
	#mood
	moodAnalysed = ["Neutral", "Happy", "Sad", "Angry", "Confused"]
	
	# help
	helpResp = ["Try asking me some things listed below"]
	commandList = ["Hi", "Hows it going", "Good Morning", "Good Afternoon", "Good Night",
	"When were you created", "Whats your name", "Whats your purpose",
	"Sing for me", "Tell me facts about turtles", "Get drunk", "Get sober",
	"Whats the weather", "Whats the time", "Whats the date",
	"Define [word]", "Search [phrase]", "Calculate [equation]",
	"Lock computer", "Sleep computer", "Shutdown computer",
	"Cancel shutdown", "bye"]
	
	# unknown/no command responses
	unknownCommandResp = ["Perhaps I will be more intelligent in the future, but right now I am unable to answer that (Type help for a list of things you can ask me to do)",
	"Sorry, I don't understand (Type 'help' for a list of things you can ask me to do)",
	"Sorry, I don't know the answer to that question. (Type help for a list of things you can ask me to do)"]
	
	noCommandResp = ["Sorry I didn't catch that"]

