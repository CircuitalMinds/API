function initSierpin() {
    var depth = parseInt(document.getElementById('depthStepper').value);
    document.getElementById("var-sn").innerHTML = depth;
    
    sierpinski = new Sierpinski();	
    
    // Constructor which initializes the canvas widget
    function Sierpinski() {
        this.w = 505;
        // Compute the height of the canvas to let an equilateral triangle
        // fit into it. Pythagoras is your friend here.
        this.h = Math.sqrt(3) / 2 * this.w;
        this.canvas = document.getElementById("sierpin");
        this.context = this.canvas.getContext("2d");
        this.maxDepth = 10;
        this.canvas.width = this.w;
        this.canvas.height = this.h;
    }

    // Draw a Sierpinski Triangle with the given recursion depth
    Sierpinski.prototype.drawSierpinskiTriangle = function(depth)
    {
        this.context.clearRect(0, 0, this.w, this.h);
        // Initialize the coordinates of an equilateral triangle which
        // fits into the canvas
        var x0 = 0, y0 = this.h - 1;
        var x1 = this.w, y1 = this.h - 1;
        var x2 = this.w/2, y2 = 0;
        var grd1 = this.context.createLinearGradient(300, 0, 0, 100);
        grd1.addColorStop(0.1, "sienna");
        grd1.addColorStop(0.5, "crimson");
        grd1.addColorStop(0.7, "indianred");
        grd1.addColorStop(1, "royalblue");
        // Draw the initial triangle (black)
        this.context.fillStyle = grd1;
        // Draw the initial triangle (black)
        this.drawTriangle(x0, y0, x1, y1, x2, y2);
        // Remove the triangle (draw white) which is defined by the 
        // midpoints of the sides of the initial triangle. Recursively
        // execute this process for the remaining 3 triangles.
        var grd2 = this.context.createLinearGradient(100, 0, 0, 300);
        grd2.addColorStop(0.1, "sienna");
        grd2.addColorStop(0.5, "crimson");
        grd2.addColorStop(0.7, "indianred");
        grd2.addColorStop(1, "royalblue");
        this.context.fillStyle = grd2;
        if (depth > this.maxDepth) { // make sure that depth doesn't get too high
            depth = this.maxDepth;
            document.getElementById('depthStepper').value = depth;
        }
        this.removeCenterTriangle(x0, y0, x1, y1, x2, y2, depth);    
    };

    // Draw a filled triangle which is defined by the points
    // (x0,y0), (x1,y1), and (x2,y2)
    Sierpinski.prototype.drawTriangle = function(x0, y0, x1, y1, x2, y2) {
        this.context.beginPath();
        this.context.moveTo(x0, y0);
        this.context.lineTo(x1, y1);
        this.context.lineTo(x2, y2);
        this.context.lineTo(x0, y0);
        this.context.fill();
    };

    // Removes the center triangle which is defined by connecting the midpoints
    // of each side.
    Sierpinski.prototype.removeCenterTriangle = function(x0, y0, x1, y1, x2, y2, depth) {
        if (depth > 0) {
            // Midpoint coordinates
            var x01 = (x0 + x1)/2, y01 = (y0 + y1)/2;
            var x02 = (x0 + x2)/2, y02 = (y0 + y2)/2;
            var x12 = (x1 + x2)/2, y12 = (y1 + y2)/2;
            // Remove the center triangle
            this.drawTriangle(x01, y01, x02, y02, x12, y12);
            if (depth > 1) {
                // Recursively remove center triangles for the
                // remaining filled triangles
                this.removeCenterTriangle(x0, y0, x01, y01, x02, y02, depth - 1);
                this.removeCenterTriangle(x01, y01, x1, y1, x12, y12, depth - 1);
                this.removeCenterTriangle(x02, y02, x12, y12, x2, y2, depth - 1);
            }
        }
    };
    var d = 0;
    var tim2 = setInterval(frame, 100);
    function frame() {
      if (d < depth) {
         d += 1;
         sierpinski.drawSierpinskiTriangle(d);
      } else {
          clearInterval(tim2);
      } 
    }  
}
