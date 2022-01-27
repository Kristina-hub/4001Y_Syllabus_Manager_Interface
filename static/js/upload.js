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
    		//path = "src='https://view.officeapps.live.com/op/embed.aspx?src=" + "../static/uploads/" + filename + "' width='1366px' height='623px' frameborder='0'>This is an embedded <a target='_blank' href='http://office.com'>Microsoft Office</a> document, powered by <a target='_blank' href='http://office.com/webapps'>Office Online</a>."
     		document.getElementById('scroll').src = "../static/uploads/" + filename;
     		//src="../static/uploads/BIO_1001A_2019.pdf"
     		// If it's in the same directory as the html file, then you can use <img src="localfile.jpg"/>
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


