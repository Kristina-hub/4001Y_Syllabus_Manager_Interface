// --------------------------------------- //
//       Authors: Kristina Kacmarova       //
//                Miranda Postma       	   //
//                Ridwan Bari              //
//                Winston Herold           //
//       Python Version: 3.7.4             //
//       Created on: 2022-02-16            //
// --------------------------------------- //



$(document).ready(function() {

	function addRow() {    	
		var table = document.getElementById("table");
		var row = table.insertRow();
		var cell = row.insertCell(0);
		cell.innerHTML = "";
		cell = row.insertCell(1);
		cell.innerHTML = "";
		cell = row.insertCell(2);
		cell.innerHTML = "";
		cell = row.insertCell(3);
		cell.innerHTML = "";
	}

	$(".submit-button").on('click', function() {
    	addRow();
    });
    
});


