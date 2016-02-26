var inp = $('input[name="pic"]');
var canvas = document.getElementById('picturebox');
var ctx = canvas.getContext('2d');

$('canvas').sketch();

$('#submitForm').on('click', function(evt) {
    evt.preventDefault();
    var canvas = document.getElementById('picturebox');
    var imgData = canvas.toDataURL();
    
    inp.val(imgData);
    
    $('form').trigger('submit');     
});
