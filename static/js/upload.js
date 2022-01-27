// --------------------------------------- //
//       Authors: Kristina Kacmarova       //
//                Miranda Postma       	   //
//                Ridwan Bari              //
//                Winston Herold           //
//       Python Version: 3.7.4             //
//       Created on: 2022-01-18            //
// --------------------------------------- //



$(document).ready(function() {

	function loadFile(form, filename) {    	
 		const formData = new FormData(form); 		
 		var oReq = new XMLHttpRequest(); 		
 		oReq.open("POST", "upload", true); 		
 		oReq.send(formData);
 		oReq.onload = function(oEvent) {
    		document.getElementById("text").innerHTML = oReq.response; 
    		
    		var path = document.location.pathname;
			//var directory = path.substring(path.indexOf('/'), path.lastIndexOf('/'));   //"../static/uploads/"
    		
    		//var path = require("path")
    		//var directory = path.dirname(path.basename(__dirname))

    		document.getElementById('scroll').src = path + "../" + filename;
    		//document.getElementById('scroll').src = "/var/www/4001Y_Website/static/uploads/" + filename;
     	};
	}
	
    $(".file-upload").on('change', function() {
    	document.getElementById("left").style.opacity = "0.5";
    	document.getElementById("full").style.opacity = "0.5";
    	document.getElementById("whitebox").style.visibility = "visible";
    	document.getElementById("text").innerHTML = "Loading..."; 
    	loadFile(this.form, this.files[0].name);
    	document.getElementById("text2").innerHTML = this.files[0].name; 
    });
    
    $(".upload-button").on('click', function() {
    	$(".file-upload").click();
    });
});


