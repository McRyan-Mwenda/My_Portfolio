$(document).ready(function () {
  var slideIndex = 0;

  showSlides();

  // slideshow function
  function showSlides() {
    let i;

    // get the array of div elements with class-name slider
    var slides = document.getElementsByClassName("slider");

    for (i = 0; i < slides.length; i++) {
      // initially set the display to
      // none for every image.
      slides[i].style.display = "none";
    }

    // increase by 1, Global variable
    slideIndex++;

    // check for boundary
    if (slideIndex > slides.length) {
      slideIndex = 1;
    }

    slides[slideIndex - 1].style.display = "block";

    // Change image every 4.5 seconds
    setTimeout(showSlides, 4500);
  }

  var workProjects = $("#wp");
  var personalProjects = $("#pp");

  var workTab = $("#wp-button");
  var personalTab = $("#pp-button");

  var workSection = $("#wp-tab");
  var personalSection = $("#pp-tab");

  personalProjects.hide();

  workTab.click(function () {
    personalSection.removeClass("is-active");
    workSection.addClass("is-active");

    personalProjects.hide();
    workProjects.fadeIn();
  });

  personalTab.click(function () {
    workSection.removeClass("is-active");
    personalSection.addClass("is-active");

    workProjects.hide();
    personalProjects.fadeIn();
  });

  var backTop = $("#back-top");

  backTop.hide();

  $(window).scroll(function () {
    var scroll = $(document).scrollTop();

    if (scroll > 500) {
      backTop.fadeIn();
    } else {
      backTop.fadeOut();
    }
  });
});
