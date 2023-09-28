# ChefBot
A Python3 Script that uses AI to assist with recipe creation. 

![image](https://github.com/zBreeez3y/ChefBot/assets/98996357/bd54b2f3-f71f-4a90-8edf-7861a272fb00)

## What is ChefBot?
Chefbot is an AI chatbot that utilizes OpenAI's GPT-3.5-Turbo and GPT-4 API's, with specific system contexts sent at each run to act as a personal chef to assist with recipe creations. 

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
end/exit (or CTRL+C)            Exit ChefBot
```

