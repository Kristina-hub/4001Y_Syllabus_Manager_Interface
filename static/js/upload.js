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
	  	var fileReader = new FileReader();
	  	fileReader.onload = function(fileLoadedEvent) {
	  		var textFromFile = fileLoadedEvent.target.result;
	  		
	  		fetch(`/upload/?textFromFile=${textFromFile}`).then(function (response) { 		// call read_file.py with parameter textFromFile
          		return response.text();
      		}).then(function (text) {
				document.getElementById("text").innerHTML = text; 							// return text from read_file.py
			});
		  	
	  	};
	  	fileReader.readAsText(fileToLoad, "UTF-8");
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



