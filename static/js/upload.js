// --------------------------------------- //
//       Authors: Kristina Kacmarova       //
//                Miranda Postma       	   //
//                Ridwan Bari              //
//                Winston Herold           //
//       Python Version: 3.7.4             //
//       Created on: 2022-01-18            //
// --------------------------------------- //


function uploadFile(form)
{
 const formData = new FormData(form);
 var oOutput = document.getElementById("static_file_response")
 var oReq = new XMLHttpRequest();
     oReq.open("POST", "upload_static_file", true);
 oReq.onload = function(oEvent) {
     if (oReq.status == 200) {
       oOutput.innerHTML = "Uploaded!";
       console.log(oReq.response)
     } else {
       oOutput.innerHTML = "Error occurred when trying to upload your file.<br \/>";
     }
     };
 oOutput.innerHTML = "Sending file!";
 console.log("Sending file!")
 oReq.send(formData);
}



$(document).ready(function() {

	function loadFileAsText() {
		var fileToLoad = document.getElementById("input-file").files[0];
		
		fetch(`/upload/?fileToLoad=${fileToLoad}`).then(function (response) { 		// call read_file.py with parameter textFromFile
          	return response.text();
      	}).then(function (text) {
			document.getElementById("text").innerHTML = text; 							// return text from read_file.py
		});
		
// 	  	var fileReader = new FileReader();
// 	  	fileReader.onload = function(fileLoadedEvent) {
// 	  		var textFromFile = fileLoadedEvent.target.result;
// 	  		
// 	  		fetch(`/upload/?textFromFile=${textFromFile}`).then(function (response) { 		// call read_file.py with parameter textFromFile
//           		return response.text();
//       		}).then(function (text) {
// 				document.getElementById("text").innerHTML = text; 							// return text from read_file.py
// 			});
// 		  	
// 	  	};
// 	  	fileReader.readAsText(fileToLoad, "UTF-8");
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


