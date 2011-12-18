<!DOCTYPE HTML>
<html>
  <head>
    <title>
      Brocab on AppEngine
    </title>
  </head>
  <body>
    <h1>BROcabulary</h1>
    <a href="${request.application_url}/edit">Create</a>
    <ul>
    %for word in words:
    <li>
      <h2>${word.value}</h2>
      ${word.definition}
      <br>
      <a href="${request.application_url}/edit?_id=${word.key().id()}">edit</a>
    </li>
    %endfor
    </ul>
  </body>
</html>