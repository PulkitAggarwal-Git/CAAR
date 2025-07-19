window.onload = function () {
        const msgBox = document.createElement('div');
        msgBox.innerText = "Please enter your username!";
        msgBox.style.position = "fixed";
        msgBox.style.top = "20px";
        msgBox.style.left = "50%";
        msgBox.style.transform = "translateX(-50%)";
        msgBox.style.backgroundColor = "#f44336";
        msgBox.style.color = "white";
        msgBox.style.padding = "12px 24px";
        msgBox.style.borderRadius = "8px";
        msgBox.style.zIndex = "9999";
        msgBox.style.boxShadow = "0px 4px 8px rgba(0,0,0,0.2)";
        msgBox.style.fontFamily = "Arial";
        msgBox.style.fontSize = "16px";
        document.body.appendChild(msgBox);

        setTimeout(() => {
            msgBox.remove();
        }, 3000);
    };