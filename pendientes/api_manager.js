var query_data = {
    books: {
        user_register: {arguments: ["username", "password"]},
        blog: {arguments: ["title", "date", "content", "picture"]},
        jupyter_app: {arguments: ["title", "topic", "module", "location", "resources"]},
        music_app: {arguments: ["video_url", "video_title", "video_image"]}
        },
    API: 'https://circuitalminds.herokuapp.com/get'
};

function get_requests ( book, option, data_requests ) {
    url = query_data.API + '/' book + '/' + option;
    var getQuery = $.get( url, data_requests );
    getQuery.done( function ( data ) {
        console.log(data);
    });
};



function check_requests ( book, option, data_requests ) {
    args = query_data.books[book].arguments;
    args_check = Object.keys(data_requests);
    for ( arg of args ) {
        if ( args_check.indexOf(arg) == -1 ) {
            return {Response: 'bad request'}
        };
    };
    return get_requests(book, option, data_requests);
};

