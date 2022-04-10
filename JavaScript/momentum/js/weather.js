const API_KEY = '705da7de01195f9445064176c704b749';

function onGeoOk(position) {
	const lat = position.coords.latitude;
	const lon = position.coords.longitude;
	const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
	fetch(url) // fetch : promise입니다..ㅎㅎ..
		.then((response) => response.json())
		.then((data) => {
			const weather = document.querySelector('#weather span:first-child');
			const city = document.querySelector('#weather span:last-child');
			city.innerText = data.name;
			weather.innerText = data.weather[0].main;
		});
}
function onGeoError(params) {
	alert("Can't find you. No weather for you.");
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
