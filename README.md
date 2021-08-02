# Choose Your Own Adventure

An easy way to create a text-based adventure game that can be played in the console. You write the story, and players will be prompted to go through it and make choices. It can be as simple or complicated as you want!

![screenshot](https://raw.githubusercontent.com/BenRStutzman/choose-your-own-adventure/master/Pictures/screenshot.jpg)

## Writing the story

Edit story.txt and create events in this format.

> [Event ID]  
>  
> [Plot]  
> ...  
> [More plot (optional)]  
> ...  
> [More plot (optional)]  
>   
> [Prompt]  
>   
> [Event ID 1]) [Choice 1]  
> [Event ID 2]) [Choice 2]

For example, your first event might be:

> 0
> 
> It's a lovely fall day, and you're hiking in the woods.  
> ...  
> You come to a fork in the trail.
> 
> Do you:
> 
> 1\) Take the path on the left?  
> 2\) Take the path on the right?

The plot will display to the user, and then they will be prompted to choose between the two options. If they choose the first, they will be taken to the event with ID 1, and if they choose the second, they'll be taken to the event with ID 2.

Separate each event with two blank lines.

For a story-ending event (e.g., getting eaten by a bear), end with a final message instead of a prompt, and don't include choices. For example:

> 3
> 
> You slap the sun bear upside the snout...  
> ...  
> Uh oh, that seems to have made it angry.  
> ...  
> The bear rears back on its hind legs and prepares to devour you.
> 
> The end.

## Compiling into an .exe

When you have the story written to your liking, just run compile.bat. This will create a folder called ChooseYourOwnAdventure, compile the python file into an executable called Adventure in that folder, and copy your story into a hidden folder alongside that executable. Then, you can send the ChooseYourOwnAdventure folder to anyone, and they can play your game by opening it and double-clicking Adventure.
