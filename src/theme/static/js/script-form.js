window.addEventListener("DOMContentLoaded", () => {
    // Entry form
    function handlingNewEntry(){
        const dropZones = document.querySelectorAll(".input_container_dropdown");
        dropZones.forEach((dropZone) => {
            
            const fileInput = dropZone.querySelector(".drop-zone-input");
            const previewContainer = dropZone.querySelector(".drop-zone-preview");
            dropZone.addEventListener("click", () => {
                fileInput.click();
            });
          
            dropZone.addEventListener("dragover", (e) => {
                e.preventDefault();
                dropZone.classList.add("drop-zone-active");
            });
        
            dropZone.addEventListener("dragleave", () => {
                dropZone.classList.remove("drop-zone-active");
            });
        
            dropZone.addEventListener("drop", (e) => {
                e.preventDefault();
                dropZone.classList.remove("drop-zone-active");
        
                const files = e.dataTransfer.files;
                if (files.length > 0) {
                    fileInput.files = files;
                    displayImagePreview(files[0], previewContainer);
                }
            });
        
            fileInput.addEventListener("change", () => {
                const files = fileInput.files;
                if (files.length > 0) {
                    displayImagePreview(files[0], previewContainer);
                }
            });
        });
    }
    function displayImagePreview(file, container) {
        const reader = new FileReader();

        reader.onload = function (e) {
            const imagePreview = document.createElement("div");
            imagePreview.classList.add("drop-zone__image-preview");

            const image = document.createElement("img");
            image.src = e.target.result;
            image.alt = file.name;

            imagePreview.appendChild(image);
            container.innerHTML = "";
            container.appendChild(imagePreview);
        };
        
        reader.readAsDataURL(file);
    }
    handlingNewEntry();
    // Report form
    var addButton = document.getElementById('report-add-button');
    var formList = document.getElementById('report-form-list');
    var totalForms = document.getElementById('id_player_entries-TOTAL_FORMS');
    var reportForm = document.getElementsByClassName('report-form')
    const reportEmpty = document.getElementById('report-form-empty');
    addButton.addEventListener('click', cloneMore);
    function cloneMore(e) {
        if (e)
                e.preventDefault();
                let currentCount = reportForm.length;
                var newElement = reportEmpty.cloneNode(true);
                const formRegex = RegExp('__prefix__', 'g');
    
                newElement.setAttribute('class', 'report-form flex flex-col justify-center items-center m-3');
                newElement.classList.remove('hidden');
                newElement.setAttribute('id', `player-entry-form-${currentCount}`);
                newElement.innerHTML = newElement.innerHTML.replace(formRegex, currentCount);
                totalForms.setAttribute('value', currentCount + 1);
                formList.appendChild(newElement);
                handlingNewEntry();
    }
    var playerForm = document.getElementById('form-player-info');
    var reportFormEntries = document.getElementById('form-report-entries');
    const nextButton = document.getElementById('next-button');
    const previousButton = document.getElementById('previous-button');
    const submitButton = document.getElementById('submit-button');
    function nextHandler(){
        playerForm.classList.add('form_hidden');
        playerForm.classList.remove('form_visible');
        reportFormEntries.classList.remove('form_hidden');
        reportFormEntries.classList.add('form_visible');
        previousButton.classList.remove('hidden');
        nextButton.classList.add('hidden');
        submitButton.classList.remove('hidden');
    };
    nextButton.addEventListener('click', nextHandler);
    function previousHandler(){
        playerForm.classList.remove('form_hidden');
        playerForm.classList.add('form_visible');
        reportFormEntries.classList.remove('form_visible');
        reportFormEntries.classList.add('form_hidden');
        previousButton.classList.add('hidden');
        nextButton.classList.remove('hidden');
        submitButton.classList.add('hidden');
    }
    previousButton.addEventListener('click', previousHandler);
});