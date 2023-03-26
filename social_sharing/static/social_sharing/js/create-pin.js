// Get the necessary DOM elements
const image_input = document.getElementById('id_image');
const pin_image = document.getElementById('pin-image');
const picture_col = document.getElementsByClassName('upload-picture-col')[0];
const link_field_custom = document.getElementById('link-field-custom');
const image_preview = document.getElementById('image-preview');
const delete_button = document.getElementById('delete-button');

// Add an event listener to the image input
image_input.addEventListener('change', function() {
  // When a file is selected, create a FileReader object
  const file = this.files[0];
  const reader = new FileReader();

  // When the FileReader finishes loading the file, display the image preview
  reader.addEventListener('load', function() {
    // Set the source of the image to the loaded file
    pin_image.src = reader.result;
    // Hide the upload picture column and show the image preview
    picture_col.style.display = 'none';
    image_preview.style.display = 'flex';

    // Center the image preview vertically and horizontally
    image_preview.style.flexDirection = 'column';
    image_preview.style.justifyContent = 'center';
    image_preview.style.alignItems = 'center';
    
    // Set the height and background color of the image preview
    image_preview.style.height = '400px';
    image_preview.style.backgroundColor = '#EEEEEF';
    
    // Center the image preview horizontally
    image_preview.style.margin = '0 auto';
    
    // Show the delete button
    delete_button.style.display = 'block';
  });

  // Read the selected file as a data URL
  reader.readAsDataURL(file);
});

// Add an event listener to the remove image button
delete_button.addEventListener("click", function() {
  // When the delete button is clicked, hide the image preview and show the upload picture column
  delete_button.style.display = 'none';
  image_preview.style.display = 'none';
  image_preview.style.position = 'relative';
  picture_col.style.display = 'flex';
});
