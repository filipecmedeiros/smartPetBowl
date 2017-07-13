document.getElementById('el').addEventListener('click', function(e){
	e.preventDefault();

	var http = new XMLHttpRequest();
	var url = "http://192.168.0.230/?abrir";
	http.open("POST", url, true);

	http.send(url);
})

