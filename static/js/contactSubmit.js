"use strict";

$("#form-contact2").submit(function(event) {
    event.preventDefault();
    var data = $(this).serializeArray();
    var formURL = $(this).attr("action");
    $.ajax({
        url: formURL,
        type: "POST",
        data: data,
        success: function() {
            alert('sent');
        }
    })
});