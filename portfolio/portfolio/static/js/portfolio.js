$( document ).ready(function() {
  var $grid = $('#portfolio, #gallery').imagesLoaded(function() {
    $grid.masonry({
      itemSelector: '.imagebox'
    });
  });

  $(".video-link").click(function() {
    $("#ytplayer").attr("src", $(this).data("url"));
    $(".modal").show();
  });

  $(".close").click(function() {
    $(".modal").hide();
  });
});
