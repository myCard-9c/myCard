$(document).ready(function() {
	window.jsPDF = window.jspdf.jsPDF
	var doc = new jsPDF();
	$("#saveBtn").click(function() {
		var doc = new jsPDF({format:"a1",orientation:"landscape"});
		console.log(document.getElementById("card"))
		doc.html(document.getElementById("card"),{callback: function (doc) {
     doc.save();
   },filename :"card.pdf"}).save()
	});
});
