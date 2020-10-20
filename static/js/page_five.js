var load_field = document.getElementById('load_field');
var check_options = document.querySelectorAll(".doc_option");
var input_field = document.getElementById("input_field");
var loader = document.getElementById('loader');

input_field.addEventListener('click', () => {
    load_field.removeAttribute('disabled');
})

load_field.addEventListener('click', (e) => {
    loader.classList.remove('hidden');
    loader.classList.add('show');
})
