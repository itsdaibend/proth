$(document).ready(function() {
    $('a.TodoCreationWindow').click( function(event){
      event.preventDefault();
      $('#SiteOverlay').fadeIn(297,	function(){
        $('#TodoCreationWindow') 
        .css('display', 'block')
        .animate({opacity: 1}, 198);
      });
    });
  
    $('#TodoCreationWindow__close, #SiteOverlay').click( function(){
      $('#TodoCreationWindow').animate({opacity: 0}, 198, function(){
        $(this).css('display', 'none');
        $('#SiteOverlay').fadeOut(297);
      });
    });
  });