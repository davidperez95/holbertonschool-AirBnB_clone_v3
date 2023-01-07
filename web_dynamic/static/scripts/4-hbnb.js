$(document).ready(function () {
    const dict = {};
    const $amenitiesCheck = $('input[type=checkbox]');
    const $selectedAmenities = $('div.amenities h4');
    const $statusIndicator = $('div#api_status');
    const statusUri = 'http://localhost:5001/api/v1/status';
    const $placesSection = $('section.places');
    const placesUri = 'http://0.0.0.0:5001/api/v1/places_search';
    const $button = $('button');

    $button.click(function () {
        $.ajax({
            url: placesUri,
            type: 'POST',
            dataType: 'json',
            context: $amenitiesCheck,
            data: '{}',
            contentType: 'application/json',
            success: function (data) {
                for (let i = 0; i < data.length; i++) {
                    $placesSection.append(finalPlace(data[i]));
                }
            }
        })
    })
  
    $amenitiesCheck.click(function () {
      if ($(this).is(':checked')) {
        dict[$(this).data('id')] = $(this).data('name');
        $selectedAmenities.text(Object.values(dict).join(', '));
      } else if ($(this).is(':not(:checked)')) {
        delete dict[$(this).data('id')];
        $selectedAmenities.text(Object.values(dict).join(', '));
      }
    });

    function maxGuests (guests) {
        if (guests !== 1) {
            return `<div class="max_guest">${guests} Guests </div>`;
        } else {
            return `<div class="max_guest">${guests} Guest </div>`;
        }
    }

    function maxRooms (rooms) {
        if (rooms !== 1) {
            return `<div class="number_rooms">${rooms} Bedrooms </div>`;
        } else {
            return `<div class="number_rooms">${rooms} Bedroom </div>`;
        }
    }

    function maxBathrooms (bathrooms) {
        if (bathrooms !== 1) {
            return `<div class="number_bathrooms">${bathrooms} Bathrooms </div>`;
        } else {
            return `<div class="number_bathrooms">${bathrooms} Bathroom </div>`;
        }
    }

    function articleTitle (title, price) {
        return `<div class='title_box'>
                    <h2>${title}</h2>
                    <div class="price_by_night">
                        ${price}
                    </div>
                </div>`;
    }

    function articleInformation (guests, rooms, bathrooms) {
        const stringGuests = maxGuests(guests);
        const stringRooms = maxRooms(rooms);
        const stringBathrooms = maxBathrooms(bathrooms);

        return `<div class="information">
                    ${stringGuests}
                    ${stringRooms}
                    ${stringBathrooms}
                </div>`;
    }

    function articleDescription (description) {
        return `<div class="description">
                    ${description}
                </div>`;
    }

    function finalPlace (place) {
        const title = articleTitle(place.name, place.price_by_night);
        const info = articleInformation(place.max_guest, place.number_rooms, place.number_bathrooms);
        const description = articleDescription(place.description)

        return `<article>
                    ${title}
                    ${info}
                    ${description}
                </article>`;
    }

    $.ajax({
      url: statusUri,
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        if (data.status === 'OK') {
          $statusIndicator.addClass('available');
        } else {
          $statusIndicator.removeClass('available');
        }
      }
    });

    $.ajax({
        url: placesUri,
        type: 'POST',
        dataType: 'json',
        data: '{}',
        contentType: 'application/json',
        success: function (data) {
            for (let i = 0; i < data.length; i++) {
                $placesSection.append(finalPlace(data[i]));
            }
        }
    })
  });
  