<h2>AST analysis of dynamic features of python.</h2>

<h3>Search for python dynamic functions in a folder </h3>
To start the analysis, enter <br />
"python ast_analysis.py \<name of the folder\>/"<br />

Add "-w" flag at the end of the command to automatically write to a .json file named "ast_analysis.json" in the current directory.<br />

<h3>Interpret the mined files </h3>
To compile the c++ json reader example:<br/>
run the scripts "build.cmd" or "build.sh".<br/> 
(need a boost library)<br/><br/>
<h3>Output file </h3>

".json" file structure:<br />
{<br />
  "DYNAMIC_FUNCTION_NAME":{<br />
    "THE_FILE_CONTAINING_THIS_FUNCTION":"LINE_NUMBER",<br />
    ...<br />
  },<br />
  ...<br />
}<br />

<h3>Bugs </h3>

Adds an extra comma at the end of the ".json" file.<br />
  Temp fix: Delete the last comma of the ".json" files <br />



