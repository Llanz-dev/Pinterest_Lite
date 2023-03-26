const image_preview = document.getElementById('image-preview');
const first_letter = document.getElementById('first-letter');
const image_input = document.getElementById('id_profile_picture');

// Add an event listener to the image input
image_input.addEventListener('change', function() {
    // When a file is selected, create a FileReader object
    const file = this.files[0];
    const reader = new FileReader();
    // When the FileReader finishes loading the file, display the image preview
    reader.addEventListener('load', function() {
        image_preview.src = reader.result;        
        image_preview.style.display = 'block';
        first_letter.style.display = 'none';
    });
  
    // Read the selected file as a data URL
    reader.readAsDataURL(file);
  });
  