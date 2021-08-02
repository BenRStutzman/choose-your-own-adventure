:: Compile the python script with pyinstaller.
pyinstaller --onefile --distpath ChooseYourOwnAdventure --name Adventure chooseYourOwnAdventure.py

:: Create a hidden folder and copy story.txt into it.
mkdir ChooseYourOwnAdventure\PleaseIgnoreThis
attrib +h ChooseYourOwnAdventure\PleaseIgnoreThis
copy story.txt ChooseYourOwnAdventure\PleaseIgnoreThis\story.txt

:: Remove unnecessary collateral files.
rmdir /s /q __pycache__
rmdir /s /q build
del Adventure.spec