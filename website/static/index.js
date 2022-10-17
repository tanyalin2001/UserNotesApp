function deleteNote(noteId) { // take the note id we passed, send a post request to the delete note end point
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => { // then refresh the window
    window.location.href = "/";
  });
}