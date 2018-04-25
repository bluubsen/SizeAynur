$( document ).ready(function() {
  var $grid = $('#portfolio, #video, #gallery').imagesLoaded(function() {
    $grid.masonry({
      itemSelector: '.imagebox'
    });
  });

  $(".video-link").click(function(e) {
    $("#ytplayer").attr("src", $(this).data("url"));
    $(".modal").show();
    e.preventDefault();
  });

  $(".close").click(function(e) {
    $("#ytplayer").attr("src", "");
    $(".modal").hide();
    e.preventDefault();
  });
});
