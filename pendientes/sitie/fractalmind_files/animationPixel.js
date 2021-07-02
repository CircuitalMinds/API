// The function gets called when the window is fully loaded
var canvasPix = document.getElementById("pixel"); 
var contextPix = canvasPix.getContext("2d");

// Define the image dimensions
var widthPix = canvasPix.width;
var heightPix = canvasPix.height;

// Create an ImageData object
var imagePix = contextPix.createImageData(widthPix, heightPix);

mainPix(0);

// Create the image
function createPix(offset) {
    // Loop over all of the pixels
    for (var x=0; x<widthPix; x++) {
        for (var y=0; y<heightPix; y++) {
            // Get the pixel index
            var pixindex = (y * widthPix + x) * 4;

            // Generate a xor pattern with some random noise
            var redP = ((x+offset) % 256) ^ ((y+offset) % 256);
            var greenP = ((2*x+offset) % 256) ^ ((2*y+offset) % 256);
            var blueP = 50 + Math.floor(Math.random()*100);

            // Rotate the colors
            blueP = (blueP + offset) % 256;

            // Set the pixel data
            imagePix.data[pixindex] = redP;     // Red
            imagePix.data[pixindex+1] = greenP; // Green
            imagePix.data[pixindex+2] = blueP;  // Blue
            imagePix.data[pixindex+3] = 255;   // Alpha
        }
    }
}

// Main loop
function mainPix(tframe) {
    // Request animation frames
    window.requestAnimationFrame(mainPix);

    // Create the image
    createPix(Math.floor(tframe / 10));

    // Draw the image data to the canvas
    contextPix.putImageData(imagePix, 0, 0);
}
