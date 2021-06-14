AST analysis of dynamic features of python.
To start the analysis, enter 
"python3 ast_analysis.py "NAME-OF-THE-FOLDER"/ "

Add "-w" flag at the end of the command to automatically write to a .json file named "ast_analysis.json" in the current directory.
eg. "python3 ast_analysis.py "NAME-OF-THE-FOLDER"/ -w"

".json" file structure:
{
  "DYNAMIC_FUNCTION_NAME":{
    "THE_FILE_CONTAINING_THIS_FUNCTION":"LINE_NUMBER",
    ...
  },
  ...
}

BUG:
Adds an extra comma at the end of the ".json" file.
  Temp fix: Delete the last comma of the ".json" files 



