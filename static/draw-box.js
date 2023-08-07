
const form = document.getElementById('form2');
const csrftoken = form.querySelector('[name=csrfmiddlewaretoken]').value;
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const image = document.getElementById('image');

// Draw the image onto the canvas
image.addEventListener('load', () => {
    canvas.width = image.width;
    canvas.height = image.height;
    ctx.drawImage(image, 0, 0);
});

let isDrawing = false;
let startX = 0;
let startY = 0;
let endX = 0;
let endY = 0;

// Add event listeners to capture mouse events
canvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    startX = e.offsetX;
    startY = e.offsetY;
});

canvas.addEventListener('mousemove', (e) => {
    if (isDrawing) {
        endX = e.offsetX;
        endY = e.offsetY;

        // Clear the canvas and redraw the image
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(image, 0, 0);

        // Draw the box
        ctx.strokeStyle = 'red';
        ctx.strokeRect(startX, startY, endX - startX, endY - startY);
    }
});

canvas.addEventListener('mouseup', (e) => {
    isDrawing = false;
});
  // Submit the box coordinates to your Django view
  const data = {
    startX: startX,
    startY: startY,
    endX: endX,
    endY: endY,
};

const okButton = document.getElementById('ok-button');

okButton.addEventListener('click', () => {
    // Submit the box coordinates to your Django view
    const data = {
        startX: startX,
        startY: startY,
        endX: endX,
        endY: endY,
    };

    fetch('http://127.0.0.1:8000/processapp/image_upload_view/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
    });
});


