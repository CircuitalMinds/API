function initCrib() {

    var canvasCrib = document.getElementById("crib");
    var ctxCrib = canvasCrib.getContext("2d");
    var primo = 1;
    var contPn = 0;
    var pin = 1.0;
    var nT = parseInt(document.getElementById("pn").value);
    var sn = canvasCrib.width / 10;
    canvasCrib.height = sn * nT
    var grdA = ctxCrib.createLinearGradient(300, 0, 0, 100);
    ctxCrib.beginPath();
    grdA.addColorStop(0.1, "sienna");
    grdA.addColorStop(0.5, "crimson");
    grdA.addColorStop(0.7, "indianred");
    grdA.addColorStop(1, "royalblue");
    // Draw the initial triangle (black)
    ctxCrib.strokeStyle = grdA;
    ctxCrib.stroke();
    ctxCrib.font = "15px Arial";
    for (var i = 0; i < nT; i += 1) {
        for (var j = 0; j < 10; j += 1) {
            ctxCrib.rect(j * sn, i * sn, sn, sn);
            if (primo == 2 || primo == 3 || primo == 5 || primo == 7) {
                contPn += 1;
                pin *= 1 / (1 - 1 / (primo ** 2));
                ctxCrib.strokeText(primo, j * sn + sn / 4, i * sn + 3 * sn / 4);
            } else if (primo > 1 && primo % 2 !== 0 && primo % 3 !== 0 && primo % 5 !== 0 && primo % 7 !== 0) {
                contPn += 1;
                pin *= 1 / (1 - 1 / (primo ** 2));
                ctxCrib.strokeText(primo, j * sn + sn / 4, i * sn + 3 * sn / 4);
            }
            primo += 1;
        }
    }
    document.getElementById("var-pn").innerHTML = contPn;
    document.getElementById("var-pi").innerHTML = Math.sqrt(6 * pin);
    document.getElementById("var-n").innerHTML = nT * 10;
    ctxCrib.strokeStyle = grdA;
    ctxCrib.stroke();
}
