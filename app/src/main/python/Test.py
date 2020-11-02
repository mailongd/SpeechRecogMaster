from responces import Commands, Responses
import random

commands = {"greetings": Commands.greetings,
            "fairwells": Commands.fairwells,
            "thankCom": Commands.thankCom,
            "convA": Commands.smallTalkA,
            "convB": Commands.smallTalkB,
            "convC": Commands.smallTalkC,
            "appologyCom": Commands.appologyCom,
            "morningCom": Commands.morningCom,
            "afternoonCom": Commands.afternoonCom,
            "nightCom": Commands.nightCom,
            "rudeCom": Commands.rudeCom,
            "singCom": Commands.singCom,
            "creatorCom": Commands.creatorCom,
            "nameCom": Commands.nameCom,
            "purposeCom": Commands.purposeCom,
            "goodCom": Commands.goodCom,
            "neutralCom": Commands.neutralCom,
            "badCom": Commands.badCom,
            "confirm": Commands.confirm,
            "unconfirm": Commands.unconfirm,
            "question": Commands.question,
            "angry": Commands.moodAngry,
            "confused": Commands.moodConfused,
            "help": Commands.helpCom
            }

responses = {"greetings": Responses.greetings,
             "fairwells": Responses.fairwells,
             "thankResp": Responses.thankResp,
             "conv": Responses.smallTalk,
             "appologyResp": Responses.appologyResp,
             "morningResp": Responses.morningResp,
             "afternoonResp": Responses.afternoonResp,
             "nightResp": Responses.nightResp,
             "rudeResp": Responses.rudeResp,
             "singResp": Responses.singResp,
             "creatorResp": Responses.creatorResp,
             "nameResp": Responses.nameResp,
             "purposeResp": Responses.purposeResp,
             "drunkResp": Responses.drunkResp,
             "soberResp": Responses.soberResp,
             "goodResp": Responses.goodResp,
             "neutralResp": Responses.okResp,
             "badResp": Responses.badResp,
             "unconfirmResp": Responses.unconfirmResp,
             "okResp": Responses.okResp,
             "moodAnalysed": Responses.moodAnalysed,
             "helpResp": Responses.helpResp,
             "commandList": Responses.commandList,
             "unknown": Responses.unknownCommandResp,
             "noCommandResp": Responses.noCommandResp
             }

def returnMood(text="hi im angry"):
    global mood
    mood = responses["moodAnalysed"][0] # Neutral start

    inConv = lambda x: [i for i in text.split() if i in x] # Returns any string matches in a list

    def multipartConv(a, b, moodarg=None):
        '''
        2 parts must be present in a conversation (a and b)
        '''
        A = inConv(a)  
        B = inConv(b)
        if len(A) > 0 and len(B) > 0:
            if moodarg is not None:
                global mood
                mood = moodarg
                
    def excludeInConv(exclude, include, moodarg=None):
        '''
        checks if the strings in exclude aren't in the string,
        and the strings in include are in the string
        '''
        A = inConv(exclude) # to exclude or include multiple lists use the + operator to join the lists
        B = inConv(include)
        if len(A) == 0 and len(B) > 0:
            if moodarg is not None:
                global mood
                mood = moodarg

    text = text.lower()
    
    for i in text.split(): # checks for single keywords
        if i in commands["angry"]: # checking for angry mood
            mood = responses["moodAnalysed"][3]
        elif i in commands["appologyCom"]:
            mood = responses["moodAnalysed"][0]
            break
        elif i in commands["rudeCom"]:
            mood = responses["moodAnalysed"][3]
            break
        elif i in commands["neutralCom"]:
            mood = responses["moodAnalysed"][0]
            break
                        
    multipartConv(commands["unconfirm"], commands["goodCom"], moodarg=responses["moodAnalysed"][2]) # not good

    multipartConv(commands["unconfirm"], commands["angry"], moodarg=responses["moodAnalysed"][0]) # not angry

    multipartConv(commands["unconfirm"], commands["confused"], moodarg=responses["moodAnalysed"][4]) #checking for confused mood

    excludeInConv(commands["unconfirm"]+commands["morningCom"], commands["goodCom"], moodarg=responses["moodAnalysed"][1]) # good

    excludeInConv(commands["unconfirm"], commands["badCom"], moodarg=responses["moodAnalysed"][2]) # not good

    return mood

print (returnMood("good not angry"))
