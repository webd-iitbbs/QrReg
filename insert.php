<?php

if (isset($_POST['submit-re']) && !empty($_POST['submit-re'])   ) {
	echo md5($_POST['input_text']);
}

?>

<form action="" method="POST">
	<input type="number" name="input_text">
	<input type="submit" name="submit-re">
</form>