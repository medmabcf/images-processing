const form = document.getElementById('form1');
const csrftoken = form.querySelector('[name=csrfmiddlewaretoken]').value;
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const image = document.getElementById('image');
function resizeImage(image){
    var aspectRatio = image.naturalWidth / image.naturalHeight;

    // Set the size of the canvas
    var maxWidth = 800;
    var maxHeight = 500;
    if (maxWidth / maxHeight > aspectRatio) {
        new_width = maxHeight * aspectRatio;
        new_height = maxHeight;
    } else {
        new_width = maxWidth;
        new_height = maxWidth / aspectRatio;
    }
    return [new_width, new_height]
}
// Draw the image onto the canvas
image.addEventListener('load', () => {
    
         [canvas.width ,canvas.height] = resizeImage(image)
    
 
     
     ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
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

    console.log(startX);

    updateData();
    

});

canvas.addEventListener('mousemove', (e) => {
    if (isDrawing) {
       
        [canvas.width ,canvas.height] = resizeImage(image)
        endX = e.offsetX;
        endY = e.offsetY;
        updateData();
        // Clear the canvas and redraw the image
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
        // Draw the box
        ctx.strokeStyle = 'red';
        ctx.strokeRect(startX, startY, endX - startX, endY - startY);
    }
});

canvas.addEventListener('mouseup', (e) => {
    isDrawing = false;
});

const data = {
    startX: startX,
    startY: startY,
    endX: endX,
    endY: endY,
};


function updateData() {
    data.startX = startX;
    data.startY = startY;
    data.endX = endX;
    data.endY = endY;
}

 
  
 


const okButton = document.getElementById('ok-button');

okButton.addEventListener('click', () => {
    // Log the data object
    console.log(data);

      // Submit the box coordinates to your Django view
  var [new_width, new_height] = resizeImage(image);
  var width_scale=image.naturalWidth/new_width
  var height_scale=image.naturalHeight/new_height
    startX*=width_scale,
    startY*=height_scale,
   endX*=width_scale,
   endY*=height_scale,
   updateData()
    console.log(data);
    const centerdata = {
        centerX : (startX + endX) / 2,
        centerY : (startY + endY) / 2,
        image_width : image.naturalWidth,
        image_height : image.naturalHeight,
    };

    // Submit the box coordinates to your Django view
    fetch('http://127.0.0.1:8000/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({cord:centerdata,path:image.src}),
    });
});



