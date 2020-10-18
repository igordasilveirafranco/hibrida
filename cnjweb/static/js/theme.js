const checkbox = document.querySelector('#theme_choice');

checkbox.addEventListener('change', () => {
    console.log("aqui chegou")
    document.body.classList.toggle('dark');

})