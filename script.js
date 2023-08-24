document.getElementById("apiForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const requestData = {};
    formData.forEach((value, key) => {
        requestData[key] = value;
    });

    fetch(event.target.action, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(requestData),
    })
    .then(response => response.json())
    .then(data => {
        const responseDiv = document.getElementById("response");
        bmi = JSON.stringify(data["bmi"])
        responseDiv.innerHTML = `Your Body Mass Index is ${bmi}`;

    })
    .catch(error => {
        console.error("API error:", error);
        // Handle errors here
    });
});