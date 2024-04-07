![ReadChecker_Logo_v001 LQ](https://github.com/danilodelucio/ReadChecker/assets/47226196/4efdd538-43e7-4e75-a333-12cc9ad33b0d)


<h1>Introduction 📓</h1>

This tool checks the versions of your Read nodes, coloring them to:

- **Green**: if they are updated;
- **Orange**: if they are out of date;
- **Red**: if they don’t exist;
- **Blue**: if they come from your Assets Library;

![Nodes color preview](https://github.com/danilodelucio/ReadChecker/assets/47226196/dccf07d3-7d93-415d-a690-8a8be01a992e)

This is helpful to check visually if the Read nodes are updated or not in your Node Graph.

![Screenshot 2023-07-14 080128](https://github.com/danilodelucio/ReadChecker/assets/47226196/db36d800-1793-411e-a256-be73c3e8c771)




<br>
<h1>Version Pattern ✅</h1>

The validation starts by looking for a version pattern in the file path of a Read node. This pattern is created using **Regular Expression**, so that any type of versioning (of the most used in the industry) is recognized. 
If the version captured doesn't match the pattern, the node will remain the default color.

![image](https://github.com/danilodelucio/ReadChecker/assets/47226196/9d12ede6-2724-4fd1-b3b5-2ac66c7dab53)




<br>
<h1>Folders/Files validation 📁📄</h1>

Some examples of folders and files validation, if the version pattern is found:

- File name:
![2023-07-14 08_56_10-test - ReadChecker - Visual Studio Code](https://github.com/danilodelucio/ReadChecker/assets/47226196/259e69be-fa6a-4834-827c-fb010d0260f7)

- Previous folder:
![2023-07-14 09_00_47-test - ReadChecker - Visual Studio Code](https://github.com/danilodelucio/ReadChecker/assets/47226196/d2d6db8d-d8fa-487f-a3c4-45bc7c6a1fba)

- Previous folder + File name
![2023-07-14 09_07_56-test - ReadChecker - Visual Studio Code](https://github.com/danilodelucio/ReadChecker/assets/47226196/6626b2ed-91c0-4996-923f-0b40c33319e9)

- Different folder + File name:
![2023-07-14 09_26_33-test - ReadChecker - Visual Studio Code](https://github.com/danilodelucio/ReadChecker/assets/47226196/5bd87f2b-1dac-4ddd-9b63-595ac77b916c)


> [!WARNING]
> _Regardless of the file extension or if the folder is empty, **ReadChecker** will validate the version pattern found in the file path only._




<br>
<h1>Assets Library path 🔍</h1>

To set the color for the Assets Library, open the ReadChecker Settings panel and update the Assets Path.

![image](https://github.com/danilodelucio/ReadChecker/assets/47226196/089f6236-408a-4f30-b33c-15813d636c46)

> [!NOTE]
> _**ReadChecker** will not validate the versions for the Read nodes that contain the Assets Path, they will be only set to BLUE color._


<br>
<h1>Nuke and Python compatibility ☢️🐍</h1>

**ReadChecker** was written in **Python 2.7.16** and **3.10.5**, so it's designed to work with all versions of Nuke.




<br>
<h1>Performance 📊</h1>

By default, this tool utilizes the **updateUI()** callback, which means that all Read nodes will be validated after any changes to the script. Don't worry about performance issues, this callback is designed to run as a low-priority process. Additionally, it uses the **OnScriptLoad()** and **OnScriptSave()** callbacks to validate all Read nodes just once when the Nuke script is opened/saved.

If you prefer to not use the callbacks, you can run the tool whenever you want by using the **Validate now** button.

![Screenshot 2023-08-12 015704](https://github.com/danilodelucio/ReadChecker/assets/47226196/994bc020-6874-404f-ac53-876fe65fde86)

You can also turn on/off the callbacks by the ReadChecker Settings panel:

![image](https://github.com/danilodelucio/ReadChecker/assets/47226196/382ea978-4dd9-4eff-b591-94bd156974d1)

> [!IMPORTANT]
> _For now, the RED color for nodes with Error doesn’t work using the UpdateUI function._<br>
> _For more information about callbacks, please visit the [NUKE Python Developer’s Guide](https://learn.foundry.com/nuke/developers/latest/pythonreference/callbacks.htm) page._




<br>
<h1>Troubleshooting 🛠️</h1>

If you have feedback, suggestions, or feature requests, please visit the [Discussions](https://github.com/danilodelucio/ReadChecker/discussions) page and create a **New Discussion**. <br>
For bugs, please go to the [Issues](https://github.com/danilodelucio/ReadChecker/issues) page and create a **New Issue**.




<br>
<h1>Installation ⚙️</h1>

- Paste the **ReadChecker** folder into your main **.nuke** directory (usually inside `~/user/.nuke`);
- Add `nuke.pluginAddPath('./ReadChecker')` into your **init.py** (if you don’t have one, you can create it);
- Enjoy! 😍

![image](https://github.com/danilodelucio/ReadChecker/assets/47226196/19e35133-d707-4cb1-9557-5dbd0d1723f9)

![image](https://github.com/danilodelucio/ReadChecker/assets/47226196/317cbc19-8b78-42a0-9180-e0c344aca1f9)

<h1>License📝</h1>

- You are free to use this tool for both non-commercial and commercial purposes (it's completely free!);
- You cannot claim to be the original author of this tool or sell it as your own product;




<br>
<h1>Special Thanks🙏</h1>

Special thanks to Henrique Reginato, Magno Borgo, and Gustavo Goncalves for testing this tool and providing valuable feedback for improvement. Also, thanks to Juliana Chen for her support and encouragement.




<br>
<h1>Support me! 🥺</h1>

![image](https://github.com/danilodelucio/ReadChecker/assets/47226196/eededd07-ec9c-45aa-9040-97d0a84a3699)

If you find this tool useful, please consider supporting me on [Buy Me A Coffee](https://www.buymeacoffee.com/danilodelucio). ☕ <br>
You can also share this tool or send me a positive message, it would help me in the same way.


<h1>Cheers! 🥂</h1>
