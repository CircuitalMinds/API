function config_searcher ( app ) {
    app.searcher.query = APP.GetData('query');
    app.searcher.result = APP.GetData('result');
    app.searcher.query_submit = $('input')[0];
    app.searcher.register = '';

    app.searcher.Template = function ( title, image ) {
        var strObj = '<li class="button card-content bg-darkTeal bg-dark-hover fg-light" '
                     + 'onclick=music_app.change_video_from(this.getElementsByClassName("label")[0].textContent) >'
                     + '<img class="avatar" src="' + image + '">'
                     + '<span class="label">'+ title +'</span>'
                     + '<span class="second-label"> 1 min </span>'
                     + '</li>';
        return strObj;
    };

    app.searcher.Filter = function ( query, array_data ) {
        data = {};
        query_data = [];
        for ( var j = 0; j < query.length + 1; j++ ) {data[j] = [];};
        for ( element of array_data ) {
            word = element.toLowerCase();
            target = element.toLowerCase();
            result = app.searcher.WordMatches(word, target);
            data[result].push(element);
        };
        matches = Object.keys(data).sort().reverse();
        for ( m of matches ) {
            if ( data[m].length > 0 ) {for ( r of data[m] ) {query_data.push(r)}};
        };
        return query_data;
    };

    app.searcher.WordMatches = function ( word, target ) {
        matches = 0;
        for ( var i = 0; i < word.length; i++ ) {
            if ( word[i] == target[i] ) {matches += 1} else {break}
        };
        return matches;
    };

    app.searcher.get_query = function ( q ) {
        default_image = app.static.image + "/desktop/julia.gif";
        if ( q != '' & q != undefined & q != null ) {
            query_result = '';
            q = q.toLowerCase()
            if ( app.videos[q[0]] != undefined ) {
                query_data = Object.keys(app.videos[q[0]]);
                filter_data = app.searcher.Filter(q, query_data);
                if ( filter_data.length == 0 ) {
                    query_result += app.searcher.Template('search not found', default_image)
                } else {
                    for ( title of filter_data ) {
                        query_result += app.searcher.Template(title, app.videos[q[0]][title].image)
                    };
                };
            } else {
                query_result += app.searcher.Template('search not found', default_image)
            };
            app.searcher.register = q;
        } else if ( q == '' ) {
            app.searcher.register = q;
        };
        app.searcher.SearchDisplay(app.searcher.register);
    };

    app.searcher.SearchDisplay = function ( data ) {
        if ( data == '' ) {
            app.searcher.result.setAttribute("class", "bg-white");
            app.searcher.result.innerHTML = '';
            app.searcher.result.style['display'] = 'none';
        } else {
            app.searcher.result.setAttribute("class", "bg-darkTeal fg-white");
            txt = '<ul class="feed-list bg-darkTeal fg-light"><li class="title"> Search Result </li>' + data + '</ul>';
            app.searcher.result.innerHTML = txt;
            app.searcher.result.style['display'] = 'block';
        }
    };

    app.searcher.query_submit.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            app.searcher.get_query(app.searcher.query.value);
        }
    });
};