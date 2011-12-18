<!DOCTYPE HTML>
<html>
  <head>
    <title>
      Brocab on AppEngine
    </title>
  </head>
  <body>
    <h1>BROcabulary</h1>
    <form action="?POST" method="POST">
      <label>
	Word
      </label>
      <input type="text" name="value" value="${value or ''}">
	<label>
	  Definition
	</label>
	<br>
	<textarea name="definition">${definition or ''}</textarea> 
	  <input type="hidden" name="id" value="${id or ''}">
      <input type="submit" value="Save">
    </form>
  </body>
</html>