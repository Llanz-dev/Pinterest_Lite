const image_input = document.getElementById('id_image');
const pin_image = document.getElementById('pin-image');
const picture_col = document.getElementsByClassName('upload-picture-col')[0];
const link_field_custom = document.getElementById('link-field-custom');
const image_preview = document.getElementById('image-preview');
const delete_button = document.getElementById('delete-button');


image_input.addEventListener('change', function() {
  const file = this.files[0];
  const reader = new FileReader();

  reader.addEventListener('load', function() {
    pin_image.src = reader.result;
    picture_col.style.display = 'none';
    image_preview.style.display = 'flex';
    image_preview.style.flexDirection = 'column';
    image_preview.style.justifyContent = 'center';
    image_preview.style.alignItems = 'center';
    image_preview.style.height = '400px';
    image_preview.style.backgroundColor = '#EEEEEF';
    image_preview.style.margin = '0 auto';
    delete_button.style.display = 'block';
  });

  reader.readAsDataURL(file);
});

// Add an event listener to the remove image button
delete_button.addEventListener("click", function() {
  delete_button.style.display = 'none';
  image_preview.style.display = 'none';
  image_preview.style.position = 'relative';
  picture_col.style.display = 'flex';

});