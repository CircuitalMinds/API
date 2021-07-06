var APP = {
    url_data: 'https://raw.githubusercontent.com/CircuitalMinds/video_app/main/video_data.json',
    git_url: "https://circuitalminds.github.io",
    static: {},
    search_engine: {
        register: '',
        result: $('#result')[0],
        query: $('input')[0]
    }
};
["images", "js", "css"].map( i => APP.static[i] = APP.git_url + '/static/' + i );

var videos = [];
var video_data = {};

Player = $("#video-media")[0];
Player.video_title = $('#video-title')[0];
buttons = {
    "previous": $("#previous")[0],
    "next": $("#next")[0],
    "play": $("#play")[0],
    "pause": $("#pause")[0],
    "minus": $("#minus")[0],
    "plus": $("#plus")[0]
};
buttons.previous.onclick = function () { Player.previous_video() };
buttons.next.onclick = function () { Player.next_video() };
buttons.play.onclick = function () { Player.onplay() };
buttons.pause.onclick = function () { Player.onpause() };
buttons.minus.onclick = function () { Player.set_volume('-') };
buttons.plus.onclick = function () { Player.set_volume('+') };

Player.set_video = function ( index ) {
    title = videos[index];
    this.video_title.innerHTML = title;
    this.src = video_data[title].url;
    this.onplay();
};
Player.onplay = function () {
    this.play()
};
Player.onpause = function () {
    this.pause()
};
Player.previous_video = function () {
    if ( this.video_title == '' ) {
      this.set_video(this.random_video());
    } else {
        index = videos.indexOf(this.video_title.textContent);
        if ( index > 0 ) {
            this.set_video(index - 1);
        } else {
            this.set_video(this.random_video());
        };
    };
};
Player.next_video = function () {
    if ( this.video_title == '' ) {
      this.set_video(this.random_video());
    } else {
        index = videos.indexOf(this.video_title.textContent);
        if ( index > 0 ) {
            this.set_video(index + 1);
        } else {
            this.set_video(this.random_video());
        };
    };
};
Player.random_video = function () {
    return Math.round(Math.random() * videos.length  - 1);
}

Player.set_volume = function ( option ) {
    if ( option == '+' & this.volume != 1 ) {
        this.volume += 0.1;
    } else if ( option == '-' & this.volume != 0 ) {
        this.volume -= 0.1;
    };
};



function set_video_data ( dataset ) {
  	video_list = Object.values(dataset);
    for ( video of video_list ) {
        video_title = video.title;
        videos.push(video_title);
        video_data[video_title] = {};
        for ( key of Object.keys(video) ) {
            if ( key != 'title' ) {
        	    video_data[video_title][key] = video[key];
            };
        };
    };
};

function get_request_videos () {
    var url = APP.url_data;
    var request = new XMLHttpRequest();
    request.open('GET', url);
    request.responseType = 'json';
    request.send();
    request.onload = function() {
        var data = request.response;
      	set_video_data(data);
    };
};

function SearchTemplate ( data ) {
    data_list = '<ul class="feed-list bg-darkTeal fg-light">'
                + '<li class="title"> Search Result </li>';
    function set_row ( title ) {
        return '<li class="button card-content bg-darkTeal bg-dark-hover fg-light" '
               + 'onclick=Player.set_video(INDEX); >'.replace('INDEX', videos.indexOf(title))
               + '<img class="avatar" src="IMAGE" >'.replace('IMAGE', data[title].image)
               + '<span id="title" class="label">' + title + '</span>'
               + '<span class="second-label">' + data[title].duration + '</span>'
               + '</li>';
    };
    Object.keys(data).map( name => data_list += set_row(name) );
    data_list += '</ul>';
    return data_list;
}

function SearchResult ( data ) {
        if ( data == '' ) {
            this.result.setAttribute("class", "bg-white");
            this.result.innerHTML = '';
            this.result.style['display'] = 'none';
        } else {
            this.result.setAttribute("class", "bg-darkTeal fg-white");
            this.result.innerHTML = data;
            this.result.style['display'] = 'block';
        }
    };

APP.search_engine.query.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            get_result(this.value);
        }
    });

function get_result ( query ) {
    if ( query == '' ) {
        SearchResult(query);
    } else {
        matches = videos.filter( video => video.toLowerCase().match(query.toLowerCase()) != null );
        matches.sort();
        data = {};
        matches.map( title => data[title] = video_data[title] );
        SearchResult(SearchTemplate(data));
    };
};

$( document ).ready(function() {
    get_request_videos();
    Player.poster = APP.static.images + "/desktop/julia.gif";
});
