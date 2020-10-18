// $('.pagination li').click(function() {
//     $(this).siblings('li').removeClass('active');
//     $(this).addClass('active');
// });
var search_btn = document.getElementById('search_btn');
var search_field = document.getElementById('search_field');
var search_field_two = $('#search_field');
var box_files = document.getElementsByClassName('box_files');
var file_icon = document.querySelectorAll('.fa-folder');

var folder_title = $(".folder_title").text();
search_field_two.on("input", function() {
    var digitado = search_field_two.val();
    var comparavel = folder_title.val();
    console.log(comparavel)
    if (digitado == comparavel) {
        folder_title.addClass("world_bgc");
    } else {
        folder_title.removeClass("world_bgc");
    }
});


search_btn.addEventListener('click', (e) => {
    e.preventDefault();
    console.log(search_field.value);
})

file_icon.forEach((value, index, array) => {
    value.addEventListener('click', () => {
        console.log("click")
        value.classList.toggle('fa-folder-open');

    })

})