// Load saved notes
const notesList = document.getElementById("notesList");
const input = document.getElementById("noteInput");
let notes = JSON.parse(localStorage.getItem("notes") || "[]");

function renderNotes() {
  notesList.innerHTML = "";
  notes.forEach((note, index) => {
    const li = document.createElement("li");
    li.className = "p-3 bg-white rounded-lg shadow flex justify-between items-center animate-fadeIn";
    li.innerHTML = `
      <span>${note}</span>
      <button onclick="deleteNote(${index})" 
        class="text-red-500 hover:text-red-700">❌</button>
    `;
    notesList.appendChild(li);
  });
}

function addNote() {
  const text = input.value.trim();
  if (!text) return;
  notes.push(text);
  localStorage.setItem("notes", JSON.stringify(notes));
  input.value = "";
  renderNotes();
}

function deleteNote(index) {
  notes.splice(index, 1);
  localStorage.setItem("notes", JSON.stringify(notes));
  renderNotes();
}

renderNotes();
