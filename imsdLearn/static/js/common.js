

// window.onload = function() {
//     console.log("Page is loaded");
//     alert("I am common.js file");
// }

$(document).ready(function() {
    console.log("Document is ready");
    // alert("I am common.js file inside document ready");

    $('#analysis_form').submit(function(event) {
        event.preventDefault(); // Prevent the default form submission
        console.log(event)
        // var formData = $(this).serialize(); // Serialize form data
        var formData = $(this).serializeArray(); // Serialize form data to JSON
        
        // Validation: Check for empty fields
        formData.forEach(element => {
            console.log(element.name + ": " + element.value);
            if (element.value === "" ) { 
                showDialog({ title: 'Error', message: "Value for " + element.name + " cannot be empty.", type: 'error' });
                return;
            }
        });
        console.log(typeof(formData))
        // console.log(formData)

    });
});
