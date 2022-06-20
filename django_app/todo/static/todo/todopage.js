// Function for creation modal window.
$(document).ready(function() {
    $('button.TodoCreationWindow').click( function(){
      
      let status = $(this).attr("id");
      let form = $(".form-group")[0];
      form.status.value = status;
    });
  });

// Function for update modal window.
$(function(){
  $(".btn-secondary").on("click", function(){
      var id = $(this).attr("id");
      var title = $('#todo_title_' + id).text();
      var memo = $('#todo_memo_' + id).html().replaceAll("<br>", "\n").replaceAll('&amp;', '&').replaceAll('&lt;', '<').replaceAll('&gt;', '>');
      var label = $(this).parent('div').prev().children('div').attr("id");
      var status = $(this).parent('div').prev().attr("id");

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
      form.label.value = label;
      form.status.value = status;
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