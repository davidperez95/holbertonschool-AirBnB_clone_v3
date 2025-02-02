document.addEventListener('DOMContentLoaded', () => {
  const amenitiesid = [];
  const amenitiesnames = [];

  const boxes = document.querySelectorAll('.amenities input[type="checkbox"]');
  const amenitiestitle = document.querySelector('.amenities h4');

  boxes.forEach((amenity) => {
    amenity.addEventListener('change', () => {
      if (amenity.checked) {
        amenitiesid.push(amenity.dataset.id);
        amenitiesnames.push(amenity.dataset.name);

      } else {
        const indexid = amenitiesid.indexOf(amenity.dataset.id);
        if (indexid !== -1) amenitiesid.splice(indexid, 1);

        const indexname = amenitiesnames.indexOf(amenity.dataset.name);
        if (indexname !== -1) amenitiesnames.splice(indexname, 1);
      }

      let amenities = amenitiesnames.toString().replaceAll(',', ', ');

      if (amenities.lenght > 32) {
        amenities = amenities.substring(0, 32) + '...'
      }
    
      amenitiestitle.innerHTML = amenities;
    });
  });
});
