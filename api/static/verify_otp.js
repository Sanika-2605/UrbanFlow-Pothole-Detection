function verifyOTP() {
    const userOTP = document.getElementById('otp').value;

    fetch('/api/verify-otp/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ otp })
    })
    .then(response => response.json())
    .then(data => alert(data.message || data.error));

     if (data.message) {
            document.getElementById("otp-msg").innerText = "✅ " + data.message;
            document.getElementById("otp-msg").style.color = "green";
            setTimeout(() => {
                window.location.href = "api/citizen2.html";
            }, 1000);
        } else {
            document.getElementById("otp-msg").innerText = "❌ " + data.error;
            document.getElementById("otp-msg").style.color = "red";
        }
    
}

