AST analysis of dynamic features of python.<br />
<br />
To start the analysis, enter <br />
"python ast_analysis.py \<name of the folder\>/"<br />

Add "-w" flag at the end of the command to automatically write to a .json file named "ast_analysis.json" in the current directory.<br />

To compile the c++ json reader example:<br/>
run the scripts "build.cmd" or "build.sh".<br/> 
(need a boost library)<br/>
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



