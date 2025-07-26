function submitReport() {
    const phone = document.getElementById('phone').value;
    const image = document.getElementById('image').files[0];
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;
    const location = document.getElementById('location').value;

    const formData = new FormData();
    formData.append('phone', phone);
    formData.append('image', image);
    formData.append('latitude', latitude);
    formData.append('longitude', longitude);
    formData.append('location', location);

    fetch('/api/submit-report/', {
        method: 'POST',
        body: formData
    })
    .then(res => res.json())
    .then(data => alert(data.message || data.error));
}


navigator.geolocation.getCurrentPosition(function(position) {
    document.getElementById('latitude').value = position.coords.latitude;
    document.getElementById('longitude').value = position.coords.longitude;
});
