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
      var memo = $('#todo_memo_' + id).html().replaceAll("<br>", "\n");

      if($(this).parent('div').parent('div').hasClass('priority-4')){
        var priority = 4;
      } else if($(this).parent('div').parent('div').hasClass('priority-3')){
        var priority = 3;
      } else if($(this).parent('div').parent('div').hasClass('priority-2')){
        var priority = 2;
      } else if($(this).parent('div').parent('div').hasClass('priority-1')){
        var priority = 1;
      };

      let form = $(".form-group")[1];
      form.todo_id.value = id;
      form.title.value = title;
      form.memo.value = memo;
      form.priority.value = priority;

      $("form").attr("action", ("/todos/update/" + id));
  });
});

// Two functions for dropping down div with "Edit" and "Status" buttons.
$(".card .mb-3").mouseenter( function() {
  $(this).find(".drop-block").show(200);
});
$(".card .mb-3").mouseleave( function() {
  $(this).find(".drop-block").hide(200);
});