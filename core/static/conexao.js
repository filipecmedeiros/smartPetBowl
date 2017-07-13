document.getElementById('el').addEventListener('click', function(e){
	e.preventDefault();

	var http = new XMLHttpRequest();
	var url = "http://192.168.0.160/?abrir";
	http.open("POST", url, true);

	http.send(url);
})

document.getElementById('le').addEventListener('click', function(e){
	e.preventDefault();

	var http = new XMLHttpRequest();
	var url = "http://192.168.0.160/?";
	http.open("POST", url, true);

	http.send(url);
})
