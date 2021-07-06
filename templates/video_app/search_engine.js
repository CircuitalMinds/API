var search_engine = {
    register: '',
    result: $('#result')[0],
    query: $('input')[0],
};


search_engine.Template = function ( data ) {
    data_list = '<ul class="feed-list bg-darkTeal fg-light">'
                + '<li class="title"> Search Result </li>';
    function set_row ( data_i ) {
        return '<li class="button card-content bg-darkTeal bg-dark-hover fg-light" '
               + 'onclick="' + data_i.index + '"; >'
               + '<img class="avatar" src="' + data_i.image + '">'
               + '<span id="title" class="label">' + data_i.title + '</span>'
               + '<span class="second-label">' + data_i.duration + '</span>'
               + '</li>';
    };
    data.map( row => data_list += set_row(row) );
    data_list += '</ul>';
    return data_list;
}

search_engine.Display = function ( data ) {
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

search_engine.query.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            search_engine.get_result(this.value);
        }
    });

search_engine.get_result = function ( query ) {
    matches = [];
    for ( target of targets ) {
        x = target.toLowerCase();
        if ( x.match(query) != null ) {matches.push(target)};
    };
    return matches;
};
