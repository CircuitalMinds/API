function print ( data ) {
    console.log(
        JSON.stringify( data )
    );
};
let Http = {};
Http.get = function ( Url, Handler=Print ) {
    $.getJSON(
        Url, (data) => setTimeout( () => Handler(data), 200 )
    );
};
Http.post = function ( Url, Data, Handler=Print ) {
    $.post(
        Url, Data, (data) => setTimeout( () => Handler(data), 200 )
    );
};