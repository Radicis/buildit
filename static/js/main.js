$(document).ready(function(){
  $("#reset").click(function(){
    $.ajax({
		url: "/reset/",
		success: function(data){			
			$('.page-container').load("/reset/");
		}
	});	
  });
});