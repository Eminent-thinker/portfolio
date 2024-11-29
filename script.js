// Detect Operating System
function detectOS() {
    const userAgent = navigator.userAgent.toLowerCase();
    if (userAgent.indexOf("win") > -1) return "Windows";
    if (userAgent.indexOf("mac") > -1) return "MacOS";
    if (userAgent.indexOf("linux") > -1) return "Linux";
    if (userAgent.indexOf("android") > -1) return "Android";
    if (userAgent.indexOf("iphone") > -1 || userAgent.indexOf("ipad") > -1) return "iOS";
    return "Unknown OS";
}

// Capture visitor info
const visitorInfo = {
    userAgent: navigator.userAgent,
    os: detectOS(), // Add OS detection
    ip: ""  // You might want to use an external service to get the user's IP (like https://ipinfo.io)
};

// Send visitor info to the backend
fetch('/api/store-visitor', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(visitorInfo)
})
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("Visitor info stored successfully:", data);
    })
    .catch(error => {
        console.error('Error sending visitor info:', error);
    });
