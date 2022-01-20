function Dict ( data ) {
    let Obj = new Object();
    if ( data != undefined ) {
        Obj.data = data;
    } else {
        Obj.data = {};
    };
    Obj.keys = function () {
        return Object.keys(this.data);
    };
    Obj.values = function () {
        return Object.values(this.data);
    };
    Obj.get = function ( key ) {
        return this.data[key];
    };
    Obj.setattr = function ( key, value ) {
        this.data[key] = value;
    };
    Obj.len = function () {
        return Object.keys(this.data).length;
    };
    Obj.items = function () {
        return Object.entries(this.data);
    };
    Obj.pop = function ( key ) {
        delete this.data[key];
    };
    return Obj;
};

let taskObj = new Object();
taskObj.Data = {
    site_url: "https://circuitalminds.github.io",
    api_url: "https://circuitalminds.herokuapp.com"
};
var Api = new Object();
Api.responses = {
    data: [],
    scheme: function ( url, datatype="json" ) {
        var obj = {request: url, response: ( datatype == "json" ) ? {} : "" };
        return obj;
    }
};

Api.call = function ( method, query, params={} ) {
    isMethod = ( method != undefined ) ? this.Data.methods.indexOf(method) : false;
    isQuery = ( query != undefined ) ? this.Data.books.indexOf(query) : false;
    isQuery = ( query != undefined ) ? this.Data.resources.indexOf(query) : false;
    if ( isMethod || isQuery ) {
        url = [this.Data.url, method, query].join("/");
        if ( Object.keys(params).length > 0 ) {
            url += "?" + Object.keys(params).map( x => x + "=" + params[x] ).join("&");
        };
        obj = this.responses.scheme(url);
        $.get(url).done(function (data) {
            console.log(data);
            obj.response = data;
            this.responses.data.push(obj);
        });
    } else {
        return {response: "request invalid"};
    };
};

Api.getGeolocation = function() {
    if ( navigator.geolocation ) {
        navigator.geolocation.watchPosition(
            function ( position ) {
                ["latitude", "longitude"].map(
                    console.log(position.coords[k])
                );
            }
        );
    };
    console.log(this.Data.geolocation);
};

taskObj.initWorker = function( workerObj ) {
    console.log("start");
    var Interval = setInterval( function() {
        if ( workerObj["status"] ) {
            workerObj.init();
        } else {
            console.log("ok");
            clearInterval(Interval);
        };
    }, workerObj["timer"]);
    return
};

var alarm = {
  remind: function(aMessage) {
    alert(aMessage);
    delete this.timeoutID;
  },

  setup: function() {
    this.cancel();
    var self = this;
    this.timeoutID = window.setTimeout(function(msg) {self.remind(msg);}, 1000, "Wake up!");
  },

  cancel: function() {
    if(typeof this.timeoutID == "number") {
      window.clearTimeout(this.timeoutID);
      delete this.timeoutID;
    }
  }
};
window.onclick = function() { alarm.setup() };
