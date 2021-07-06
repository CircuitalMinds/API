var Manager = {
    url: "https://circuitalminds.github.io"
};

function Templates ( index, title, image ) {
    var strObj = '<li class="button card-content bg-darkTeal bg-dark-hover fg-light" '
                 + 'onclick=APP.set_video_from_list(INDEX); >'
                 + '<img class="avatar" src="IMAGE">'
                 + '<span id="title" class="label">TITLE</span>'
                 + '<span class="second-label"> 1 min </span>'
                 + '</li>';
    return strObj;
};


function RequestObject ( url ) {
    var object_data = {
        request_url: url,
        response_type: 'json',
        response_data: null
    };
    return object_data;
};

function ManagerRequest ( request_data ) {
    var url = request_data.url;
    var request = new XMLHttpRequest();
    request.open('GET', url);
    request.responseType = request_data.response_type;
    request.send();
    request.onload = function() {
        var data = request.response;
        request_data.response_data = data;
};
