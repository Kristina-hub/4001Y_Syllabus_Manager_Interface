// --------------------------------------- //
//       Authors: Kristina Kacmarova       //
//                Miranda Postma       	   //
//                Ridwan Bari              //
//                Winston Herold           //
//       Python Version: 3.7.4             //
//       Created on: 2022-01-18            //
// --------------------------------------- //



$(document).ready(function() {
	function loadFile(form) {
	    document.getElementById("left").style.opacity = "0.5";
    	document.getElementById("full").style.opacity = "0.5";
    	document.getElementById("whitebox").style.visibility = "visible";
//     	document.getElementById("text").innerHTML = "1"; 
    	
 		const formData = new FormData(form);
//  		document.getElementById("text").innerHTML = "2"; 
 		
 		var oReq = new XMLHttpRequest();
//  		document.getElementById("text").innerHTML = "3"; 
 		
 		oReq.open("POST", "upload_static_file", true);
//  		document.getElementById("text").innerHTML = "4"; 
 		
 		oReq.send(formData);
//  		document.getElementById("text").innerHTML = "5"; 
	}
    $(".file-upload").on('change', function() {
    	document.getElementById("text").innerHTML = this.form;  // [object HTMLInputElement]
    	loadFile(this.form);
    });
    $(".upload-button").on('click', function() {
    	$(".file-upload").click();
    });
});


// 			<div class="leftside" id="left" style="cursor:pointer;">
// 				<div class="upload-button">
// 					<img src="../static/img/book-1.jpg">
// 					<h2>1. Upload your syllabus</h2>
// 					<p>Supported formats: .txt, .docx, .pdf</p>
// 				</div>
// 			</div>
// 			<input class="file-upload" type="file" id="input-file"/> 
// upload button -> choose file -> calls function


			
// 		<form enctype = "multipart/form-data">
// 		   <input id="input-file" type="file" name="static_file" />
// 		   <button id="upload-button" onclick="uploadFile(this.form)"> Upload </button>
// 		</form>
// choose file button -> upload button -> calls function


function uploadFile(form) {
//  		const formData = new FormData(form);
//  		var oReq = new XMLHttpRequest();
//  		oReq.open("POST", "upload_static_file", true);
//  		oReq.send(formData);
//  
     	document.getElementById("left").style.opacity = "0.5";
    	document.getElementById("full").style.opacity = "0.5";
    	document.getElementById("whitebox").style.visibility = "visible";
    	//document.getElementById("text").innerHTML = "This"; 
    	document.getElementById("text").innerHTML = form; //HTMLFormElement
}





