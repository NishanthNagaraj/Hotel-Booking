$(".card").on("click", function (e) {
    e.preventDefault();
    $(".card").removeClass("active");
    $(this).addClass("active");
    $(".form").stop().slideUp();
    $(".form").delay(300).slideDown();
  });
  $(".button").on("click",function()
  {
    alert("Payment Sucessfully Completed");
  });