<!DOCTYPE HTML>
<html>
  <head>
    <title>
      Brocab on AppEngine
    </title>
  </head>
  <body>
    <h1>BROcabulary</h1>
    <!--
	this pattern/style for form simulates a post back for those of you
	who may have suffered through asp.net

        so, the view that renders this, should look for "POST" in the
        request parameters to determine whether to handle the form
        data or not

        the advantage here is that logic for generating the form,
        handling the data is contained in one function rather than
        spread across multiple functions.

        this has nothing to do with appengine, pyramid etc.... this is
        just a style for handling forms, nothing more
    -->
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