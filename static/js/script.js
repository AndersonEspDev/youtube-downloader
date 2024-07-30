function downloadVideo() {
  const url = document.getElementById('url').value
  const message = document.getElementById('message')

  if (!url) {
    message.textContent = 'Please enter a YouTube video URL.'
    return
  }

  fetch('/download', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ url: url })
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        message.textContent = 'Download started!'
        // Redireciona para o endpoint de download para iniciar o download
        window.location.href = `/download/${data.filename}`
      } else {
        message.textContent = `Error: ${data.error}`
      }
    })
    .catch(error => {
      message.textContent = `Error: ${error}`
    })
}
