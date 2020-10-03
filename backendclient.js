
const serverURL = "http://localhost:5000";

function connectToServer()
{
    // We should return a Promise here.
    // Also, start doing the backend please. 
	// We need to be testing things as we go.
	fetch(serverURL)
		.then(function (response) {
			response.json()
				.then(function (json) {
					console.log(json);
					return true;
				})
				.catch(function (error) {
					console.log(json);
					return false;
				});
		})
		.catch(function (error) {
			console.log(error);
			return false;
		});
}

connectToServer();
