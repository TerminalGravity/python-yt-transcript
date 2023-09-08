window.onload = function() {
    const form = document.querySelector('form');

    form.onsubmit = function(e) {
        e.preventDefault();

        const url = document.querySelector('input[type="text"]').value;

        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: url })
        })
        .then(response => response.json())
        .then(data => {
            if (data.filename) {
                const downloadLink = document.createElement('a');
                downloadLink.href = `/download/${data.filename}`;
                downloadLink.innerText = 'Download Transcription';
                document.querySelector('.container').appendChild(downloadLink);
            }
        })
        .catch(error => console.error('Error:', error));
    };
};
