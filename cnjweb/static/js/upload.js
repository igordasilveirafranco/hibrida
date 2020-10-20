$(document).ready(function() {
    $('#form_pdf').on('submit', function(event) {
        event.preventDefault();
        var formData = new FormData($('#form_pdf')[0]);
        $.ajax({
            xhr: function() {
                var xhr = new XMLHttpRequest();
                xhr.upload.addEventListener('progress', function(e) {
                    if (e.lengthComputable) {
                        // console.log('Bytes Loaded: ' + e.loaded);
                        // console.log('Total :' + e.total);
                        // console.log('Percentage : ' + (e.loaded / e.total));
                        var percent = Math.round((e.loaded / e.total) * 100);
                        $("#progress_bar").attr('aria-valuenow', percent).css('width', percent + '%').text(percent + "%");
                    }
                })
                return xhr
            },
            type: 'POST',
            url: ' ',
            data: formData,
            processData: false,
            contentType: false,
            success: function() {
                window.location.href = "http://127.0.0.1:8000/advogado/concluido";
            },
        });

    })

});