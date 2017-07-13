document.getElementById('el').addEventListener('click', function(e){
	e.preventDefault();

	var http = new XMLHttpRequest();
	var url = "http://192.168.0.110/?ligar";
	http.open("POST", url, true);

	
	http.send(url);

	http = new XMLHttpRequest();
	http.open('get', 'localhost:8000');
	local.reload();
})
