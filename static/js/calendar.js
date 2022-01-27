// --------------------------------------- //
//       Authors: Kristina Kacmarova       //
//                Miranda Postma       	   //
//                Ridwan Bari              //
//                Winston Herold           //
//       Python Version: 3.7.4             //
//       Created on: 2022-01-18            //
// --------------------------------------- //



const modal = document.querySelector(".modal");
const trigger = document.querySelector(".trigger");
const closeButton = document.querySelector(".close-button");

function toggleModal() {
    modal.classList.toggle("show-modal");
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

trigger.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);


// function openForm() {
//   document.getElementById("myForm").style.display = "block";
// }
// 
// function closeForm() {
//   document.getElementById("myForm").style.display = "none";
// }

// $(document).ready(function() {
// 
// 	function loadFile(form, filename) {    	
//  		const formData = new FormData(form); 		
//  		var oReq = new XMLHttpRequest(); 		
//  		oReq.open("POST", "calendar", true); 		
//  		oReq.send(formData);
//  		oReq.onload = function(oEvent) {
//     		document.getElementById("text").innerHTML = oReq.response;
//      	};
// 	}
// 	
//     $(".calendar-select").on('change', function() {
//     	document.getElementById('scroll').style.visibility = "hidden"; 
//     	document.getElementById("text2").innerHTML = "";
//     	document.getElementById("text").innerHTML = "Loading...";
//     	document.getElementById("middle").style.opacity = "0.5";
// //     	loadFile(this.form, this.files[0].name);
//     });
//     
//     $(".calendar-button").on('click', function() {
//     	$(".calendar-select").click();
//     });
//     
// });


