$(document).ready(function() {
	window.jsPDF = window.jspdf.jsPDF
	var doc = new jsPDF();
	$("#saveBtn").click(function() {
		var doc = new jsPDF({format:"a1",orientation:"landscape"});
		doc.html(document.getElementById("card"),{html2canvas:{windowWidth:1536,windowHeight:722},filename :"myCard.pdf"}).save()
	});
});
