var randomize = functon(facts) {
	var index = Math.floor(Math.random() * 1052) + 1;
	return phrases[index];
}

$(document).ready(function() {
	$("#newFact").click(function() {
		fact = randomize(facts);
		$("#fact").html(fact);
	});


});