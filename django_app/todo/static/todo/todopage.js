// Function for creation modal window.
$(document).ready(function() {
    $('a.TodoCreationWindow').click( function(event){
      
      let status = $(this).attr("id");
      let form = $(".form-group")[0];
      form.status.value = status;

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

// Function for the update modal window.
$(document).ready(function() {
  $('button.TodoUpdateWindow').click( function(event){
    event.preventDefault();
    $('#SiteOverlay').fadeIn(297,	function(){
      $('#TodoUpdateWindow') 
      .css('display', 'block')
      .animate({opacity: 1}, 198);
    });
  });

  $('#TodoUpdateWindow__close, #SiteOverlay').click( function(){
    $('#TodoUpdateWindow').animate({opacity: 0}, 198, function(){
      $(this).css('display', 'none');
      $('#SiteOverlay').fadeOut(297);
    });
  });
});

// Function for moving the Todo's ID to the form action field and for values substitution in update form.
$(function(){
  $(".btn-secondary").on("click", function(){
      var id = $(this).attr("id");
      var title = $('#todo_title_' + id).text();
      var memo = $('#todo_memo_' + id).text();
      let form = $(".form-group")[1];
      form.todo_id.value = id;
      form.title.value = title;
      form.memo.value = memo;

      $("form").attr("action", ("/todos/update/" + id));
  });
});