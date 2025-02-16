document.addEventListener("DOMContentLoaded", function() {
    const formOld = document.querySelector("form[action='/process-data-old']");
    const formNew = document.querySelector("form[action='/process-data-new']");
    
    if (formOld) {
        formOld.addEventListener("submit", function(event) {
            event.preventDefault();
            processPrediction(formOld, "/process-data-old", "result-old");
        });
    }
    
    if (formNew) {
        formNew.addEventListener("submit", function(event) {
            event.preventDefault();
            processPrediction(formNew, "/process-data-new", "result-new");
        });
    }
    
    function processPrediction(form, url, resultId) {
        const formData = new FormData(form);
        fetch(url, {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(result => {
            document.getElementById(resultId).innerText = "Predicted Price: " + result;
        })
        .catch(error => console.error("Error:", error));
    }
});
