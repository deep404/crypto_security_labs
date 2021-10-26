# Topic: *Enforcing a Policy*
## Author: *Moglan Mihai*
------
## Main tasks :
__1. Choose which options they would like to run (by selecting or deselecting options);__

__2. Search by name for an option (via a search bar);__

__3. Select or deselect all options in one click;__

__4. Create and save a policy that contains only the selected options under the same name or
a different one;__

## Introduction :
This and further labaratory works will be done in Python. For first and second one I used tkinter, os and json libraries. My working OS is Ubuntu 16_04 and all audit files where downloaded from tenable.com.
   
## A little description :
__1. The GUI very much looks like Notepad GUI's. There is the white field for text and one menu up;__

__2. First menu is 'File Menu' with following commands (now works the 'New', 'Open', 'Save', 'Save As', 'Export', 'Run Audit' and 'Exit'):;__

  * Export (parse the audit file and the user select the custom items he wants and export the custom items again in a new audit file);
  * New (creates a new blank working field);
  * Open (open a file from the PC, parse it and show all the custom items from the audit file in the working field);
  * Save (the user select the custom items he wants, using checkbox, and save the custom items in a json file)
  * Save As (the same as Save option, but the custom items are saved in a new json file) ;
  * Run Audit (after the json file with options is opened, 'run audit' option runs all the containers and make a report if the user OS satisfies the selected audit options)
  * Exit (close the app);

__3. The audit file is parsed charchater by character using for loop;__
  
__4. When the .audit file is opened it is parsed in the background and in the text box is illustrated all the custom items in a json format;__

__5. When is selected one of the option 'Save', 'Save As' or 'Export', there pops out a new window where the user selectes the custom items he wants using checkbox ('Select All' and 'Deselect all' options exist), then he 'Submit' his choice;__

__6. Under the 'File' menu, there is the 'Search' field. The user indicate the word/sentence he wants to find and press 'Find' button. He can navigate between between found words/sentences using 'Next' and 'Back' buttons. The found words/sentences are highlighted with red;__

__7. In order to run the app change the location of audit files in the code and run the .py code in any CLI with python support;__

__8. In the 'Lab3' folder there is an example of input -> 'audit.json' and output after running the 'Run Audit' option -> 'audit_result.txt'. Also, I uploaded the .audit for the Ubuntu 16.04, so you can try on your Ubuntu 16.04 OS;__

__9. You can use the video like a tutorial how to use the application;__

