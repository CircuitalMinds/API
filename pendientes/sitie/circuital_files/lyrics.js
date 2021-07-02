let requestURL= 'https://raw.githubusercontent.com/CircuitalMinds/blog/main/js/lyrics.json';
let requestLyrics = new XMLHttpRequest();
requestLyrics.open('GET', requestURL);
requestLyrics.responseType = 'json';
requestLyrics.send();

requestLyrics.onload = function() {
  const jsonLyrics = requestLyrics.response;

  writeLyrics("original-part1", "traduction-part1");
  writeLyrics("original-part2", "traduction-part2");
  writeLyrics("original-part3", "traduction-part3");
  writeLyrics("original-part4", "traduction-part4");
  
  function writeLyrics(keyOriginal, keyTraduction) {
          const textOriginal = jsonLyrics[keyOriginal];  
	  const textTraduction = jsonLyrics[keyTraduction]; 
          var nodeA = "";
  	  var nodeB = "";
	  for (var i=0; i < textOriginal.length; i++) {

	      if (i % 4 == 0) {
		nodeA += "<br>";
		nodeB += "<br>";
		};
	      nodeA += "<span style='height: 26px;'>" + textOriginal[i] + "</spam><br>";
	      nodeB += "<span style='height: 26px;'>" + textTraduction[i] + "</spam><br>";
	      
	      };
	  document.getElementById(keyOriginal).innerHTML = nodeA;
	  document.getElementById(keyTraduction).innerHTML = nodeB;
  }; 
}
