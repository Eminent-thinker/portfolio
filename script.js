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

// Fetch Location Using ipinfo.io API
// async function fetchLocation() {
//     try {
//         const response = await fetch("https://ipinfo.io/json?token=your_ipinfo_token");
//         if (!response.ok) throw new Error("Failed to fetch location data.");
//         const data = await response.json();
//         return `${data.city}, ${data.region}, ${data.country}`;
//     } catch (error) {
//         console.error(error);
//         return "Unable to determine location.";
//     }
// }

// Display Visitor Info
async function displayVisitorInfo() {
    const osInfo = detectOS();
    document.getElementById("os-info").textContent = `Operating System: ${osInfo}`;
    // const locationInfo = await fetchLocation();
    // document.getElementById("location-info").textContent = `Location: ${locationInfo}`;
}

// Collapsible Sections
document.addEventListener("DOMContentLoaded", () => {
    const headers = document.querySelectorAll(".collapsible-header");
    headers.forEach(header => {
        header.addEventListener("click", () => {
            const content = header.nextElementSibling;
            content.style.display = content.style.display === "block" ? "none" : "block";
        });
    });
    displayVisitorInfo();
});
