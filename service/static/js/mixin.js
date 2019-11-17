(function($) {
  "use strict";
  
  // Go to card buttons with jQuery easing
  $(document).on('click', 'a.scroll-to-card',
  function(e) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop:
      ($($anchor.attr('href')).offset().top)
    }, 1000, 'easeInOutExpo');
    e.preventDefault();
  })
  
  // render plots as they enter viewport
//  $(document).on()
})(jQuery); // End of use strict