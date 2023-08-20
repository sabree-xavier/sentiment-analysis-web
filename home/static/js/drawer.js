// JavaScript to toggle the drawer
const toggleButton = document.getElementById('toggleDrawer');
const drawer = document.getElementById('drawer');

toggleButton.addEventListener('click', () => {
    drawer.classList.toggle('open');
});