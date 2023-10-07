# ChefBot
A Python3 CLI Script that uses AI to assist with recipe creation. 

![image](https://github.com/zBreeez3y/ChefBot/assets/98996357/bd54b2f3-f71f-4a90-8edf-7861a272fb00)

## What is ChefBot?
Chefbot is an AI chatbot that utilizes OpenAI's GPT-4 API, with specific system contexts sent at each run to act as a personal chef to assist with recipe creations. 

If you're like me... you don't like to spend a lot of time searching through various recipes trying to find ones to cook each week or two. I personally am not too creative when it comes to food either, so I wanted someone (or something) to help me come up with some recipes to make. Well lucky for us, we're living in the beginning of the generative AI boom, so I figured using it would be the perfect project. 

## What can ChefBot do? 
In short, ChefBot provides you with recipes based upon any preference you provide it. It's flexible in how it creates recipes for you, and it's really all up to the information/details of your wants/needs that you provide it. On top of creating recipes, ChefBot can save recipes and ingredients for all the recipes it recommends to separate files, which you can then email directly to yourself so you can have the lists on your mobile device simply by typing "email" in the script. It will save your conversation each run, which can be loaded back into the next run in case you need to revisit any of the recipes from your prior run.

### Initial Run
The first time you run the script, ChefBot will ask you for 3 details:
 - Any food allergies you may have
 - If you have any preferred cuisine styles
 - If you have any ingredients you dislike/want ChefBot to not use
   
Once provided, ChefBot will save those to a text file called "preferences.txt" in the scripts working directory, and will load those in each time you run it afterwards

At that point, you can just interact with ChefBot as you would with a real chef. Below are some ways that ChefBot can be used
#### Example Scenarios 
- You have limited ingredients on hand, so you ask ChefBot if there are any recipes you could make using just those ingredients
- You want to plan dinners out for the week, so you ask ChefBot to come up with however many dinner recipes you need for the week (and maybe you'd like some leftovers for a night or two)
- You're in the mood for something with a specific ingredient, so you ask ChefBot for recipes with that ingredient
- You ask ChefBot for ideas on recipes for X amount of people
- Someone is allergic to X, so you ask ChefBot how to make Y without X
- You tell ChefBot that you want meals to stay within a specific calorie count, or any dietary restriction
- Etc, etc. There are so many ways you could utilize ChefBot. Just talk with it :)

## Script Commands
ChefBot has a number of commands that can be ran to perform various tasks. Below are the commands that can be ran: 
```
preferences                     Reset preferences and rerun preference prompts (!Warning! Resets ChefBot conversation)
save [recipes|ingredients]      Save currently recommended recipes/ingredients to a text file
load chat                       Load the previous ChefBot chat history
email                           Email both 'recipes.txt' and 'ingredients.txt' to yourself (for access on mobile)
help                            Displays the ChefBot help menu
end|exit (or CTRL+C)            Exit ChefBot
```

## Setup
ChefBot requires an OpenAI GPT-4 eligible API key. I believe at this time, you can only get access to GPT-4 API if you have an OpenAI account older than August 18, 2023 and have spent more than $1 on the site, or if you make a new account now and buy $0.50 worth of prepaid credits. OpenAI stated on July 6th, 2023 "We plan to open up access to new developers by the end of this month, and then start raising rate-limits after that depending on compute availability." though I have not seen an update for that yet. 
- Create OpenAI account/Get your OpenAI GPT-4 eligible API Key
- Create an app password for your Gmail account (Highly recommended to make a random account for this)
- Create an enviornment variable on your host called "OPENAI_API_KEY" and set value to API key
- Create an enviornment variable on your host called "chefbot" with the value in the format: {recipient_email};{sender_email};{sender_appPass}
   - This is for the email feature of the script.
 #### GPT-3.5
 You could change the "model" variable on lines 214 and 241 to "gpt-3.5-turbo" to use GPT-3.5. However, I did not yield consistent results using this model. 
## Disclaimer
The GPT API's do have a "pay per use" model on their API's, so the script does cost a little money to use. 

- GPT-4's price is $0.03/1k PROMPT tokens and $0.06/1k SAMPLED tokens

The average cost per conversation (for me) was around $0.13. That was usually with 3-4 different recipes that it generated per conversation. Intended use is once a week, so an average of $0.52/month
