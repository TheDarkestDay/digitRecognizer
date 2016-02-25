var inp = $('input[type="hidden"]');
$('canvas').sketch();

$('#submitForm').on('click', function(evt) {
    evt.preventDefault();
    var canvas = document.getElementById('picturebox');
    var imgData = canvas.toDataURL();
    
    inp.val(imgData);
    
 //   $('form').trigger('submit');     
});
