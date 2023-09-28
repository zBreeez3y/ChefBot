import os 
import re
import ssl
import json
import email
import openai
import smtplib
from art import *
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

#Define class of ANSI Escaped color codes
class colors:
    user = '\033[1;36m'
    ast = '\033[1;31m'
    ver = '\033[1;32m'
    inf = '\033[1;33m'
    end = '\033[0m'

#Banner
print("===========================================================================")
tprint('ChefBot', font='sub-zero')
print(f"                                 Ver: {colors.ver}1.0{colors.end}")
print("                               by zBreeez3y")
print("===========================================================================")
print("** type 'help' for help menu" + '\n')

#Check for enviornment variables
try:
    openai.api_key = os.environ['OPENAI_API_KEY']
except:
    print("There is no chefbot environment variable set. Please set one in the format '<to_email>;<from_email>;<sender_appPass>'" + '\n')
    exit()

#Help menu function
def help():
    print('\n' + "ChefBot Help Menu")
    print("-----------------" + '\n')
    print("Normal usage: Interact with ChefBot for personally tailored recipes")
    print("Use the following commands to interact with the ChefBot script:" + '\n')
    print("preferences                     Reset preferences and rerun preference prompts (!Warning! Resets ChefBot conversation)")
    print("save [recipes|ingredients]      Save currently recommended recipes/ingredients to a text file")
    print("load chat                       Load the previous ChefBot chat history")
    print("email                           Email both 'recipes.txt' and 'ingredients.txt' to yourself (for access on mobile)")
    print("help                            Displays the ChefBot help menu")
    print("end/exit (or CTRL+C)            Exit ChefBot" + '\n')

#Function to set preferences
def preference():
    preferences = {}
    print('\n' + f"{colors.ast}Preferences:{colors.end}" + '\n')
    categories = ['allergies', 'cuisines', 'dislikes']
    for category in categories:
        if category == 'allergies':
            prompt = 'any food allergies you have'
        elif category == 'cuisines':
            prompt = 'any cuisine styles you favor'
        elif category == 'dislikes':
            prompt = 'any ingredients/foods/cuisines you dislike'
        string = input("List {}, separated by a comma (Enter 'na' if none): ".format(prompt))
        if len(string.split(' ')) > 1: 
            while not re.match('^([a-zA-Z]+\,\s)+[a-zA-Z]+$', string) and "n/a" not in string:
                print(f"{colors.inf}Provide your response with a comma between each item{colors.end}" + '\n')
                string = input("List {}, separated by a comma (Enter 'na' if none): ".format(prompt))
        if "na" not in string:
            preferences.update({f'{category}': []})
            for item in string.split(','): 
                preferences[f'{category}'].append(item)

    file = os.path.join(os.getcwd(), 'preferences.txt')
    if not preferences == {}:
        with open(file, 'w') as f: 
            f.write(json.dumps(preferences))
    else:
        with open(file, 'w') as f: 
            f.write("")
    print(f"{colors.ast}Preferences saved.{colors.end}" + '\n')

#Save previous prompt to text file function
def save2text(text):
    cwd = os.getcwd()
    file = cwd + f'\\{text}.txt'
    with open(file, 'w') as f:
        f.write(previous)
    f.close()
    print('\n' + f"{colors.inf}'{text}.txt' has been updated with latest {text}{colors.end}" + '\n')

#Email recipes/ingredients
def sendMail():
    subject = "ChefBot Attachments"
    body = "Here are your ChefBot recipes and ingredients lists!"
    sender = os.environ['chefbot'].split(";")[1]
    receiver = os.environ['chefbot'].split(";")[0]
    password = os.environ['chefbot'].split(";")[2]

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    files = ['recipes.txt', 'ingredients.txt']
    for item in files:
        with open(item, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={item}"
        )
        message.attach(part)
        attachment.close()
    
    smtp_server = 'smtp.gmail.com'
    port = 587
    text = message.as_string()
    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, receiver, text)
    server.quit()
    

