function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginRight = "0";
}

var closebtns = document.getElementsByClassName("close");
var i;

for (i = 0; i < closebtns.length; i++) {
  closebtns[i].addEventListener("click", function() {
    this.parentElement.style.display = 'none';
  });
}

// var input = document.getElementById("note");
// input.addEventListener("keypress", function(event) {
//   if (event.key === "Enter") {
//     event.preventDefault();
//     document.getElementById("submit").click();
//   }
// });




function deleteNote(noteId){
  fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({noteId:noteId})
  }).then((_res) => {
    window.location.href = '/notes';
  });
}

