const input_file = document.getElementById('id_image');
const pin_image = document.getElementById('pin-image');
const picture_col = document.getElementsByClassName('upload-picture-col')[0];
const image_preview = document.getElementById('image-preview');


input_file.addEventListener('change', function() {
  const file = this.files[0];
  const reader = new FileReader();

  reader.addEventListener('load', function() {
    pin_image.src = reader.result;
    picture_col.style.display = 'none';
    image_preview.style.display = 'flex';
    image_preview.style.flexDirection = 'column';
    image_preview.style.justifyContent = 'center';
    image_preview.style.alignItems = 'center';
    image_preview.style.height = '510px';
    image_preview.style.backgroundColor = '#EEEEEF';

  });

  reader.readAsDataURL(file);
});