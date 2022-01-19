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
	  		var textFromFileLoaded = fileLoadedEvent.target.result;
		  	document.getElementById("text").innerHTML = textFromFileLoaded;
	  	};
	  	fileReader.readAsText(fileToLoad, "UTF-8");
	}
    
    $(".file-upload").on('change', function(){
    	loadFileAsText();
    	document.getElementById("left").style.opacity = "0.5";
    	document.getElementById("full").style.opacity = "0.5";
    	document.getElementById("whitebox").style.visibility = "visible";
//     	$(".whitebox").show();
    });
    
    $(".upload-button").on('click', function() {
    	$(".file-upload").click();
    });
    
});



