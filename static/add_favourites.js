function addToFavourites(problem_name, problem_url) {
    fetch('/add_to_favourites', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: problem_name,
            url: problem_url
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log("Hi")
            const msgBox = document.createElement('div');
            msgBox.innerText = "Added to favourites!";
            msgBox.style.position = "fixed";
            msgBox.style.top = "20px";
            msgBox.style.left = "50%";
            msgBox.style.transform = "translateX(-50%)";
            msgBox.style.backgroundColor = "white";
            msgBox.style.color = "black";
            msgBox.style.padding = "12px 24px";
            msgBox.style.borderRadius = "8px";
            msgBox.style.zIndex = "9999";
            msgBox.style.boxShadow = "0px 4px 8px rgba(0,0,0,0.2)";
            msgBox.style.fontFamily = "Arial";
            msgBox.style.fontSize = "16px";
            document.body.appendChild(msgBox);

            setTimeout(() => {
                msgBox.remove();
            }, 1500);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}