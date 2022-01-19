// --------------------------------------- //
//       Authors: Kristina Kacmarova       //
//                Miranda Postma       	   //
//                Ridwan Bari              //
//                Winston Herold           //
//       Python Version: 3.7.4             //
//       Created on: 2022-01-18            //
// --------------------------------------- //

$(document).ready(function() {
    var readURL = function(input) {
    	if (input.files && input.files[0]) {
    		var reader = new FileReader();
    		reader.onload = function (e) {
    			$('.profile-pic').attr('src', e.target.result);
    		}
    		reader.readAsDataURL(input.files[0]);
    	}
    }
    $(".file-upload").on('change', function(){
    	readURL(this);
    });
    $(".upload-button").on('click', function() {
    	$(".file-upload").click();
    });
});
