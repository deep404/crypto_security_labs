# Topic: *Importing Compliance Audit Policies*
## Author: *Moglan Mihai*
------
## Main tasks :
__1. Import the manually downloaded policies from a predefined trusted location;__

__2. Parse and understand the format of data within the imported policy;__

__3. Save the same set of policies under a different name within a structured form (ex:
database);__

## Introduction :
This and further labaratory works will be done in Python. For first one I used tkinter, os and json libraries. My working OS is Ubuntu 16_04 and all audit files where downloaded from tenable.com.
   
## A little description :
__1. The GUI very much looks like Notepad GUI's. There is the white field for text and 2 menus up;__

__2. First menu is 'File Menu' with following commands (now works the 'New', 'Open', 'Save As', 'Export' and 'Exit'):;__

  * Export (parse the audic file and saves all the custom types data in a JSON file);
  * New (creates a new blank working field);
  * Open (open a file from the PC);
  * Save As (save the current content with a new name on PC) - unenabled;
  * Exit (close the app);

__3. The audit file is parsed charchater by character using for loop;__
  
__4. When the .audit file is opened it is parsed in the background and in the text box is illustrated all the custom items in a json format;__

__5. In the corner there is the 'Status Bar' which indicates the curent information about the activiti on the app;__

__6. In order to run the app change the location of audit files in the code and run the .py code in any CLI with python support;__


