<?php
  if(isset($_POST["kanji-url"])){
    $kanji_url = $_POST["kanji-url"];
    $kanji_data = json_decode(file_get_contents($kanji_url));
    echo $kanji_data;
  }

?>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!--Custom CSS-->
    <link rel="stylesheet" href="index.css">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
	  <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
	  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
	  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <title>IB Kanji</title>
  </head>
  <body>
    <div id=main-container>
      <header style="text-align: center;"><h1>IB Kanji</h1></header>

      <nav>
        <ul class="nav justify-content-center">
          <li class="nav-item">
            <a class="nav-link active" href="#">SL Kanji</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">HL Kanji</a>
          </li>
        </ul>
      </nav>
      <form id="kanji-form" method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        <input name="kanji-search" id="kanji-search" type="search" placeholder="Type a kanji to see if its required for the IB">
        <input name="kanji-url" id="kanji-url" type="url" hidden>
      </form>
    </div>
    <script>
      $(function() {
        $("#kanji-search").keyup(function(e){
          if ((event.keyCode || event.which) === 13){
            $kanji_search_val = this.value.trim().replace(" ","%20");
            //console.log($(this).val());
            console.log($kanji_search_val);
            $url = "https://jisho.org/api/v1/search/words?keyword=" + encodeURIComponent($kanji_search_val);
            $("#kanji-url").text($url);
          }
        });
      });
    </script>
  </body>
</html>