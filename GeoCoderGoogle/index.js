const address = "5099 17e avenue montréal";
function geocode() {
  if (address) {
    console.log("address ok");
    new google.maps.Geocoder()
      .geocode(
        {
          address: address,
        },
        (result) => {
          console.log("result", result);
          const data = {};
          const firstPartsRequest = result[0].address_components;
          if (firstPartsRequest) {
            firstPartsRequest.forEach((part) => {
              if (part.types.includes("country")) {
                data.country = part.long_name;
                console.log(data);
              }
              if (part.types.includes("postal_code")) {
                data.postalCode = part.long_name;
                console.log(data);
              }
              if (part.types.includes("street_number")) {
                data.number = part.long_name;
              }
              if (part.types.includes("route")) {
                data.route = `${data.number}, ${part.long_name}`;
                console.log(data);
              }
              if (part.types.includes("locality")) {
                data.locality = part.long_name;
                console.log(data);
              }
            });
            console.log(data);
            callback({ data });
          }
        }
      )
      .catch((e) => {
        alert("Geocode was not successful for the following reason: " + e);
      });
  }
}
geocode(address);
