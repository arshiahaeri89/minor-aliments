document.addEventListener("DOMContentLoaded", function(){
  let navbar_height = document.querySelector('.navbar').offsetHeight;
  document.body.style.paddingTop = navbar_height + 'px';
});