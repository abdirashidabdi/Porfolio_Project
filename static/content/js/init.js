(function($){
  $(function(){

    $('.sidenav').sidenav();

  }); // end of document ready
})(jQuery); // end of jQuery name space

document.addEventListener('DOMContentLoaded', function() {
  const elems = document.querySelectorAll('.materialboxed');
  const instances = M.Materialbox.init(elems, options);
});