<?php
        if ($_SERVER['REQUEST_METHOD']=="POST"){
       $user=$_POST['username'];
      $pass=$_POST['password'];

      if ($user==="Happy" && $pass==="happybhai7890"){
           echo "<h2 style='color:green;'>ACCESS GRANTED</h2><br>";
      }else{
      echo "<h2 style='color:red;'>ACCESS DENIED</h2><br>";
}
}
?>
<html>
   <head>
       <title>profile dashboard rank</title>
       <style>
           body{
    background-color: black;
    align-content: center;
    color: white;
    align-items: center;
}

.login_box{
    text-align: center;
    border: 2px solid yellow;
    box-shadow: 0 0 5px yellow;
    padding : 2vh;
    width: auto;
    background-color: grey;
    border-radius: 15px;
    height: auto;
}
input{
    margin : 2vh;
    color: black;
    border : 2px solid black;
    border-radius: 16px;
    height : auto;
    padding: 2vh;
    font-size: 2vh;
    text-align: center;
    background-color: white;
    box-shadow: 0 0 5px black;
}
label{
    align-self: center;
    color: black;
    font-size: 4vh;
}
#loginbtn{
    margin: 5px;
    background-color: blue;
    color:white;
    box-shadow: 2 0 5px blue;
    padding: 0 20px;
    text-align: center;
    font-size: 3vh;
}
h1{
    font-size:6vh;
    margin: 10px;
justify-self:center;
}
h2{
    font-size:5vh;
    margin: 10px;
justify-self:center;
}

       </style>
<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
   </head>
   <body>
       <script>
           function check() {
 var user=document.getElementById('username').value;
 var pass=document.getElementById('password').value;

 if (user.includes(" ")||pass.includes(" ")){
     alert('please enter a vaild password');
     return false
 }
if(user=="Happy" && pass=="happybhai7890"){
	window.open("/dashboard.php");
     return true
 }
}

       </script>
       <div class="login_box">
           <h1>Login page</h1><br>
           <form onsubmit="return check()" method="post">
               <label for="username">username : </label>
               <input type="text" name="username" id="username" placeholder="Enter your username" required /><br>

               <label for="password">password : </label>
               <input type="password" name="password" id="password" placeholder="Enter your password" required/><br><br>

               <input type="submit" name="loginbtn" id="loginbtn" value="login"/>
           </form>
       </div>
   </body>
</html>
