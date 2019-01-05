<html>
    <head>    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
</head>
<body>
    
<?php
    $con = mysql_connect("localhost","esummiti_reg","!nPiUFjr)&NE") or die ("not connected to data base");
    mysql_select_db("esummiti_register");
    
   if(isset($_POST['submit'])){
        $number = $_POST['number'];
    $code = $_POST['code'];
        if(empty($number) ||  empty($code) ){
            //echo "<script>alert('enter all the details');</script>";
             header("location:qrcode.php");
        }
        else{
       
       //INSERT INTO `team` (`id`, `name`, `whatsapp`, `fb_profile`, `team`, `position`, `count`, `last_active`) VALUES (NULL, 'gnani', '9603221480', 'fb.com', 'spons', 'associate', '0', '2018-10-25 00:00:00');
       $sql_query = "INSERT INTO `qr_code`(`id`, `normal_value`, `hashed`) VALUES ('NULL','$number','$code')";
       $sql = mysql_query($sql_query, $con) or die("not inserted") ;
       echo "copy the following link";
       echo "<br>";
       echo "http://ca.e-summit-iitbbs.com/register/register.php?p=";
       echo $code;
       echo "<br>";
       
      
       	
       
       	
			
		
        }
		
   }
  
?>
<br>
<a class="btn btn-primary" href="http://ca.e-summit-iitbbs.com/register/qrcode.php" role="button">submit another code</a>
</body>
</html>


