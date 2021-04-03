$(document).ready(function() {
	$('#gnr8').click(function() {
		$.get('/myCard/generate_card', function(data){
			$('#card').html(data)
		});
	});
});