#Setting 'previous' variable to empty string, and setting initial data array to AI system context based on preferences (if any)
try:
    previous = ""
    fill = ""
    preferences = os.path.join(os.getcwd(), 'preferences.txt')
    if not os.path.isfile(preferences):
            preference()
    if not os.path.getsize(preferences) == 0:
        with open(preferences, 'r') as f:
            fill = json.loads(f.read())
    if os.path.getsize(preferences) == 0:
        data = [
            {"role": "system", "content": "You are my personal chef who is going to assist me with picking meal recipes. Don't create the list until I tell you my preferences. If I try to talk about other things than food/recipes, dont respond to it and bring the conversation back to the meals. When you recommend recipes, always include the instructions and ingredient portions."},
        ]
    else:
        pref = []
        if 'allergies' in fill:
            allergy = "Food Allergies: " + str(fill['allergies']).replace("'", "").replace("[", "").replace("]", "")
            pref.append(allergy)
        if 'cuisines' in fill:
            cuisine = "Favored Cuisines: " + str(fill['cuisines']).replace("'", "").replace("[", "").replace("]", "")
            pref.append(cuisine)
        if 'dislikes' in fill:
            dislike = "Meal Dislikes: " + str(fill['dislikes']).replace("'", "").replace("[", "").replace("]", "")
            pref.append(dislike)
        content = "You are my personal chef who is going to assist me with picking meal recipes. Don't create the list until I tell you my preferences. If I try to talk about other things than food/recipes, dont respond to it and bring the conversation back to the meals. When you recommend recipes, always include the instructions and ingredient portions. Here are my preferences: {}. Please refer to them".format(str(pref))
        data = [
            {"role": "system", "content": "{}".format(content)}
        ]
except KeyboardInterrupt:
    print(('\n' * 2) + "Exiting ChefBot...")
    exit()

#Main chatbot process
while True: 
    try:
        prompt = input(f"{colors.user}Message to Chef:  {colors.end}")
        if prompt == "end" or prompt == "exit":
            print('\n' + f"{colors.ast}Chef:{colors.end}" + " Thanks for using ChefBot! Enjoy your meals!")
            if (len(data) == 1):
                exit()
            elif (len(data) > 1):
                cwd = os.getcwd()
                file = os.path.join(cwd, 'chat.json')
                with open(file, 'w') as f:
                    json.dump(data, f)
                f.close()
                exit()
        elif prompt == "help":
            help()
            continue
        elif prompt == "preferences":
            preference()
            data.clear()
            pref = []
            cwd = os.getcwd()
            file = os.path.join(cwd, "preferences.txt")
            if not os.path.getsize(file) == 0:
                with open (file, 'r') as f: 
                    pref.append(f.read())
                f.close()
                content = content = "You are my personal chef who is going to assist me with picking meal recipes. Don't create the list until I tell you my preferences. If I try to talk about other things than food/recipes, dont respond to it and bring the conversation back to the meals. When you recommend recipes, always include the instructions and ingredient portions. Here are my preferences: {}. Please refer to them".format(str(pref))
                data = [
                {"role": "system", "content": "{}".format(content)}
                ]
                continue
            else:
                with open(file, 'w') as f: 
                    f.write("")
                f.close()
                data = [
                    {"role": "system", "content": "You are my personal chef who is going to assist me with picking meal recipes. Don't create the list until I tell you my preferences. If I try to talk about other things than food/recipes, dont respond to it and bring the conversation back to the meals. When you recommend recipes, always include the instructions and ingredient portions."},
                ]
                continue
        elif (prompt == "save recipes" or prompt == "save ingredients"):
            txtFileName = prompt.split(" ")[1]
            if txtFileName == "recipes":
                prompt = "Can you please show me all the recipes? Even if you just showed me, please reshow them"
            elif txtFileName == "ingredients":
                prompt = "Can you please consolidate all the ingredients into a shopping list? Please do not list items for each meal, combine into one list."
            data.append({"role": "user", "content": f"{prompt}"})
            completion = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = data
            )
            data.append({"role": "assistant", "content": f"{completion.choices[0].message.content}"})
            previous = completion.choices[0].message.content
            save2text(txtFileName)
            continue
        elif prompt == "load chat":
            file = os.path.join(os.getcwd(), 'chat.json')
            if os.path.isfile(file):
                data.clear()
                with open(file, 'r') as f:
                    data = json.loads(f.read())
                f.close()
                print('\n' + f"{colors.inf}Succesfully loaded ChefBots previous chat history.{colors.end}" + '\n')
                continue
            else:
                print('\n' + f"{colors.inf}No previous ChefBot chat history found.{colors.end}" + '\n')
            continue
        elif prompt == "email":
            sendMail()
            print('\n' + f"{colors.inf}Email sent!{colors.end}" + '\n')
            continue
        elif prompt == "": 
            continue
        data.append({"role": "user", "content": f"{prompt}"})
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = data
        )
        data.append({"role": "assistant", "content": f"{completion.choices[0].message.content}"})
        previous = completion.choices[0].message.content
        print('\n' + f"{colors.ast}Chef: {colors.end}" + completion.choices[0].message.content + '\n')
    except KeyboardInterrupt:
        print(('\n' * 2) + "Exiting ChefBot...")
        if (len(data) == 1):
            exit()
        elif (len(data) > 1):
            cwd = os.getcwd()
            file = os.path.join(cwd, 'chat.json')
            with open(file, 'w') as f:
                json.dump(data, f)
            f.close()
            exit()
