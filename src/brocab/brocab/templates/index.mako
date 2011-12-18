<!DOCTYPE HTML>
<html>
  <head>
    <title>Brocab on AppEngine</title>
  </head>
  <body>
    <h1>BROcabulary</h1>
    <!--
	pyramid/mako specific:
	request is passed in to template implicitly, application_url
	is the root that the application is known to be mounted at, which
	is typically *:80/ but not necessarily
	
      -->
    <a href="${request.application_url}/edit.html">Create</a>

    <!--
	expecting a list of word objects, loop through them and render
	their value, definition and an edit link
      -->
    <ul>
    %for word in words:
    <li>
      <h2>${word.value}</h2>
      ${word.definition}
      <br>
      <a href="${request.application_url}/edit.html?_id=${word.key().id()}">edit</a>
    </li>
    %endfor
    </ul>
  </body>
</html>
