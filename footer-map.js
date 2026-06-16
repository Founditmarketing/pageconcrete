// Initialize the map, centered around the Triad area
var map = L.map('footer-map').setView([36.0, -80.0], 10);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Define custom icons
var hqIcon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

var serviceIcon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

// Location data
var locations = [
    { name: "Page Concrete and Outdoor Services HQ", lat: 35.9557, lng: -80.0053, isHQ: true }, // HQ representation (High Point area)
    { name: "High Point", lat: 35.9557, lng: -80.0053, isHQ: false },
    { name: "Greensboro", lat: 36.0726, lng: -79.7920, isHQ: false },
    { name: "Winston-Salem", lat: 36.0999, lng: -80.2442, isHQ: false },
    { name: "Kernersville", lat: 36.1199, lng: -80.0736, isHQ: false },
    { name: "Thomasville", lat: 35.8826, lng: -80.0820, isHQ: false },
    { name: "Oak Ridge", lat: 36.1643, lng: -79.9861, isHQ: false },
    { name: "Summerfield", lat: 36.2026, lng: -79.9014, isHQ: false },
    { name: "Clemmons", lat: 36.0232, lng: -80.3837, isHQ: false },
    { name: "Lexington", lat: 35.8240, lng: -80.2534, isHQ: false },
    { name: "Colfax", lat: 36.1112, lng: -79.9861, isHQ: false },
    { name: "Archdale", lat: 35.9182, lng: -79.9575, isHQ: false },
    { name: "Jamestown", lat: 35.9965, lng: -79.9367, isHQ: false },
    { name: "Walkertown", lat: 36.1554, lng: -80.1492, isHQ: false },
    { name: "Walburg", lat: 35.9976, lng: -80.1389, isHQ: false },
    { name: "Trinity", lat: 35.8851, lng: -79.9920, isHQ: false },
    { name: "Union Cross", lat: 36.0596, lng: -80.1284, isHQ: false },
    { name: "Midway", lat: 35.9554, lng: -80.2225, isHQ: false }
];

// Add markers
locations.forEach(function(loc) {
    var markerOptions = loc.isHQ ? { icon: hqIcon, zIndexOffset: 1000 } : { icon: serviceIcon };
    var popupText = loc.isHQ ? "<b>" + loc.name + "</b><br>Located in High Point, NC" : "<b>Service Area</b><br>" + loc.name + ", NC";
    
    L.marker([loc.lat, loc.lng], markerOptions)
        .addTo(map)
        .bindPopup(popupText);
});
