(function($) {
  "use strict"; // Start of use strict

  // Floating label headings for the contact form
  $("body").on("input propertychange", ".floating-label-form-group", function(e) {
    $(this).toggleClass("floating-label-form-group-with-value", !!$(e.target).val());
  }).on("focus", ".floating-label-form-group", function() {
    $(this).addClass("floating-label-form-group-with-focus");
  }).on("blur", ".floating-label-form-group", function() {
    $(this).removeClass("floating-label-form-group-with-focus");
  });

  // Show the navbar when the page is scrolled up
  var MQL = 992;

  //primary navigation slide-in effect
  if ($(window).width() > MQL) {
    var headerHeight = $('#mainNav').height();
    $(window).on('scroll', {
        previousTop: 0
      },
      function() {
        var currentTop = $(window).scrollTop();
        //check if user is scrolling up
        if (currentTop < this.previousTop) {
          //if scrolling up...
          if (currentTop > 0 && $('#mainNav').hasClass('is-fixed')) {
            $('#mainNav').addClass('is-visible');
          } else {
            $('#mainNav').removeClass('is-visible is-fixed');
          }
        } else if (currentTop > this.previousTop) {
          //if scrolling down...
          $('#mainNav').removeClass('is-visible');
          if (currentTop > headerHeight && !$('#mainNav').hasClass('is-fixed')) $('#mainNav').addClass('is-fixed');
        }
        this.previousTop = currentTop;
      });
  }

})(jQuery); // End of use strict
$("#sendMessageButton").click(function(e) {
  $("#sendMessageButton").html('Please Wait..');
  if ($("#name").val() !== ""){
    if ($("#city").val() !== ""){
      if ($("#state").val() !== ""){
        if ($("#phone").val() !== ""){
          if ($("#help").val() !== "Select"){
          
            e.preventDefault();
            $.ajax({
                type: "POST",
                url: "/newhelp",
                data: { 
                    name: $("#name").val(),
                    help: $("#help option:selected").text(),
                    city: $("#city").val(),
                    state: $("#state").val(),
                    phone: $("#phone").val(),
                    csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val(),
                },
                success: function() {
                  $("#sendMessageButton").html('Add My Help');
                    showThanks();
                    $('#name').val("");
                    $('#city').val("");
                    $('#state').val("");
                    $('#phone').val("");
                },
                error: function(result) {
                  $("#sendMessageButton").html('Add My Help');
                    alert('error');
                }
            });
          
          }else{alert('Please fill everything');}
        }else{alert('Please fill everything');}
      }else{alert('Please fill everything');}
    }else{alert('Please fill everything');}
  }else{alert('Please fill everything');}
  });

function showThanks(){
  document.getElementById("thanksforhelp").style.display = "flex";
  document.getElementById("mainNav").style.display = "none";
}
function hideThanks(){
  document.getElementById("thanksforhelp").style.display = "none";
  document.getElementById("mainNav").style.display = "block";
}