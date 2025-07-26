function requestOTP() {
    const phone = document.getElementById('phone').value;
     if (!mobile.match(/^\d{10}$/)) {
        alert("Please enter a valid 10-digit mobile number.");
        return;
    }
    
    fetch('/api/request-otp/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ phone })
    })
    .then(response => response.json())
    .then(data => alert(data.message || data.error));
}
