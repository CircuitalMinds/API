function youtubeSearch() {
    searchList.innerHTML = '<li><div data-role="progress" data-type="line"></div></li>';
    search = document.getElementById("yt-search").value;
    var searchData = $.get("https://circuitalminds.herokuapp.com/api/templates", {"video_title": search, "html": "search_list"});
    searchData.done( function( data )  {
           searchList.innerHTML = data;
        });
};

function endSong( option ) {
    if (option == "back") {    
        currentId = currentId - 1;
    } else if (option == "up") {
    	currentId = currentId + 1;
    }    
    fb_share.setAttribute("data-href", url_previews + encodeURI(playList[currentId]['video_title']));
    playMedia.setAttribute("src", playList[currentId]['video_url']);
    currentSong.innerHTML = playList[currentId]['video_title'];    
    playMedia.play();
};

function songFromList( songId ) {
    currentId = songId - 1;
    fb_share.setAttribute("data-href", url_previews + encodeURI(playList[currentId]['video_title']));
    playMedia.setAttribute("src", playList[currentId]['video_url']);
    currentSong.innerHTML = playList[currentId]['video_title'];
    playMedia.play();
};

function endAudioSong( option ) {
    if (option == "back") {    
        audioId = audioId - 1;
    } else if (option == "up") {
    	audioId = audioId + 1;
    }    
    audioMedia.setAttribute("src", audioList[audioId]['audio_url']);
    currentAudio.innerHTML = audioList[audioId]['audio_title'];    
    audioMedia.play();
};

function audioSongFromList( audio_Id ) {
    audioId = audio_Id - 1;
    audioMedia.setAttribute("src", audioList[audioId]['audio_url']);
    currentAudio.innerHTML = audioList[audioId]['audio_title'];
    audioMedia.play();    
};

function youtubeDownloader(Id) {
    title = document.getElementById(Id).getElementsByTagName("p")[0].textContent;
    image = document.getElementById(Id).getElementsByTagName("img")[0].src;
    url = document.getElementById(Id).getElementsByTagName("button")[0].value;
    var urlData = $.get("https://circuitalminds.herokuapp.com/api/query", {"video_title": title, "video_url": url, "video_image": image, "status": "waiting", "book": "select_songs", "option": "add"});
};

function shareVideo() {
    var el = document.createElement('textarea');
    song = playList[currentId]['video_title'];
    shareURL = "https://circuitalminds.github.io/music?play_song=" + encodeURI(song);
    el.value = shareURL;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    alert("Link Copied: " + el.value);
    document.body.removeChild(el);
};
