function initCantor() {
    var canvasCantor = document.createElement("canvas");
    canvasCantor.setAttribute("width", "505px" );
    canvasCantor.setAttribute("height", "660px" );
    canvasCantor.setAttribute("style", "display: inline-block; max-width: 100%; max-height: 100%;");
    var divCantor = document.getElementById("cantor");
    divCantor.innerHTML = "";
    divCantor.appendChild(canvasCantor);
    var fn = parseInt(document.getElementById('fn').value);
    document.getElementById("var-fn").innerHTML = fn;
    var W = canvasCantor.width;
    var H = canvasCantor.height;
    var ctx1 = canvasCantor.getContext("2d");
    var grdA = ctx1.createLinearGradient(300, 0, 0, 100);
    grdA.addColorStop(0.1, "sienna");
    grdA.addColorStop(0.5, "crimson");
    grdA.addColorStop(0.7, "indianred");
    grdA.addColorStop(1, "royalblue");
    var x1 = 10;
    var y1 = 10;
    var len = W - 20;
    var nT = len * (1 / 3) ** fn
    cantor(x1, y1, len, nT);

    function cantor(x1, y1, len, nT) {
        if (len >= nT) {
            ctx1.strokeStyle = grdA;
            ctx1.beginPath();
            ctx1.moveTo(x1, y1);
            ctx1.lineTo(x1 + len, y1);
            ctx1.lineWidth = 5;
            ctx1.stroke();
            y1 += 20;
            cantor(x1, y1, len / 3, nT);
            cantor(x1 + len * 2 / 3, y1, len / 3, nT);
        }
    }
}
