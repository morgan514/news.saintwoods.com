function updateTime() {
    const now = new Date();
    const timeString = now.toLocaleTimeString();
    const dateString = now.toLocaleDateString();
    document.getElementById('local-time').innerText = `LOCAL TIME:  ${dateString} -- ${timeString}`;
}
setInterval(updateTime, 1000);

updateTime();
