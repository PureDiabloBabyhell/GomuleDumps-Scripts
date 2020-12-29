# GomuleDumps-Scripts

/!\ To be used into a GoMule directory.

The python scripts work on GoMule dumps (.d2x.txt files) and generate files using .purediablo as extension to avoid any interference with real stashes and item loss.

A dedicated HOW TO section is available by the end of this README.

Feedback is appreciated! Send PM to Babyhell on purediablo.com with bugs/lacks and even suggestions ;-)

Current version status:
- Tested using Python 3.9.1 on Windows 10: shall be compatible with Python any 2.5+ versions.
- File names are set into the non-dicos python scripts: feel free to edit them to fit your needs.
- Content is crunched based upon the defined dicos' content: those are still to be completed.
- Generates PureDiablo compatible BBCODE to be copied into any post.
- This BBCODE is available in files with .purediablo extension, to be opened as plain txt file with any text editor.

The following scripts use the following file names:
- charmsJewels.py uses "Charms Skillers", "Charms_MF", "Jewels_Good", "Jewels"
- gems.py uses "Gems" and generates a table of pgems, and a global count on flawless gems.
- runes.py uses "Runes" and generates a full table from El to Zod
- items.py uses "Tradable_S_U" (note: this script shall be able to handle rare and magic items too)

**********
* HOW TO *
**********
- Unzip/put the scripts and the dico folder in the GoMule folder you want to use.
- If necessary, edit the scripts to set the file names as needed: those are the GoMule stash names without extension.
- Generate dumps of those stashes using GoMule.
- Open a terminal, get to the GoMule folder where you copied the scripts.
- Execute each script by typing: python <script file name>, for example: python gems.py.
- Open the generated .purediablo files in the same folder, and copy/paste it in a post on PureDiablo
