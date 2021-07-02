function setConfig (videoObj, audioObj, apiObj) {
    apiObj.url = "https://circuitalminds.github.io";
    apiObj.url_share = apiObj.url;
    apiObj.url_db = "https://circuitalminds.herokuapp.com/api";
    apiObj.url_previews = apiObj.url + "/music?play_song=";
    apiObj.yt = {get_search: youtubeSearch, downloader: youtubeDownloader};
    apiObj.fb_share = document.getElementsByClassName("cell fb-share-button")[0];
    setPlayerUpdates(videoObj, 'video');
    setPlayerUpdates(audioObj, 'audio');
};              

function setPlayerUpdates (playerObj, mediaType) {          
	playerObj.mediaType = mediaType;
	playerObj.from_list = function ( Id ) { 
		playerObj.current_song.title = playerObj.song_list[Id][mediaType + "_title"];
		playerObj.current_song.url = playerObj.song_list[Id][mediaType + "_url"];
		playerObj.current_song.index = Id;        
		titlePlayers[playerObj.mediaType].innerHTML = playerObj.current_song.title;
		mediaPlayers[playerObj.mediaType].setAttribute('src', playerObj.current_song.url);
		mediaPlayers[playerObj.mediaType].play();
    };
    playerObj.up = function () { 
    	playerObj.from_list( playerObj.current_song.index + 1 );
    };    
    playerObj.back = function () { 
    	playerObj.from_list( playerObj.current_song.index - 1 );
    };
    playerObj.random_song = function () { 
    	playerObj.from_list( Math.round(Math.random() * (playerObj.song_list.length - 1)) );
    };    
};

function youtubeSearch() {
    circuitApi.yt.search_list.innerHTML = '<li><div data-role="progress" data-type="line"></div></li>';
    circuitApi.yt.search_title.value;
    var searchData = $.get(circuitApi.url_db + "/templates", {"video_title": search, "html": "search_list"});
    searchData.done( function( data )  {
           circuitApi.yt.search_list.innerHTML = data;
    });
};

function youtubeDownloader(Id) {
    title = document.getElementById(Id).getElementsByTagName("p")[0].textContent;
    image = document.getElementById(Id).getElementsByTagName("img")[0].src;
    url = document.getElementById(Id).getElementsByTagName("button")[0].value;
    var urlData = $.get(circuitApi.url_db + "/query", {"video_title": title, "video_url": url, "video_image": image, "status": "waiting", "book": "select_songs", "option": "add"});
};

function shareVideo() {
    var el = document.createElement('textarea');
    song = videoPlayer.current_song.title;
    shareURL = circuitApi.url_previews + encodeURI(song);
    el.value = shareURL;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    alert("Link Copied: " + el.value);
    document.body.removeChild(el);
};
