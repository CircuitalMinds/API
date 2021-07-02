$( function () {
    var Criba = document.getElementById("criba");
    var ctxCriba = Criba.getContext("2d");
    var primo = 1;
    var nT = 10;
    var contPn = 0;
    var pin = 1.0;
    var sn = Criba.width / 10;
    Criba.height = sn * nT
    var grdA = ctxCriba.createLinearGradient(300, 0, 0, 100);
    ctxCriba.beginPath();
    grdA.addColorStop(0.1, "sienna");
    grdA.addColorStop(0.3, "crimson");
    grdA.addColorStop(0.6, "indianred");
    grdA.addColorStop(1, "royalblue");
    // Draw the initial triangle (black)
    ctxCriba.strokeStyle = grdA;
    ctxCriba.stroke();
    ctxCriba.font = "15px Arial";
    for (var i = 0; i < nT; i += 1) {
        for (var j = 0; j < 10; j += 1) {
            ctxCriba.rect(j * sn, i * sn, sn, sn);
            if (primo == 2 || primo == 3 || primo == 5 || primo == 7) {
                contPn += 1;
                pin *= 1 / (1 - 1 / (primo ** 2));
                ctxCriba.strokeText(primo, j * sn + sn / 4, i * sn + 3 * sn / 4);
            } else if (primo > 1 && primo % 2 !== 0 && primo % 3 !== 0 && primo % 5 !== 0 && primo % 7 !== 0) {
                contPn += 1;
                pin *= 1 / (1 - 1 / (primo ** 2));
                ctxCriba.strokeText(primo, j * sn + sn / 4, i * sn + 3 * sn / 4);
            }
            primo += 1;
        }
    }
    ctxCriba.strokeStyle = grdA;
    ctxCriba.stroke();

});
