// Initialize map
function initMap() {
    const mapOptions = {
        center: { lat: 37.7749, lng: -122.4194 },
        zoom: 12,
    };

    const map = new google.maps.Map(document.getElementById("map"), mapOptions);

    // Sample stations - replace with API data
    const stations = [
        { id: 1, name: "Station A", lat: 37.7749, lng: -122.4194, availability: "Available", price: "$0.30/min", speed: "50 kW" },
        { id: 2, name: "Station B", lat: 37.7849, lng: -122.4094, availability: "Occupied", price: "$0.25/min", speed: "40 kW" },
    ];

    // Add markers to map
    stations.forEach(station => {
        const marker = new google.maps.Marker({
            position: { lat: station.lat, lng: station.lng },
            map,
            title: station.name,
        });

        // Show station info on marker click
        marker.addListener("click", () => {
            displayStationInfo(station);
        });
    });
}

// Display station info
function displayStationInfo(station) {
    const stationDetails = document.getElementById("station-details");
    stationDetails.innerHTML = `
        <h3>${station.name}</h3>
        <p>Availability: ${station.availability}</p>
        <p>Price: ${station.price}</p>
        <p>Charging Speed: ${station.speed}</p>
    `;
}

// Book slot
function bookSlot() {
    const time = document.getElementById("charging-time").value;
    alert(`Slot booked for ${time} hours!`);
    // Send booking data to backend (e.g., using fetch API)
}

fetch('/api/stations')
    .then(response => response.json())
    .then(data => {
        console.log(data); // Handle data from backend
    })
    .catch(error => console.error('Error:', error));



function initMap() {
    const mapOptions = {
        center: { lat: 37.7749, lng: -122.4194 },
        zoom: 12,
    };
    const map = new google.maps.Map(document.getElementById("map"), mapOptions);

    // Sample stations - replace with actual API data
    const stations = [
        { lat: 37.7749, lng: -122.4194, name: "Station A" },
        { lat: 37.7849, lng: -122.4294, name: "Station B" },
    ];

    stations.forEach(station => {
        const marker = new google.maps.Marker({
            position: { lat: station.lat, lng: station.lng },
            map: map,
            title: station.name,
        });
    });
}
