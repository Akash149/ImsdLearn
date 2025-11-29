

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
        const analysis_object = {}
        // Validation: Check for empty fields
        formData.forEach(element => {
            console.log(element.name + ": " + element.value);
            if (element.value === "" ) { 
                
                showDialog({ title: 'Error', message: "Value for " + element.name + " cannot be empty.", type: 'error' });
                return;
            } 
            analysis_object[element.name] = parseFloat(element.value).toFixed(2);
        });
        console.log(typeof(formData))
        // Call  API to save analysis
        saveAnalysis(analysis_object);
        // console.log(formData)

    });
});



function saveAnalysis(analysis_obj) {
    $.ajax({
        type: "POST",
        url: "/myapp/save_analysis/",
        data: JSON.stringify(analysis_obj),
        contentType: "application/json",
        success: function(response) {
            console.log("Analysis saved successfully:", response);
            showDialog({ title: 'Success', message: "Analysis saved successfully.", type: 'success' });
        },
        error: function(xhr, status, error) {
            console.error("Error saving analysis:", error);
            showDialog({ title: 'Error', message: "Failed to save analysis.", type: 'error' });
        }
    });
}
