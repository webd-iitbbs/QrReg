
<html>
    <head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    </head>
    <body>
        
        <div class="container">
            <div class="row"></div>
            <div class="row">
                <div class="col-lg-4">
                    
                </div>
                <div class="col-lg-3" style="background-color:powderblue;">
                    <h4>QRCODE generation form</h4>
                    
                    <form method="POST" action="insertqr.php">
                <input type="text" name="number" placeholder="Seven digit Number">
                <input type="text" name="code" placeholder = "code"><br>
                <input type="submit" class="btn btn-info" name="submit" value="submit" >
                
            
        </form>
                </div>
            </div>
        </div>
        
    </body>
</html>