var c = parseFloat(document.getElementById('c').value);
var h = 0.01;
var cx = 250;
var cy = 330;
var scale = 15;
var n = 8192;

function initLorenz() {
    var x, y, z;
    var canvasLorenz = document.createElement("canvas");
    
    canvasLorenz.setAttribute("width", "505px" );
    canvasLorenz.setAttribute("height", "660px" );
    canvasLorenz.setAttribute("style", "display: inline-block; max-width: 100%; max-height: 100%;");
    var divLorenz = document.getElementById('lorenz');
    divLorenz.innerHTML = "";
    divLorenz.appendChild(canvasLorenz);
	
    var x0 = parseFloat(document.getElementById('x0').value);
    var y0 = parseFloat(document.getElementById('y0').value);
    var z0 = parseFloat(document.getElementById('z0').value);

    document.getElementById("var-x0").innerHTML = x0;
    document.getElementById("var-y0").innerHTML = y0;
    document.getElementById("var-z0").innerHTML = z0;

    var a = parseFloat(document.getElementById('a').value);
    var b = parseFloat(document.getElementById('b').value);
    document.getElementById("var-a").innerHTML = a;
    document.getElementById("var-b").innerHTML = b;

    var i = 0;
    var objCanvas = canvasLorenz.getContext('2d');
    var interval = setInterval(function () {
	if (i < n) {
	    x = x0 + h * a * (x0 - y0);
	    y = y0 + h * (-x0 * z0 + b * x0 - y0);
	    z = z0 + h * (x0 * y0 - z0);
	    objCanvas.strokeStyle = "hsl(" + Math.abs(x) * 10 + "," + Math.abs(y) * 10 + "%," + Math.abs(z) * 2 + "%)";
	    objCanvas.beginPath();
	    objCanvas.moveTo(cx + x0 * scale, cy + y0 * scale);
	    objCanvas.lineTo(cx + x * scale, cy + y * scale);
	    objCanvas.stroke();
	    x0 = x;
	    y0 = y;
	    z0 = z;
	    i += 1;
	}
	else {
	    clearInterval(interval);
	}
    });
};
