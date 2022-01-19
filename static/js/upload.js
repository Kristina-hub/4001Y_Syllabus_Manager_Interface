// --------------------------------------- //
//       Authors: Kristina Kacmarova       //
//                Miranda Postma       	   //
//                Ridwan Bari              //
//                Winston Herold           //
//       Python Version: 3.7.4             //
//       Created on: 2022-01-18            //
// --------------------------------------- //

// $(document).ready(function() {
//     var readURL = function(input) {
//     	if (input.files && input.files[0]) {
//     		var reader = new FileReader();
//     		reader.onload = function (e) {
//     			$('.profile-pic').attr('src', e.target.result);
//     		}
//     		reader.readAsDataURL(input.files[0]);
//     		reader.readAsText(input.files[0])
//     	}
//     }
//     $(".file-upload").on('change', function(){
//     	readURL(this);
//     	document.getElementById("status").innerHTML = "File Uploaded";
//     	var name = document.getElementById('input-file'); 
//     	var str = "name: " + name.files.item(0).name + " type: " + name.files.item(0).type;
//     	document.getElementById("filename").innerHTML = str;
//     });
//     $(".upload-button").on('click', function() {
//     	$(".file-upload").click();
//     });
// });


$(document).ready(function() {
//     var readURL = function(input) {
//     	if (input.files && input.files[0]) {
//     		var reader = new FileReader();
//     		reader.onload = function (e) {
//     			$('.profile-pic').attr('src', e.target.result);
//     		}
//     		reader.readAsDataURL(input.files[0]);
//     		// reader.readAsText(input.files[0])
//     		
//     		document.getElementById("status").innerHTML = "File Uploaded";
//     		var con = reader.readAsText(input.files[0]);
//     		document.getElementById("filename").innerHTML = con;
//     	}
//     }
    
// 	function readFileContent(file) {
// 		const reader = new FileReader()
// 	  	return new Promise((resolve, reject) => {
// 		reader.onload = event => resolve(event.target.result)
// 		reader.onerror = error => reject(error)
// 		reader.readAsText(file)
// 	  })
// 	}
// 
// 	function placeFileContent(target, file) {
// 		readFileContent(file).then(content => {
// 		target.value = content}).catch(error => console.log(error))
// 	}
// 	
// 	function getFile(event) {
// 		const input = event.target
// 	  	if ('files' in input && input.files.length > 0) {
// 		  placeFileContent(document.getElementById('content-target'), input.files[0])
// 	  	}
// 	}

	function loadFileAsText(){
	  var fileToLoad = document.getElementById("input-file").files[0];
// 	  document.getElementById("status").value = fileToLoad;
	  
	  var fileReader = new FileReader();
	  fileReader.onload = function(fileLoadedEvent){
		  var textFromFileLoaded = fileLoadedEvent.target.result;
		  //document.getElementById("filename").value = textFromFileLoaded;
		  document.getElementById("filename").innerHTML = textFromFileLoaded;
	  };
	  fileReader.readAsText(fileToLoad, "UTF-8");
	}
    
    
    $(".file-upload").on('change', function(){
    	loadFileAsText();
//     	readURL(this);
//     	getFile(this);
    });
    $(".upload-button").on('click', function() {
    	$(".file-upload").click();
    });
});


// document.getElementById('input-file').addEventListener('change', getFile)

