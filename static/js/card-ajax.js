$(document).ready(function() {
	var cardId;
	cardId = $("#cardBtn").attr("data-cardid");
	$.get('/myCard/generate_card',{"card_Id": cardId}, function(data){
		$('#card').html(data);
	});
});
