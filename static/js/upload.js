// --------------------------------------- //
//       Authors: Kristina Kacmarova       //
//                Miranda Postma       	   //
//                Ridwan Bari              //
//                Winston Herold           //
//       Python Version: 3.7.4             //
//       Created on: 2022-01-18            //
// --------------------------------------- //



$(document).ready(function() {
	function loadFileAsText() {
		var fileToLoad = document.getElementById("input-file").files[0];
		fetch(`/upload/?fileToLoad=${fileToLoad}`).then(function (response) { 			// call read_file.py with parameter textFromFile
          	return response.text();
      	}).then(function (text) {
			document.getElementById("text").innerHTML = text; 							// return text from read_file.py
		});
	}
    $(".file-upload").on('change', function(){
    	loadFileAsText();
    	document.getElementById("left").style.opacity = "0.5";
    	document.getElementById("full").style.opacity = "0.5";
    	document.getElementById("whitebox").style.visibility = "visible";
    });
    $(".upload-button").on('click', function() {
    	$(".file-upload").click();
    });
});


