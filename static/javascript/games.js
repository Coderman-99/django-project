// var coll = document.getElementsByClassName("top-right");
// var i;

// for (i = 0; i < coll.length; i++) {
//   coll[i].addEventListener("click", function() {
//     this.classList.toggle("active");
//     var content = this.nextElementSibling;
//     if (content.style.display === "block") {
//       content.style.display = "none";
//     } else {
//       content.style.display = "block";
//     }
//   });
// }

let countd=0

function count(){
    countd = countd + 1
    document.getElementById("test-count").innerText = countd
}

function save(){
    let already_saved = document.getElementById("saved").innerText
    document.getElementById("saved").innerText = already_saved + countd + "-"
    countd = 0
    document.getElementById("test-count").innerText = countd
}


function add_name(){
    let name = "Munirak"
    let mr = document.getElementById("name")
    mr.innerText = name
}