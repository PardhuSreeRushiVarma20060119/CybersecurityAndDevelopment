<!-- sqli-login.php -->
<?php
$conn = new mysqli("localhost", "root", "", "webattackslab");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $username = $_POST['username'];
  $password = $_POST['password'];

  $query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
  $result = $conn->query($query);

  if ($result->num_rows > 0) {
    echo "✅ Login success!";
  } else {
    echo "❌ Login failed.";
  }
}
?>

<form method="POST">
  Username: <input name="username"><br>
  Password: <input name="password"><br>
  <button type="submit">Login</button>
</form>
