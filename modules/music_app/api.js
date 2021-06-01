

function getObjectById ( Id ) {
    function getObjs ( objList ) {
        var objs = {};
        for (var i=0; i < objList.length; i++) {
            objs[objList[i]] = document.getElementById(objList[i]);
        };
        return objs;
    };
    var objList = {audio: ['audio-media', 'audio-title'],
                     video: ['video-media', 'video-title'],
                     youtube: ["search-list", "yt-search"]};
    return getObjs(objList[Id]);
};

function youtubeSearch() {
    circuitApi.yt.search_list.innerHTML = '<li><div data-role="progress" data-type="line"></div></li>';
    circuitApi.yt.search_title.value;
    var searchData = $.get(circuitApi.url_db + "/templates", {"video_title": search, "html": "search_list"});
    searchData.done( function( data )  {
       circuitApi.yt.search_list.innerHTML = data;
    });
};

function updateRegister() {
    var data = circuitApi.music_app.register[index];
    if ( data == undefined ) {
        data = circuitApi.music_app.song_list[index];
        data.plays = 1;
        circuitApi.music_app.register[index] = data;
        data.option = "add";
    } else {
        data.plays = data.plays + 1;
        circuitApi.music_app.register[index] = data;
        data.option = "update";
    };
    data.book = "music_views";
    var registerData = $.get("http://127.0.0.1:5100/query/add", data);
    registerData.done( function( info )  {
       console.log(info);
    });
};


function playlistRegister() {
    var data = circuitApi.music_app.register.views[index];
    if ( data == undefined ) {
        data = circuitApi.music_app.song_list[index];
        data.plays = 1;
        circuitApi.music_app.register.views[index] = data;
        data.option = "add";
    } else {
        data.plays = data.plays + 1;
        circuitApi.music_app.register.views[index] = data;
        data.option = "update";
    };
    data.book = "music_views";
    var searchData = $.get(circuitApi.url_db, data);
    searchData.done( function( info )  {
       console.log(info);
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