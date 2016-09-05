
var currentBackground = 0;
var backgrounds = [];
backgrounds[0] = "../static/bg1.jpg";
backgrounds[1] = "../static/bg2.jpg";
backgrounds[2] = "../static/bg3.jpg";

function changeBackground() {
	currentBackground++;
	if(currentBackground > 2)
		currentBackground = 0;

	$('body').fadeOut(0,function() {
		$('body').css({
			'background-image' : "url('" + backgrounds[currentBackground] + "')"
		});
		$('body').fadeIn(0);
	});
	setTimeout(changeBackground, 5000);
}

$(document).ready(function() {
	setTimeout(changeBackground, 5000);        
});

$( function() {
	$( "#movie-name").autocomplete({
		source: movieNames
	});
} );

function submitName() {
	var submitMovieName = document.getElementById("movie-name").value;
	submitMovieName = sanitizeString(submitMovieName);
	$('#movie-name').val(submitMovieName);
}

/**
* Sanitizes users entered string - replaces all
* special characters except comonly used
* and performs a global, case insensitive match.
* @param {string} stringInput
* @return {string} stringInput
*/
function sanitizeString(stringInput){
stringInput = stringInput.replace(/[^a-z0-9 \.,':_-]/gim,"");
return stringInput.trim();
}