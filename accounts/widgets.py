from django.forms.widgets import ClearableFileInput

class CustomClearableFileInput(ClearableFileInput):
    template_with_initial = '<div class="custom-file">{initial_text}{input}\
                             <label class="custom-file-label" for="%(id)s">\
                             %(filename)s</label></div>'
