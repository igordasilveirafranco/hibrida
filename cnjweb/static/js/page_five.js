var send_file = document.getElementById('send_file');
var check_options = document.querySelectorAll(".doc_option");
var input_file = document.getElementById("input_file");
var button_submit_pdf = document.getElementsByClassName('button_submit_pdf');



check_options.forEach(function(index) {
    index.addEventListener('click', () => {
        if ((index.checked == true)) {
            if (index.value == "pdf") {
                $("#pdf_option_modal").modal('show');
                // send_file.setAttribute('data-target', '#pdf_option_modal');
                return false;
            } else {
                send_file.removeAttribute('data-target', '#pdf_option_modal');
                send_file.removeAttribute('disabled');

            }
        }
    })
})

function NewInput() {
    send_file.removeAttribute('disabled');
    send_file.click();
    $("#pdf_option_modal").modal('hide');

}