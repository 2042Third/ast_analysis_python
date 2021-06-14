AST analysis of dynamic features of python.<br />
<br />
To start the analysis, enter <br />
"python3 ast_analysis.py "NAME-OF-THE-FOLDER"/ "<br />

Add "-w" flag at the end of the command to automatically write to a .json file named "ast_analysis.json" in the current directory.<br />
eg. "python3 ast_analysis.py "NAME-OF-THE-FOLDER"/ -w"<br />

".json" file structure:<br />
{<br />
  "DYNAMIC_FUNCTION_NAME":{<br />
    "THE_FILE_CONTAINING_THIS_FUNCTION":"LINE_NUMBER",<br />
    ...<br />
  },<br />
  ...<br />
}<br />

BUG:<br />
Adds an extra comma at the end of the ".json" file.<br />
  Temp fix: Delete the last comma of the ".json" files <br />



