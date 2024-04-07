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




<h1>Version Pattern ✅</h1>

The validation starts by looking for a version pattern in the file path of a Read node. This pattern is created using **Regular Expression**, so that any type of versioning (of the most used in the industry) is recognized. 
If the version captured doesn't match the pattern, the node will remain the default color.

![image](https://github.com/danilodelucio/ReadChecker/assets/47226196/9d12ede6-2724-4fd1-b3b5-2ac66c7dab53)




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
> Regardless of the file extension or if the folder is empty, ReadChecker will validate the version pattern found in the file path only.
