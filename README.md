<h2>python AST mining</h2>
<h3>Requirements</h3>
<ul>
  <li>python3</li>
  <li>Unix Environment</li>
  <li>python numpy(ml, diagram)</li>
  <li>python matplot(diagram)</li>
  <li>python panda(ml)</li>
  <li>python scikit-learn(ml)</li>
  <li>c++ boost(json reader)</li>
</ul>
<h3>Mining Program</h3>
On a Unix machine "linux/wsl/macos"</br>
in the root folder of this project input command</br>
"python ast_analysis.py &#10092;target folder&#10093;/ -w"</br>
to start the mining.</br>
</br>
The result will be written a file named "ast_analysis_data.csv" in the root folder.</br>
<h3>Load into SQL</h3>
The provided sql script "ast_analysis.sql" will load the result into a database called "astmine" in table "output".</br>
Some query script are provided in the file "sql_scripts.sql" </br>
<h3>Download Our Result</h3>
<a href="http://pdm.pw:8080/fileserv/file-serv/ast_analysis_data.csv" target="_blank" rel="noopener noreferrer">csv (10,21,2021)</a></br>
<a href="https://u.pcloud.link/publink/show?code=XZWkCEXZEuWH3dbEB4hDza31GHQi4jFe0sEV" target="_blank" rel="noopener noreferrer">sql inserts</a></br>


