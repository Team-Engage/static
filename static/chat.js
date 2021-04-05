// var socket = io();

var messages = document.getElementById("chat-msgs");
var form = document.getElementById("chat-form");
var input = document.getElementById("chat-input");

function add_msg(msg) {
  var item = document.createElement("li");
  item.textContent = msg;
  messages.appendChild(item);
  window.scroll(0, document.body.scrollHeight);
}

form.addEventListener("submit", function(e) {
  e.preventDefault();
  if (input.value) {
//  socket.emit("chat message", input.value);
    input.value = "";
  }
});

// socket.on("chat message", add_msg(msg));