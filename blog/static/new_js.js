document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.fixed-action-btn');
  var instances = M.FloatingActionButton.init(elems);
});


message_element = document.getElementById("flash_message");

setTimeout(function(){
  message_element.style.display = "none";
}, 3000)



document.addEventListener('DOMContentLoaded', function() {
   var elems = document.querySelectorAll('.select');
   var instances = M.FormSelect.init(elems);
 });

 document.addEventListener('DOMContentLoaded', function() {
   var elems = document.querySelectorAll('.collapsible');
   var instances = M.Collapsible.init(elems);
 });


 document.addEventListener('DOMContentLoaded', function() {
   var elems = document.querySelectorAll('.materialboxed');
   var instances = M.Materialbox.init(elems);
 });
