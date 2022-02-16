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
		var row = table.insertRow(0);
		row.insertCell(0);
		row.insertCell(1);
		row.insertCell(2);
		row.insertCell(3);
	}

	$(".submit-button").on('click', function() {
    	addRow();
    });
    
});


