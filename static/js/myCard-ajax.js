$(document).ready(function() {
	$('#gnr8').click(function() {
		$.get('/myCard/generate_card', function(data){
			$('#card').html(data)
		});
	});
	$('.card').click(function() {
		var cardId;
		cardId = $(this).attr("data-cardid");
		$.get('/myCard/generate_card',{"card_Id": cardId}, function(data){
			$('#card').html(data);
		});
	});
});