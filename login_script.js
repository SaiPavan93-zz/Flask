$("#sub").click(function() {

$.post($("#loginForm").attr("action"),
$("#loginForm :input").serializeArray(), function(info){$("#result").html(info);});
clearInput();
window.location = "dashboard.html";
	});

$("#loginForm").submit( function() {
	return false;
});

function clearInput()
{
	$("#loginForm :input").each( function() {
	   $(this).val('');
	});
}
