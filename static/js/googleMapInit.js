"use strict";

function initMap() {
    // Initialize Google Maps URI constant
    const GOOGLE_MAPS_GEOCODER = "https://maps.googleapis.com/maps/api/geocode/";

    // Set up address components
    var locationAddress = $("#location-address");
    var streetLine1 = locationAddress.attr("data-street-line-1");
    var streetLine2 = locationAddress.attr("data-street-line-2");
    var city = locationAddress.attr("data-city");
    var state = locationAddress.attr("data-state-or-province");
    var postal = locationAddress.attr("data-postal-or-zip-code");
    var country = locationAddress.attr("data-country");
    var fullAddressString = [
        streetLine1,
        streetLine2,
        city,
        state,
        postal,
        country
    ].join(" ");

    // Encode full URI for geocoding request
    var encodedAddressURI = encodeURI(GOOGLE_MAPS_GEOCODER + "json?" + fullAddressString);

    // Call the geocoder to get coordinates
    var lat, long;
    $.ajax({
        url: encodedAddressURI,
        dataType: "json",
        success: function(data) {
            lat = data["results"]["geometry"]["location"]["lat"];
            long = data["results"]["geometry"]["location"]["lng"];
        }
    });

    // Create the map
    var map;
    map = new google.maps.Map($("#map"), {
        center: {lat: lat, lng: long},
        zoom: 8
    });
}

initMap();