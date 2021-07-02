(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
'use strict';var m;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var ca="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
function da(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var ea=da(this);function t(a,b){if(b)a:{var c=ea;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&ca(c,a,{configurable:!0,writable:!0,value:b})}}
t("Symbol",function(a){function b(e){if(this instanceof b)throw new TypeError("Symbol is not a constructor");return new c("jscomp_symbol_"+(e||"")+"_"+d++,e)}
function c(e,f){this.h=e;ca(this,"description",{configurable:!0,writable:!0,value:f})}
if(a)return a;c.prototype.toString=function(){return this.h};
var d=0;return b});
t("Symbol.iterator",function(a){if(a)return a;a=Symbol("Symbol.iterator");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=ea[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&ca(d.prototype,a,{configurable:!0,writable:!0,value:function(){return fa(aa(this))}})}return a});
function fa(a){a={next:a};a[Symbol.iterator]=function(){return this};
return a}
function u(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:aa(a)}}
function ha(a){for(var b,c=[];!(b=a.next()).done;)c.push(b.value);return c}
var ia="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ja=function(){function a(){function c(){}
new c;Reflect.construct(c,[],function(){});
return new c instanceof c}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(c,d,e){c=b(c,d);e&&Reflect.setPrototypeOf(c,e.prototype);return c}}return function(c,d,e){void 0===e&&(e=c);
e=ia(e.prototype||Object.prototype);return Function.prototype.apply.call(c,e,d)||e}}(),ka;
if("function"==typeof Object.setPrototypeOf)ka=Object.setPrototypeOf;else{var la;a:{var ma={a:!0},na={};try{na.__proto__=ma;la=na.a;break a}catch(a){}la=!1}ka=la?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var pa=ka;
function v(a,b){a.prototype=ia(b.prototype);a.prototype.constructor=a;if(pa)pa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.M=b.prototype}
function qa(){this.o=!1;this.l=null;this.i=void 0;this.h=1;this.u=this.m=0;this.C=this.j=null}
function ra(a){if(a.o)throw new TypeError("Generator is already running");a.o=!0}
qa.prototype.B=function(a){this.i=a};
function sa(a,b){a.j={Aa:b,Ba:!0};a.h=a.m||a.u}
qa.prototype.return=function(a){this.j={return:a};this.h=this.u};
function w(a,b,c){a.h=c;return{value:b}}
qa.prototype.A=function(a){this.h=a};
function ta(a,b,c){a.m=b;void 0!=c&&(a.u=c)}
function ua(a){a.m=0;var b=a.j.Aa;a.j=null;return b}
function va(a){a.C=[a.j];a.m=0;a.u=0}
function wa(a){var b=a.C.splice(0)[0];(b=a.j=a.j||b)?b.Ba?a.h=a.m||a.u:void 0!=b.A&&a.u<b.A?(a.h=b.A,a.j=null):a.h=a.u:a.h=0}
function xa(a){this.h=new qa;this.i=a}
function ya(a,b){ra(a.h);var c=a.h.l;if(c)return za(a,"return"in c?c["return"]:function(d){return{value:d,done:!0}},b,a.h.return);
a.h.return(b);return Aa(a)}
function za(a,b,c,d){try{var e=b.call(a.h.l,c);if(!(e instanceof Object))throw new TypeError("Iterator result "+e+" is not an object");if(!e.done)return a.h.o=!1,e;var f=e.value}catch(g){return a.h.l=null,sa(a.h,g),Aa(a)}a.h.l=null;d.call(a.h,f);return Aa(a)}
function Aa(a){for(;a.h.h;)try{var b=a.i(a.h);if(b)return a.h.o=!1,{value:b.value,done:!1}}catch(c){a.h.i=void 0,sa(a.h,c)}a.h.o=!1;if(a.h.j){b=a.h.j;a.h.j=null;if(b.Ba)throw b.Aa;return{value:b.return,done:!0}}return{value:void 0,done:!0}}
function Ba(a){this.next=function(b){ra(a.h);a.h.l?b=za(a,a.h.l.next,b,a.h.B):(a.h.B(b),b=Aa(a));return b};
this.throw=function(b){ra(a.h);a.h.l?b=za(a,a.h.l["throw"],b,a.h.B):(sa(a.h,b),b=Aa(a));return b};
this.return=function(b){return ya(a,b)};
this[Symbol.iterator]=function(){return this}}
function x(a,b){b=new Ba(new xa(b));pa&&a.prototype&&pa(b,a.prototype);return b}
t("Reflect",function(a){return a?a:{}});
t("Reflect.construct",function(){return ja});
t("Reflect.setPrototypeOf",function(a){return a?a:pa?function(b,c){try{return pa(b,c),!0}catch(d){return!1}}:null});
function Ca(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
t("String.prototype.endsWith",function(a){return a?a:function(b,c){var d=Ca(this,b,"endsWith");b+="";void 0===c&&(c=d.length);c=Math.max(0,Math.min(c|0,d.length));for(var e=b.length;0<e&&0<c;)if(d[--c]!=b[--e])return!1;return 0>=e}});
t("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=Ca(this,b,"startsWith");b+="";var e=d.length,f=b.length;c=Math.max(0,Math.min(c|0,d.length));for(var g=0;g<f&&c<e;)if(d[c++]!=b[g++])return!1;return g>=f}});
t("Object.setPrototypeOf",function(a){return a||pa});
function Da(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
var Ea="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)Da(d,e)&&(a[e]=d[e])}return a};
t("Object.assign",function(a){return a||Ea});
t("Promise",function(a){function b(g){this.h=0;this.j=void 0;this.i=[];this.o=!1;var h=this.l();try{g(h.resolve,h.reject)}catch(k){h.reject(k)}}
function c(){this.h=null}
function d(g){return g instanceof b?g:new b(function(h){h(g)})}
if(a)return a;c.prototype.i=function(g){if(null==this.h){this.h=[];var h=this;this.j(function(){h.u()})}this.h.push(g)};
var e=ea.setTimeout;c.prototype.j=function(g){e(g,0)};
c.prototype.u=function(){for(;this.h&&this.h.length;){var g=this.h;this.h=[];for(var h=0;h<g.length;++h){var k=g[h];g[h]=null;try{k()}catch(l){this.l(l)}}}this.h=null};
c.prototype.l=function(g){this.j(function(){throw g;})};
b.prototype.l=function(){function g(l){return function(p){k||(k=!0,l.call(h,p))}}
var h=this,k=!1;return{resolve:g(this.K),reject:g(this.u)}};
b.prototype.K=function(g){if(g===this)this.u(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.N(g);else{a:switch(typeof g){case "object":var h=null!=g;break a;case "function":h=!0;break a;default:h=!1}h?this.J(g):this.m(g)}};
b.prototype.J=function(g){var h=void 0;try{h=g.then}catch(k){this.u(k);return}"function"==typeof h?this.X(h,g):this.m(g)};
b.prototype.u=function(g){this.B(2,g)};
b.prototype.m=function(g){this.B(1,g)};
b.prototype.B=function(g,h){if(0!=this.h)throw Error("Cannot settle("+g+", "+h+"): Promise already settled in state"+this.h);this.h=g;this.j=h;2===this.h&&this.L();this.C()};
b.prototype.L=function(){var g=this;e(function(){if(g.F()){var h=ea.console;"undefined"!==typeof h&&h.error(g.j)}},1)};
b.prototype.F=function(){if(this.o)return!1;var g=ea.CustomEvent,h=ea.Event,k=ea.dispatchEvent;if("undefined"===typeof k)return!0;"function"===typeof g?g=new g("unhandledrejection",{cancelable:!0}):"function"===typeof h?g=new h("unhandledrejection",{cancelable:!0}):(g=ea.document.createEvent("CustomEvent"),g.initCustomEvent("unhandledrejection",!1,!0,g));g.promise=this;g.reason=this.j;return k(g)};
b.prototype.C=function(){if(null!=this.i){for(var g=0;g<this.i.length;++g)f.i(this.i[g]);this.i=null}};
var f=new c;b.prototype.N=function(g){var h=this.l();g.fa(h.resolve,h.reject)};
b.prototype.X=function(g,h){var k=this.l();try{g.call(h,k.resolve,k.reject)}catch(l){k.reject(l)}};
b.prototype.then=function(g,h){function k(r,q){return"function"==typeof r?function(E){try{l(r(E))}catch(I){p(I)}}:q}
var l,p,n=new b(function(r,q){l=r;p=q});
this.fa(k(g,l),k(h,p));return n};
b.prototype.catch=function(g){return this.then(void 0,g)};
b.prototype.fa=function(g,h){function k(){switch(l.h){case 1:g(l.j);break;case 2:h(l.j);break;default:throw Error("Unexpected state: "+l.h);}}
var l=this;null==this.i?f.i(k):this.i.push(k);this.o=!0};
b.resolve=d;b.reject=function(g){return new b(function(h,k){k(g)})};
b.race=function(g){return new b(function(h,k){for(var l=u(g),p=l.next();!p.done;p=l.next())d(p.value).fa(h,k)})};
b.all=function(g){var h=u(g),k=h.next();return k.done?d([]):new b(function(l,p){function n(E){return function(I){r[E]=I;q--;0==q&&l(r)}}
var r=[],q=0;do r.push(void 0),q++,d(k.value).fa(n(r.length-1),p),k=h.next();while(!k.done)})};
return b});
t("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});
t("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var e=d.length;c=c||0;for(0>c&&(c=Math.max(c+e,0));c<e;c++){var f=d[c];if(f===b||Object.is(f,b))return!0}return!1}});
t("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==Ca(this,b,"includes").indexOf(b,c||0)}});
t("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)Da(b,d)&&c.push([d,b[d]]);return c}});
t("WeakMap",function(a){function b(k){this.h=(h+=Math.random()+1).toString();if(k){k=u(k);for(var l;!(l=k.next()).done;)l=l.value,this.set(l[0],l[1])}}
function c(){}
function d(k){var l=typeof k;return"object"===l&&null!==k||"function"===l}
function e(k){if(!Da(k,g)){var l=new c;ca(k,g,{value:l})}}
function f(k){var l=Object[k];l&&(Object[k]=function(p){if(p instanceof c)return p;Object.isExtensible(p)&&e(p);return l(p)})}
if(function(){if(!a||!Object.seal)return!1;try{var k=Object.seal({}),l=Object.seal({}),p=new a([[k,2],[l,3]]);if(2!=p.get(k)||3!=p.get(l))return!1;p.delete(k);p.set(l,4);return!p.has(k)&&4==p.get(l)}catch(n){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();f("freeze");f("preventExtensions");f("seal");var h=0;b.prototype.set=function(k,l){if(!d(k))throw Error("Invalid WeakMap key");e(k);if(!Da(k,g))throw Error("WeakMap key fail: "+k);k[g][this.h]=l;return this};
b.prototype.get=function(k){return d(k)&&Da(k,g)?k[g][this.h]:void 0};
b.prototype.has=function(k){return d(k)&&Da(k,g)&&Da(k[g],this.h)};
b.prototype.delete=function(k){return d(k)&&Da(k,g)&&Da(k[g],this.h)?delete k[g][this.h]:!1};
return b});
t("Map",function(a){function b(){var h={};return h.previous=h.next=h.head=h}
function c(h,k){var l=h.h;return fa(function(){if(l){for(;l.head!=h.h;)l=l.previous;for(;l.next!=l.head;)return l=l.next,{done:!1,value:k(l)};l=null}return{done:!0,value:void 0}})}
function d(h,k){var l=k&&typeof k;"object"==l||"function"==l?f.has(k)?l=f.get(k):(l=""+ ++g,f.set(k,l)):l="p_"+k;var p=h.i[l];if(p&&Da(h.i,l))for(h=0;h<p.length;h++){var n=p[h];if(k!==k&&n.key!==n.key||k===n.key)return{id:l,list:p,index:h,H:n}}return{id:l,list:p,index:-1,H:void 0}}
function e(h){this.i={};this.h=b();this.size=0;if(h){h=u(h);for(var k;!(k=h.next()).done;)k=k.value,this.set(k[0],k[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),k=new a(u([[h,"s"]]));if("s"!=k.get(h)||1!=k.size||k.get({x:4})||k.set({x:4},"t")!=k||2!=k.size)return!1;var l=k.entries(),p=l.next();if(p.done||p.value[0]!=h||"s"!=p.value[1])return!1;p=l.next();return p.done||4!=p.value[0].x||"t"!=p.value[1]||!l.next().done?!1:!0}catch(n){return!1}}())return a;
var f=new WeakMap;e.prototype.set=function(h,k){h=0===h?0:h;var l=d(this,h);l.list||(l.list=this.i[l.id]=[]);l.H?l.H.value=k:(l.H={next:this.h,previous:this.h.previous,head:this.h,key:h,value:k},l.list.push(l.H),this.h.previous.next=l.H,this.h.previous=l.H,this.size++);return this};
e.prototype.delete=function(h){h=d(this,h);return h.H&&h.list?(h.list.splice(h.index,1),h.list.length||delete this.i[h.id],h.H.previous.next=h.H.next,h.H.next.previous=h.H.previous,h.H.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this.i={};this.h=this.h.previous=b();this.size=0};
e.prototype.has=function(h){return!!d(this,h).H};
e.prototype.get=function(h){return(h=d(this,h).H)&&h.value};
e.prototype.entries=function(){return c(this,function(h){return[h.key,h.value]})};
e.prototype.keys=function(){return c(this,function(h){return h.key})};
e.prototype.values=function(){return c(this,function(h){return h.value})};
e.prototype.forEach=function(h,k){for(var l=this.entries(),p;!(p=l.next()).done;)p=p.value,h.call(k,p[1],p[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
t("Set",function(a){function b(c){this.h=new Map;if(c){c=u(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.h.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(u([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
b.prototype.add=function(c){c=0===c?0:c;this.h.set(c,c);this.size=this.h.size;return this};
b.prototype.delete=function(c){c=this.h.delete(c);this.size=this.h.size;return c};
b.prototype.clear=function(){this.h.clear();this.size=0};
b.prototype.has=function(c){return this.h.has(c)};
b.prototype.entries=function(){return this.h.entries()};
b.prototype.values=function(){return this.h.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.h.forEach(function(f){return c.call(d,f,f,e)})};
return b});
function Fa(a,b){a instanceof String&&(a+="");var c=0,d=!1,e={next:function(){if(!d&&c<a.length){var f=c++;return{value:b(f,a[f]),done:!1}}d=!0;return{done:!0,value:void 0}}};
e[Symbol.iterator]=function(){return e};
return e}
t("Array.prototype.entries",function(a){return a?a:function(){return Fa(this,function(b,c){return[b,c]})}});
t("Array.prototype.keys",function(a){return a?a:function(){return Fa(this,function(b){return b})}});
t("Array.prototype.values",function(a){return a?a:function(){return Fa(this,function(b,c){return c})}});
t("Number.isNaN",function(a){return a?a:function(b){return"number"===typeof b&&isNaN(b)}});
t("Number.MAX_SAFE_INTEGER",function(){return 9007199254740991});
t("Object.values",function(a){return a?a:function(b){var c=[],d;for(d in b)Da(b,d)&&c.push(b[d]);return c}});
var y=this||self;function z(a,b,c){a=a.split(".");c=c||y;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
function A(a,b){a=a.split(".");b=b||y;for(var c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function Ga(){}
function Ha(a){a.qa=void 0;a.getInstance=function(){return a.qa?a.qa:a.qa=new a}}
function Ia(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"}
function Ja(a){var b=Ia(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function Ka(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function La(a){return Object.prototype.hasOwnProperty.call(a,Ma)&&a[Ma]||(a[Ma]=++Na)}
var Ma="closure_uid_"+(1E9*Math.random()>>>0),Na=0;function Oa(a,b,c){return a.call.apply(a.bind,arguments)}
function Pa(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function B(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?B=Oa:B=Pa;return B.apply(null,arguments)}
function Qa(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}}
function Ra(a,b){z(a,b,void 0)}
function C(a,b){function c(){}
c.prototype=b.prototype;a.M=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.Kk=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}}
function Sa(a){return a}
;function Ta(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,Ta);else{var c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b&&(this.La=b)}
C(Ta,Error);Ta.prototype.name="CustomError";function Ua(a){a=a.url;var b=/[?&]dsh=1(&|$)/.test(a);this.j=!b&&/[?&]ae=1(&|$)/.test(a);this.l=!b&&/[?&]ae=2(&|$)/.test(a);if((this.h=/[?&]adurl=([^&]*)/.exec(a))&&this.h[1]){try{var c=decodeURIComponent(this.h[1])}catch(d){c=null}this.i=c}}
;function Va(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;var Wa=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},D=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},Xa=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f="string"===typeof a?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},Ya=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e="string"===typeof a?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},Za=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;
D(a,function(e,f){d=b.call(void 0,d,e,f,a)});
return d};
function $a(a,b){a:{for(var c=a.length,d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){b=e;break a}b=-1}return 0>b?null:"string"===typeof a?a.charAt(b):a[b]}
function ab(a,b){b=Wa(a,b);var c;(c=0<=b)&&Array.prototype.splice.call(a,b,1);return c}
function bb(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function cb(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(Ja(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;function db(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function eb(a){var b=fb,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function gb(a){for(var b in a)return!1;return!0}
function hb(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function ib(){var a=F("PLAYER_VARS",{});return null!==a&&"privembed"in a?a.privembed:!1}
function jb(a,b){for(var c in a)if(!(c in b)||a[c]!==b[c])return!1;for(var d in b)if(!(d in a))return!1;return!0}
function kb(a){var b={},c;for(c in a)b[c]=a[c];return b}
function mb(a){if(!a||"object"!==typeof a)return a;if("function"===typeof a.clone)return a.clone();var b=Array.isArray(a)?[]:"function"!==typeof ArrayBuffer||"function"!==typeof ArrayBuffer.isView||!ArrayBuffer.isView(a)||a instanceof DataView?{}:new a.constructor(a.length),c;for(c in a)b[c]=mb(a[c]);return b}
var nb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function ob(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<nb.length;f++)c=nb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var pb;function qb(){if(void 0===pb){var a=null,b=y.trustedTypes;if(b&&b.createPolicy){try{a=b.createPolicy("goog#html",{createHTML:Sa,createScript:Sa,createScriptURL:Sa})}catch(c){y.console&&y.console.error(c.message)}pb=a}else pb=a}return pb}
;function rb(a,b){this.h=b===sb?a:""}
m=rb.prototype;m.Z=!0;m.Y=function(){return this.h.toString()};
m.oa=!0;m.la=function(){return 1};
m.toString=function(){return this.h+""};
function tb(a){if(a instanceof rb&&a.constructor===rb)return a.h;Ia(a);return"type_error:TrustedResourceUrl"}
var sb={};var ub=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};
function vb(a,b){if(b)a=a.replace(wb,"&amp;").replace(xb,"&lt;").replace(yb,"&gt;").replace(zb,"&quot;").replace(Ab,"&#39;").replace(Bb,"&#0;");else{if(!Cb.test(a))return a;-1!=a.indexOf("&")&&(a=a.replace(wb,"&amp;"));-1!=a.indexOf("<")&&(a=a.replace(xb,"&lt;"));-1!=a.indexOf(">")&&(a=a.replace(yb,"&gt;"));-1!=a.indexOf('"')&&(a=a.replace(zb,"&quot;"));-1!=a.indexOf("'")&&(a=a.replace(Ab,"&#39;"));-1!=a.indexOf("\x00")&&(a=a.replace(Bb,"&#0;"))}return a}
var wb=/&/g,xb=/</g,yb=/>/g,zb=/"/g,Ab=/'/g,Bb=/\x00/g,Cb=/[\x00&<>"']/;function Db(a,b){this.h=b===Eb?a:""}
m=Db.prototype;m.Z=!0;m.Y=function(){return this.h.toString()};
m.oa=!0;m.la=function(){return 1};
m.toString=function(){return this.h.toString()};
function Fb(a){if(a instanceof Db&&a.constructor===Db)return a.h;Ia(a);return"type_error:SafeUrl"}
var Gb=/^(?:audio\/(?:3gpp2|3gpp|aac|L16|midi|mp3|mp4|mpeg|oga|ogg|opus|x-m4a|x-matroska|x-wav|wav|webm)|font\/\w+|image\/(?:bmp|gif|jpeg|jpg|png|tiff|webp|x-icon)|video\/(?:mpeg|mp4|ogg|webm|quicktime|x-matroska))(?:;\w+=(?:\w+|"[\w;,= ]+"))*$/i,Hb=/^data:(.*);base64,[a-z0-9+\/]+=*$/i,Ib=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;function Jb(a){if(a instanceof Db)return a;a="object"==typeof a&&a.Z?a.Y():String(a);Ib.test(a)||(a="about:invalid#zClosurez");return new Db(a,Eb)}
var Eb={},Kb=new Db("about:invalid#zClosurez",Eb);var Lb;a:{var Mb=y.navigator;if(Mb){var Nb=Mb.userAgent;if(Nb){Lb=Nb;break a}}Lb=""}function G(a){return-1!=Lb.indexOf(a)}
;function Ob(a,b,c){this.h=c===Pb?a:"";this.i=b}
m=Ob.prototype;m.oa=!0;m.la=function(){return this.i};
m.Z=!0;m.Y=function(){return this.h.toString()};
m.toString=function(){return this.h.toString()};
var Pb={};function Qb(a,b){var c=qb();a=c?c.createHTML(a):a;return new Ob(a,b,Pb)}
;function Rb(a,b){b=b instanceof Db?b:Jb(b);a.href=Fb(b)}
function Sb(a,b){a.rel="stylesheet";a.href=tb(b).toString();(b=a.ownerDocument&&a.ownerDocument.defaultView)&&b!=y?b=Tb(b.document,"style"):(null===Ub&&(Ub=Tb(y.document,"style")),b=Ub);b&&a.setAttribute("nonce",b)}
function Vb(a,b){a.src=tb(b);(b=Wb(a.ownerDocument&&a.ownerDocument.defaultView))&&a.setAttribute("nonce",b)}
function Wb(a){if(a&&a!=y)return Tb(a.document,"script");null===Xb&&(Xb=Tb(y.document,"script"));return Xb}
var Xb=null,Ub=null,Yb=/^[\w+/_-]+[=]{0,2}$/;function Tb(a,b){if(!a.querySelector)return"";var c=a.querySelector(b+"[nonce]");c||"style"!=b||(c=a.querySelector('link[rel="stylesheet"][nonce]'));return c&&(a=c.nonce||c.getAttribute("nonce"))&&Yb.test(a)?a:""}
;function Zb(a){return a=vb(a,void 0)}
function $b(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var ac=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^\\/?#]*)@)?([^\\/?#]*?)(?::([0-9]+))?(?=[\\/?#]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function bc(a){return a?decodeURI(a):a}
function cc(a){return bc(a.match(ac)[3]||null)}
function dc(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)dc(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function ec(a){var b=[],c;for(c in a)dc(c,a[c],b);return b.join("&")}
function fc(a,b){b=ec(b);if(b){var c=a.indexOf("#");0>c&&(c=a.length);var d=a.indexOf("?");if(0>d||d>c){d=c;var e=""}else e=a.substring(d+1,c);a=[a.substr(0,d),e,a.substr(c)];c=a[1];a[1]=b?c?c+"&"+b:b:c;b=a[0]+(a[1]?"?"+a[1]:"")+a[2]}else b=a;return b}
var gc=/#|$/;function H(a,b){var c=void 0;return new (c||(c=Promise))(function(d,e){function f(k){try{h(b.next(k))}catch(l){e(l)}}
function g(k){try{h(b["throw"](k))}catch(l){e(l)}}
function h(k){k.done?d(k.value):(new c(function(l){l(k.value)})).then(f,g)}
h((b=b.apply(a,void 0)).next())})}
;function hc(){return G("iPhone")&&!G("iPod")&&!G("iPad")}
;function ic(a){ic[" "](a);return a}
ic[" "]=Ga;var jc=G("Opera"),kc=G("Trident")||G("MSIE"),lc=G("Edge"),mc=G("Gecko")&&!(-1!=Lb.toLowerCase().indexOf("webkit")&&!G("Edge"))&&!(G("Trident")||G("MSIE"))&&!G("Edge"),nc=-1!=Lb.toLowerCase().indexOf("webkit")&&!G("Edge");function oc(){var a=y.document;return a?a.documentMode:void 0}
var pc;a:{var qc="",rc=function(){var a=Lb;if(mc)return/rv:([^\);]+)(\)|;)/.exec(a);if(lc)return/Edge\/([\d\.]+)/.exec(a);if(kc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(nc)return/WebKit\/(\S+)/.exec(a);if(jc)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
rc&&(qc=rc?rc[1]:"");if(kc){var sc=oc();if(null!=sc&&sc>parseFloat(qc)){pc=String(sc);break a}}pc=qc}var tc=pc,uc;if(y.document&&kc){var vc=oc();uc=vc?vc:parseInt(tc,10)||void 0}else uc=void 0;var wc=uc;var xc=hc()||G("iPod"),yc=G("iPad"),zc=G("Safari")&&!((G("Chrome")||G("CriOS"))&&!G("Edge")||G("Coast")||G("Opera")||G("Edge")||G("Edg/")||G("OPR")||G("Firefox")||G("FxiOS")||G("Silk")||G("Android"))&&!(hc()||G("iPad")||G("iPod"));var Ac={},Bc=null;
function Cc(a){var b=3;Ja(a);void 0===b&&(b=0);if(!Bc){Bc={};for(var c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),d=["+/=","+/","-_=","-_.","-_"],e=0;5>e;e++){var f=c.concat(d[e].split(""));Ac[e]=f;for(var g=0;g<f.length;g++){var h=f[g];void 0===Bc[h]&&(Bc[h]=g)}}}b=Ac[b];c=[];for(d=0;d<a.length;d+=3){var k=a[d],l=(e=d+1<a.length)?a[d+1]:0;h=(f=d+2<a.length)?a[d+2]:0;g=k>>2;k=(k&3)<<4|l>>4;l=(l&15)<<2|h>>6;h&=63;f||(h=64,e||(l=64));c.push(b[g],b[k],b[l]||"",b[h]||"")}return c.join("")}
;var K=window;var Dc=!kc||9<=Number(wc);function Ec(a,b){this.x=void 0!==a?a:0;this.y=void 0!==b?b:0}
m=Ec.prototype;m.clone=function(){return new Ec(this.x,this.y)};
m.equals=function(a){return a instanceof Ec&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
m.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
m.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
m.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};function Fc(a,b){this.width=a;this.height=b}
m=Fc.prototype;m.clone=function(){return new Fc(this.width,this.height)};
m.aspectRatio=function(){return this.width/this.height};
m.isEmpty=function(){return!(this.width*this.height)};
m.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
m.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
m.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Gc(a){var b=document;return"string"===typeof a?b.getElementById(a):a}
function Hc(a,b){db(b,function(c,d){c&&"object"==typeof c&&c.Z&&(c=c.Y());"style"==d?a.style.cssText=c:"class"==d?a.className=c:"for"==d?a.htmlFor=c:Ic.hasOwnProperty(d)?a.setAttribute(Ic[d],c):0==d.lastIndexOf("aria-",0)||0==d.lastIndexOf("data-",0)?a.setAttribute(d,c):a[d]=c})}
var Ic={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
function Jc(a,b,c){var d=arguments,e=document,f=String(d[0]),g=d[1];if(!Dc&&g&&(g.name||g.type)){f=["<",f];g.name&&f.push(' name="',Zb(g.name),'"');if(g.type){f.push(' type="',Zb(g.type),'"');var h={};ob(h,g);delete h.type;g=h}f.push(">");f=f.join("")}f=Kc(e,f);g&&("string"===typeof g?f.className=g:Array.isArray(g)?f.className=g.join(" "):Hc(f,g));2<d.length&&Lc(e,f,d);return f}
function Lc(a,b,c){function d(h){h&&b.appendChild("string"===typeof h?a.createTextNode(h):h)}
for(var e=2;e<c.length;e++){var f=c[e];if(!Ja(f)||Ka(f)&&0<f.nodeType)d(f);else{a:{if(f&&"number"==typeof f.length){if(Ka(f)){var g="function"==typeof f.item||"string"==typeof f.item;break a}if("function"===typeof f){g="function"==typeof f.item;break a}}g=!1}D(g?bb(f):f,d)}}}
function Kc(a,b){b=String(b);"application/xhtml+xml"===a.contentType&&(b=b.toLowerCase());return a.createElement(b)}
function Mc(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;function Nc(a){var b=Oc;if(b)for(var c in b)Object.prototype.hasOwnProperty.call(b,c)&&a.call(void 0,b[c],c,b)}
function Pc(){var a=[];Nc(function(b){a.push(b)});
return a}
var Oc={Cb:"allow-forms",Db:"allow-modals",Eb:"allow-orientation-lock",Fb:"allow-pointer-lock",Gb:"allow-popups",Hb:"allow-popups-to-escape-sandbox",Ib:"allow-presentation",Jb:"allow-same-origin",Kb:"allow-scripts",Lb:"allow-top-navigation",Mb:"allow-top-navigation-by-user-activation"},Qc=Va(function(){return Pc()});
function Rc(){var a=Kc(document,"IFRAME"),b={};D(Qc(),function(c){a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
;function Sc(a){Tc();var b=qb();a=b?b.createScriptURL(a):a;return new rb(a,sb)}
var Tc=Ga;function Uc(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var Vc=(new Date).getTime();function Wc(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));c=a.substring(0,a.indexOf("://"));if(!c)throw Error("URI is missing protocol: "+a);if("http"!==c&&"https"!==c&&"chrome-extension"!==c&&"moz-extension"!==c&&"file"!==c&&"android-app"!==c&&"chrome-search"!==c&&"chrome-untrusted"!==c&&"chrome"!==
c&&"app"!==c&&"devtools"!==c)throw Error("Invalid URI scheme in origin: "+c);a="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+1);b=b.substring(0,d);if("http"===c&&"80"!==e||"https"===c&&"443"!==e)a=":"+e}return c+"://"+b+a}
;function Xc(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;p=l=0}
function b(n){for(var r=g,q=0;64>q;q+=4)r[q/4]=n[q]<<24|n[q+1]<<16|n[q+2]<<8|n[q+3];for(q=16;80>q;q++)n=r[q-3]^r[q-8]^r[q-14]^r[q-16],r[q]=(n<<1|n>>>31)&4294967295;n=e[0];var E=e[1],I=e[2],J=e[3],ba=e[4];for(q=0;80>q;q++){if(40>q)if(20>q){var U=J^E&(I^J);var O=1518500249}else U=E^I^J,O=1859775393;else 60>q?(U=E&I|J&(E|I),O=2400959708):(U=E^I^J,O=3395469782);U=((n<<5|n>>>27)&4294967295)+U+ba+O+r[q]&4294967295;ba=J;J=I;I=(E<<30|E>>>2)&4294967295;E=n;n=U}e[0]=e[0]+n&4294967295;e[1]=e[1]+E&4294967295;
e[2]=e[2]+I&4294967295;e[3]=e[3]+J&4294967295;e[4]=e[4]+ba&4294967295}
function c(n,r){if("string"===typeof n){n=unescape(encodeURIComponent(n));for(var q=[],E=0,I=n.length;E<I;++E)q.push(n.charCodeAt(E));n=q}r||(r=n.length);q=0;if(0==l)for(;q+64<r;)b(n.slice(q,q+64)),q+=64,p+=64;for(;q<r;)if(f[l++]=n[q++],p++,64==l)for(l=0,b(f);q+64<r;)b(n.slice(q,q+64)),q+=64,p+=64}
function d(){var n=[],r=8*p;56>l?c(h,56-l):c(h,64-(l-56));for(var q=63;56<=q;q--)f[q]=r&255,r>>>=8;b(f);for(q=r=0;5>q;q++)for(var E=24;0<=E;E-=8)n[r++]=e[q]>>E&255;return n}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var l,p;a();return{reset:a,update:c,digest:d,Ma:function(){for(var n=d(),r="",q=0;q<n.length;q++)r+="0123456789ABCDEF".charAt(Math.floor(n[q]/16))+"0123456789ABCDEF".charAt(n[q]%16);return r}}}
;function Yc(a,b,c){var d=String(y.location.href);return d&&a&&b?[b,Zc(Wc(d),a,c||null)].join(" "):null}
function Zc(a,b,c){var d=[],e=[];if(1==(Array.isArray(c)?2:1))return e=[b,a],D(d,function(h){e.push(h)}),$c(e.join(" "));
var f=[],g=[];D(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];D(d,function(h){e.push(h)});
a=$c(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function $c(a){var b=Xc();b.update(a);return b.Ma().toLowerCase()}
;var ad={};function bd(a){this.h=a||{cookie:""}}
m=bd.prototype;m.isEnabled=function(){if(!y.navigator.cookieEnabled)return!1;if(!this.isEmpty())return!0;this.set("TESTCOOKIESENABLED","1",{ra:60});if("1"!==this.get("TESTCOOKIESENABLED"))return!1;this.remove("TESTCOOKIESENABLED");return!0};
m.set=function(a,b,c){var d=!1;if("object"===typeof c){var e=c.Rk;d=c.secure||!1;var f=c.domain||void 0;var g=c.path||void 0;var h=c.ra}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');void 0===h&&(h=-1);this.h.cookie=a+"="+b+(f?";domain="+f:"")+(g?";path="+g:"")+(0>h?"":0==h?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(Date.now()+1E3*h)).toUTCString())+(d?";secure":"")+(null!=e?";samesite="+e:"")};
m.get=function(a,b){for(var c=a+"=",d=(this.h.cookie||"").split(";"),e=0,f;e<d.length;e++){f=ub(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
m.remove=function(a,b,c){var d=void 0!==this.get(a);this.set(a,"",{ra:0,path:b,domain:c});return d};
m.isEmpty=function(){return!this.h.cookie};
m.clear=function(){for(var a=(this.h.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=ub(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var cd=new bd("undefined"==typeof document?null:document);function dd(a){return!!ad.FPA_SAMESITE_PHASE2_MOD||!(void 0===a||!a)}
function ed(a,b,c,d){(a=y[a])||(a=(new bd(document)).get(b));return a?Yc(a,c,d):null}
function fd(a){var b=void 0===b?!1:b;var c=Wc(String(y.location.href)),d=[];var e=b;e=void 0===e?!1:e;var f=y.__SAPISID||y.__APISID||y.__3PSAPISID||y.__OVERRIDE_SID;dd(e)&&(f=f||y.__1PSAPISID);if(f)e=!0;else{var g=new bd(document);f=g.get("SAPISID")||g.get("APISID")||g.get("__Secure-3PAPISID")||g.get("SID");dd(e)&&(f=f||g.get("__Secure-1PAPISID"));e=!!f}e&&(e=(c=0==c.indexOf("https:")||0==c.indexOf("chrome-extension:")||0==c.indexOf("moz-extension:"))?y.__SAPISID:y.__APISID,e||(e=new bd(document),
e=e.get(c?"SAPISID":"APISID")||e.get("__Secure-3PAPISID")),(e=e?Yc(e,c?"SAPISIDHASH":"APISIDHASH",a):null)&&d.push(e),c&&dd(b)&&((b=ed("__1PSAPISID","__Secure-1PAPISID","SAPISID1PHASH",a))&&d.push(b),(a=ed("__3PSAPISID","__Secure-3PAPISID","SAPISID3PHASH",a))&&d.push(a)));return 0==d.length?null:d.join(" ")}
;function gd(){this.h=[];this.i=-1}
gd.prototype.set=function(a,b){b=void 0===b?!0:b;0<=a&&52>a&&0===a%1&&this.h[a]!=b&&(this.h[a]=b,this.i=-1)};
gd.prototype.get=function(a){return!!this.h[a]};
function hd(a){-1==a.i&&(a.i=Za(a.h,function(b,c,d){return c?b+Math.pow(2,d):b},0));
return a.i}
;function id(a,b){this.j=a;this.l=b;this.i=0;this.h=null}
id.prototype.get=function(){if(0<this.i){this.i--;var a=this.h;this.h=a.next;a.next=null}else a=this.j();return a};
function jd(a,b){a.l(b);100>a.i&&(a.i++,b.next=a.h,a.h=b)}
;var kd;
function ld(){var a=y.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!G("Presto")&&(a=function(){var e=Kc(document,"IFRAME");e.style.display="none";document.documentElement.appendChild(e);var f=e.contentWindow;e=f.document;e.open();e.close();var g="callImmediate"+Math.random(),h="file:"==f.location.protocol?"*":f.location.protocol+"//"+f.location.host;e=B(function(k){if(("*"==h||k.origin==h)&&k.data==g)this.port1.onmessage()},this);
f.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){f.postMessage(g,h)}}});
if("undefined"!==typeof a&&!G("Trident")&&!G("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var e=c.xa;c.xa=null;e()}};
return function(e){d.next={xa:e};d=d.next;b.port2.postMessage(0)}}return function(e){y.setTimeout(e,0)}}
;function md(a){y.setTimeout(function(){throw a;},0)}
;function nd(){this.i=this.h=null}
nd.prototype.add=function(a,b){var c=od.get();c.set(a,b);this.i?this.i.next=c:this.h=c;this.i=c};
nd.prototype.remove=function(){var a=null;this.h&&(a=this.h,this.h=this.h.next,this.h||(this.i=null),a.next=null);return a};
var od=new id(function(){return new pd},function(a){return a.reset()});
function pd(){this.next=this.scope=this.h=null}
pd.prototype.set=function(a,b){this.h=a;this.scope=b;this.next=null};
pd.prototype.reset=function(){this.next=this.scope=this.h=null};function qd(a,b){rd||sd();td||(rd(),td=!0);ud.add(a,b)}
var rd;function sd(){if(y.Promise&&y.Promise.resolve){var a=y.Promise.resolve(void 0);rd=function(){a.then(vd)}}else rd=function(){var b=vd;
"function"!==typeof y.setImmediate||y.Window&&y.Window.prototype&&!G("Edge")&&y.Window.prototype.setImmediate==y.setImmediate?(kd||(kd=ld()),kd(b)):y.setImmediate(b)}}
var td=!1,ud=new nd;function vd(){for(var a;a=ud.remove();){try{a.h.call(a.scope)}catch(b){md(b)}jd(od,a)}td=!1}
;function wd(){this.i=-1}
;function xd(){this.i=64;this.h=[];this.m=[];this.o=[];this.l=[];this.l[0]=128;for(var a=1;a<this.i;++a)this.l[a]=0;this.u=this.j=0;this.reset()}
C(xd,wd);xd.prototype.reset=function(){this.h[0]=1732584193;this.h[1]=4023233417;this.h[2]=2562383102;this.h[3]=271733878;this.h[4]=3285377520;this.u=this.j=0};
function yd(a,b,c){c||(c=0);var d=a.o;if("string"===typeof b)for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.h[0];c=a.h[1];var g=a.h[2],h=a.h[3],k=a.h[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var l=1518500249}else f=c^g^h,l=1859775393;else 60>e?(f=c&g|h&(c|g),l=2400959708):
(f=c^g^h,l=3395469782);f=(b<<5|b>>>27)+f+k+l+d[e]&4294967295;k=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.h[0]=a.h[0]+b&4294967295;a.h[1]=a.h[1]+c&4294967295;a.h[2]=a.h[2]+g&4294967295;a.h[3]=a.h[3]+h&4294967295;a.h[4]=a.h[4]+k&4294967295}
xd.prototype.update=function(a,b){if(null!=a){void 0===b&&(b=a.length);for(var c=b-this.i,d=0,e=this.m,f=this.j;d<b;){if(0==f)for(;d<=c;)yd(this,a,d),d+=this.i;if("string"===typeof a)for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.i){yd(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.i){yd(this,e);f=0;break}}this.j=f;this.u+=b}};
xd.prototype.digest=function(){var a=[],b=8*this.u;56>this.j?this.update(this.l,56-this.j):this.update(this.l,this.i-(this.j-56));for(var c=this.i-1;56<=c;c--)this.m[c]=b&255,b/=256;yd(this,this.m);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.h[c]>>d&255,++b;return a};function zd(a){var b=A("window.location.href");null==a&&(a='Unknown Error of type "null/undefined"');if("string"===typeof a)return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};var c=!1;try{var d=a.lineNumber||a.line||"Not available"}catch(g){d="Not available",c=!0}try{var e=a.fileName||a.filename||a.sourceURL||y.$googDebugFname||b}catch(g){e="Not available",c=!0}b=Ad(a);if(!(!c&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name)){c=a.message;if(null==
c){if(a.constructor&&a.constructor instanceof Function){if(a.constructor.name)c=a.constructor.name;else if(c=a.constructor,Bd[c])c=Bd[c];else{c=String(c);if(!Bd[c]){var f=/function\s+([^\(]+)/m.exec(c);Bd[c]=f?f[1]:"[Anonymous]"}c=Bd[c]}c='Unknown Error of type "'+c+'"'}else c="Unknown Error of unknown type";"function"===typeof a.toString&&Object.prototype.toString!==a.toString&&(c+=": "+a.toString())}return{message:c,name:a.name||"UnknownError",lineNumber:d,fileName:e,stack:b||"Not available"}}a.stack=
b;return{message:a.message,name:a.name,lineNumber:a.lineNumber,fileName:a.fileName,stack:a.stack}}
function Ad(a,b){b||(b={});b[Cd(a)]=!0;var c=a.stack||"";(a=a.La)&&!b[Cd(a)]&&(c+="\nCaused by: ",a.stack&&0==a.stack.indexOf(a.toString())||(c+="string"===typeof a?a:a.message+"\n"),c+=Ad(a,b));return c}
function Cd(a){var b="";"function"===typeof a.toString&&(b=""+a);return b+a.stack}
var Bd={};function Dd(a){a&&"function"==typeof a.dispose&&a.dispose()}
;function Ed(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];Ja(d)?Ed.apply(null,d):Dd(d)}}
;function L(){this.h=this.h;this.u=this.u}
L.prototype.h=!1;L.prototype.dispose=function(){this.h||(this.h=!0,this.D())};
function Fd(a,b){a.h?b():(a.u||(a.u=[]),a.u.push(b))}
L.prototype.D=function(){if(this.u)for(;this.u.length;)this.u.shift()()};function Gd(a){return"string"==typeof a.className?a.className:a.getAttribute&&a.getAttribute("class")||""}
function Hd(a,b){"string"==typeof a.className?a.className=b:a.setAttribute&&a.setAttribute("class",b)}
function Id(a,b){a.classList?b=a.classList.contains(b):(a=a.classList?a.classList:Gd(a).match(/\S+/g)||[],b=0<=Wa(a,b));return b}
function Jd(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):Id(a,"inverted-hdpi")&&Hd(a,Xa(a.classList?a.classList:Gd(a).match(/\S+/g)||[],function(b){return"inverted-hdpi"!=b}).join(" "))}
;var Kd="StopIteration"in y?y.StopIteration:{message:"StopIteration",stack:""};function Ld(){}
Ld.prototype.next=function(){throw Kd;};
Ld.prototype.O=function(){return this};
function Md(a){if(a instanceof Ld)return a;if("function"==typeof a.O)return a.O(!1);if(Ja(a)){var b=0,c=new Ld;c.next=function(){for(;;){if(b>=a.length)throw Kd;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function Nd(a,b){if(Ja(a))try{D(a,b,void 0)}catch(c){if(c!==Kd)throw c;}else{a=Md(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==Kd)throw c;}}}
function Od(a){if(Ja(a))return bb(a);a=Md(a);var b=[];Nd(a,function(c){b.push(c)});
return b}
;function Pd(a,b){this.i={};this.h=[];this.T=this.j=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof Pd)for(c=Qd(a),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
function Qd(a){Rd(a);return a.h.concat()}
m=Pd.prototype;m.equals=function(a,b){if(this===a)return!0;if(this.j!=a.j)return!1;b=b||Sd;Rd(this);for(var c,d=0;c=this.h[d];d++)if(!b(this.get(c),a.get(c)))return!1;return!0};
function Sd(a,b){return a===b}
m.isEmpty=function(){return 0==this.j};
m.clear=function(){this.i={};this.T=this.j=this.h.length=0};
m.remove=function(a){return Object.prototype.hasOwnProperty.call(this.i,a)?(delete this.i[a],this.j--,this.T++,this.h.length>2*this.j&&Rd(this),!0):!1};
function Rd(a){if(a.j!=a.h.length){for(var b=0,c=0;b<a.h.length;){var d=a.h[b];Object.prototype.hasOwnProperty.call(a.i,d)&&(a.h[c++]=d);b++}a.h.length=c}if(a.j!=a.h.length){var e={};for(c=b=0;b<a.h.length;)d=a.h[b],Object.prototype.hasOwnProperty.call(e,d)||(a.h[c++]=d,e[d]=1),b++;a.h.length=c}}
m.get=function(a,b){return Object.prototype.hasOwnProperty.call(this.i,a)?this.i[a]:b};
m.set=function(a,b){Object.prototype.hasOwnProperty.call(this.i,a)||(this.j++,this.h.push(a),this.T++);this.i[a]=b};
m.forEach=function(a,b){for(var c=Qd(this),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
m.clone=function(){return new Pd(this)};
m.O=function(a){Rd(this);var b=0,c=this.T,d=this,e=new Ld;e.next=function(){if(c!=d.T)throw Error("The map has changed since the iterator was created");if(b>=d.h.length)throw Kd;var f=d.h[b++];return a?f:d.i[f]};
return e};var Td=function(){if(!y.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
try{y.addEventListener("test",Ga,b),y.removeEventListener("test",Ga,b)}catch(c){}return a}();function Ud(a,b){this.type=a;this.h=this.target=b;this.defaultPrevented=this.j=!1}
Ud.prototype.stopPropagation=function(){this.j=!0};
Ud.prototype.preventDefault=function(){this.defaultPrevented=!0};function Vd(a,b){Ud.call(this,a?a.type:"");this.relatedTarget=this.h=this.target=null;this.button=this.screenY=this.screenX=this.clientY=this.clientX=0;this.key="";this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.state=null;this.pointerId=0;this.pointerType="";this.i=null;a&&this.init(a,b)}
C(Vd,Ud);var Wd={2:"touch",3:"pen",4:"mouse"};
Vd.prototype.init=function(a,b){var c=this.type=a.type,d=a.changedTouches&&a.changedTouches.length?a.changedTouches[0]:null;this.target=a.target||a.srcElement;this.h=b;if(b=a.relatedTarget){if(mc){a:{try{ic(b.nodeName);var e=!0;break a}catch(f){}e=!1}e||(b=null)}}else"mouseover"==c?b=a.fromElement:"mouseout"==c&&(b=a.toElement);this.relatedTarget=b;d?(this.clientX=void 0!==d.clientX?d.clientX:d.pageX,this.clientY=void 0!==d.clientY?d.clientY:d.pageY,this.screenX=d.screenX||0,this.screenY=d.screenY||
0):(this.clientX=void 0!==a.clientX?a.clientX:a.pageX,this.clientY=void 0!==a.clientY?a.clientY:a.pageY,this.screenX=a.screenX||0,this.screenY=a.screenY||0);this.button=a.button;this.keyCode=a.keyCode||0;this.key=a.key||"";this.charCode=a.charCode||("keypress"==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.pointerId=a.pointerId||0;this.pointerType="string"===typeof a.pointerType?a.pointerType:Wd[a.pointerType]||"";this.state=a.state;
this.i=a;a.defaultPrevented&&Vd.M.preventDefault.call(this)};
Vd.prototype.stopPropagation=function(){Vd.M.stopPropagation.call(this);this.i.stopPropagation?this.i.stopPropagation():this.i.cancelBubble=!0};
Vd.prototype.preventDefault=function(){Vd.M.preventDefault.call(this);var a=this.i;a.preventDefault?a.preventDefault():a.returnValue=!1};var Xd="closure_listenable_"+(1E6*Math.random()|0);var Yd=0;function Zd(a,b,c,d,e){this.listener=a;this.h=null;this.src=b;this.type=c;this.capture=!!d;this.ha=e;this.key=++Yd;this.ba=this.ea=!1}
function $d(a){a.ba=!0;a.listener=null;a.h=null;a.src=null;a.ha=null}
;function ae(a){this.src=a;this.listeners={};this.h=0}
ae.prototype.add=function(a,b,c,d,e){var f=a.toString();a=this.listeners[f];a||(a=this.listeners[f]=[],this.h++);var g=be(a,b,d,e);-1<g?(b=a[g],c||(b.ea=!1)):(b=new Zd(b,this.src,f,!!d,e),b.ea=c,a.push(b));return b};
ae.prototype.remove=function(a,b,c,d){a=a.toString();if(!(a in this.listeners))return!1;var e=this.listeners[a];b=be(e,b,c,d);return-1<b?($d(e[b]),Array.prototype.splice.call(e,b,1),0==e.length&&(delete this.listeners[a],this.h--),!0):!1};
function ce(a,b){var c=b.type;c in a.listeners&&ab(a.listeners[c],b)&&($d(b),0==a.listeners[c].length&&(delete a.listeners[c],a.h--))}
function be(a,b,c,d){for(var e=0;e<a.length;++e){var f=a[e];if(!f.ba&&f.listener==b&&f.capture==!!c&&f.ha==d)return e}return-1}
;var de="closure_lm_"+(1E6*Math.random()|0),ee={},fe=0;function ge(a,b,c,d,e){if(d&&d.once)he(a,b,c,d,e);else if(Array.isArray(b))for(var f=0;f<b.length;f++)ge(a,b[f],c,d,e);else c=ie(c),a&&a[Xd]?je(a,b,c,Ka(d)?!!d.capture:!!d,e):ke(a,b,c,!1,d,e)}
function ke(a,b,c,d,e,f){if(!b)throw Error("Invalid event type");var g=Ka(e)?!!e.capture:!!e,h=le(a);h||(a[de]=h=new ae(a));c=h.add(b,c,d,g,f);if(!c.h){d=me();c.h=d;d.src=a;d.listener=c;if(a.addEventListener)Td||(e=g),void 0===e&&(e=!1),a.addEventListener(b.toString(),d,e);else if(a.attachEvent)a.attachEvent(ne(b.toString()),d);else if(a.addListener&&a.removeListener)a.addListener(d);else throw Error("addEventListener and attachEvent are unavailable.");fe++}}
function me(){function a(c){return b.call(a.src,a.listener,c)}
var b=oe;return a}
function he(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)he(a,b[f],c,d,e);else c=ie(c),a&&a[Xd]?a.j.add(String(b),c,!0,Ka(d)?!!d.capture:!!d,e):ke(a,b,c,!0,d,e)}
function pe(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)pe(a,b[f],c,d,e);else(d=Ka(d)?!!d.capture:!!d,c=ie(c),a&&a[Xd])?a.j.remove(String(b),c,d,e):a&&(a=le(a))&&(b=a.listeners[b.toString()],a=-1,b&&(a=be(b,c,d,e)),(c=-1<a?b[a]:null)&&qe(c))}
function qe(a){if("number"!==typeof a&&a&&!a.ba){var b=a.src;if(b&&b[Xd])ce(b.j,a);else{var c=a.type,d=a.h;b.removeEventListener?b.removeEventListener(c,d,a.capture):b.detachEvent?b.detachEvent(ne(c),d):b.addListener&&b.removeListener&&b.removeListener(d);fe--;(c=le(b))?(ce(c,a),0==c.h&&(c.src=null,b[de]=null)):$d(a)}}}
function ne(a){return a in ee?ee[a]:ee[a]="on"+a}
function oe(a,b){if(a.ba)a=!0;else{b=new Vd(b,this);var c=a.listener,d=a.ha||a.src;a.ea&&qe(a);a=c.call(d,b)}return a}
function le(a){a=a[de];return a instanceof ae?a:null}
var re="__closure_events_fn_"+(1E9*Math.random()>>>0);function ie(a){if("function"===typeof a)return a;a[re]||(a[re]=function(b){return a.handleEvent(b)});
return a[re]}
;function se(){L.call(this);this.j=new ae(this);this.N=this;this.F=null}
C(se,L);se.prototype[Xd]=!0;se.prototype.addEventListener=function(a,b,c,d){ge(this,a,b,c,d)};
se.prototype.removeEventListener=function(a,b,c,d){pe(this,a,b,c,d)};
function te(a,b){var c=a.F;if(c){var d=[];for(var e=1;c;c=c.F)d.push(c),++e}a=a.N;c=b.type||b;"string"===typeof b?b=new Ud(b,a):b instanceof Ud?b.target=b.target||a:(e=b,b=new Ud(c,a),ob(b,e));e=!0;if(d)for(var f=d.length-1;!b.j&&0<=f;f--){var g=b.h=d[f];e=ue(g,c,!0,b)&&e}b.j||(g=b.h=a,e=ue(g,c,!0,b)&&e,b.j||(e=ue(g,c,!1,b)&&e));if(d)for(f=0;!b.j&&f<d.length;f++)g=b.h=d[f],e=ue(g,c,!1,b)&&e}
se.prototype.D=function(){se.M.D.call(this);if(this.j){var a=this.j,b=0,c;for(c in a.listeners){for(var d=a.listeners[c],e=0;e<d.length;e++)++b,$d(d[e]);delete a.listeners[c];a.h--}}this.F=null};
function je(a,b,c,d,e){a.j.add(String(b),c,!1,d,e)}
function ue(a,b,c,d){b=a.j.listeners[String(b)];if(!b)return!0;b=b.concat();for(var e=!0,f=0;f<b.length;++f){var g=b[f];if(g&&!g.ba&&g.capture==c){var h=g.listener,k=g.ha||g.src;g.ea&&ce(a.j,g);e=!1!==h.call(k,d)&&e}}return e&&!d.defaultPrevented}
;function ve(a){var b=[];we(new xe,a,b);return b.join("")}
function xe(){}
function we(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(Array.isArray(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),we(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),ye(d,c),c.push(":"),we(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":ye(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var ze={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},Ae=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function ye(a,b){b.push('"',a.replace(Ae,function(c){var d=ze[c];d||(d="\\u"+(c.charCodeAt(0)|65536).toString(16).substr(1),ze[c]=d);return d}),'"')}
;function Be(a){if(!a)return!1;try{return!!a.$goog_Thenable}catch(b){return!1}}
;function Ce(a){this.h=0;this.o=void 0;this.l=this.i=this.j=null;this.u=this.m=!1;if(a!=Ga)try{var b=this;a.call(void 0,function(c){De(b,2,c)},function(c){De(b,3,c)})}catch(c){De(this,3,c)}}
function Ee(){this.next=this.context=this.onRejected=this.i=this.h=null;this.j=!1}
Ee.prototype.reset=function(){this.context=this.onRejected=this.i=this.h=null;this.j=!1};
var Fe=new id(function(){return new Ee},function(a){a.reset()});
function Ge(a,b,c){var d=Fe.get();d.i=a;d.onRejected=b;d.context=c;return d}
function He(a){return new Ce(function(b,c){c(a)})}
Ce.prototype.then=function(a,b,c){return Ie(this,"function"===typeof a?a:null,"function"===typeof b?b:null,c)};
Ce.prototype.$goog_Thenable=!0;function Je(a,b){return Ie(a,null,b,void 0)}
Ce.prototype.cancel=function(a){if(0==this.h){var b=new Ke(a);qd(function(){Le(this,b)},this)}};
function Le(a,b){if(0==a.h)if(a.j){var c=a.j;if(c.i){for(var d=0,e=null,f=null,g=c.i;g&&(g.j||(d++,g.h==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.h&&1==d?Le(c,b):(f?(d=f,d.next==c.l&&(c.l=d),d.next=d.next.next):Me(c),Ne(c,e,3,b)))}a.j=null}else De(a,3,b)}
function Oe(a,b){a.i||2!=a.h&&3!=a.h||Pe(a);a.l?a.l.next=b:a.i=b;a.l=b}
function Ie(a,b,c,d){var e=Ge(null,null,null);e.h=new Ce(function(f,g){e.i=b?function(h){try{var k=b.call(d,h);f(k)}catch(l){g(l)}}:f;
e.onRejected=c?function(h){try{var k=c.call(d,h);void 0===k&&h instanceof Ke?g(h):f(k)}catch(l){g(l)}}:g});
e.h.j=a;Oe(a,e);return e.h}
Ce.prototype.C=function(a){this.h=0;De(this,2,a)};
Ce.prototype.F=function(a){this.h=0;De(this,3,a)};
function De(a,b,c){if(0==a.h){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.h=1;a:{var d=c,e=a.C,f=a.F;if(d instanceof Ce){Oe(d,Ge(e||Ga,f||null,a));var g=!0}else if(Be(d))d.then(e,f,a),g=!0;else{if(Ka(d))try{var h=d.then;if("function"===typeof h){Qe(d,h,e,f,a);g=!0;break a}}catch(k){f.call(a,k);g=!0;break a}g=!1}}g||(a.o=c,a.h=b,a.j=null,Pe(a),3!=b||c instanceof Ke||Re(a,c))}}
function Qe(a,b,c,d,e){function f(k){h||(h=!0,d.call(e,k))}
function g(k){h||(h=!0,c.call(e,k))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function Pe(a){a.m||(a.m=!0,qd(a.B,a))}
function Me(a){var b=null;a.i&&(b=a.i,a.i=b.next,b.next=null);a.i||(a.l=null);return b}
Ce.prototype.B=function(){for(var a;a=Me(this);)Ne(this,a,this.h,this.o);this.m=!1};
function Ne(a,b,c,d){if(3==c&&b.onRejected&&!b.j)for(;a&&a.u;a=a.j)a.u=!1;if(b.h)b.h.j=null,Se(b,c,d);else try{b.j?b.i.call(b.context):Se(b,c,d)}catch(e){Te.call(null,e)}jd(Fe,b)}
function Se(a,b,c){2==b?a.i.call(a.context,c):a.onRejected&&a.onRejected.call(a.context,c)}
function Re(a,b){a.u=!0;qd(function(){a.u&&Te.call(null,b)})}
var Te=md;function Ke(a){Ta.call(this,a)}
C(Ke,Ta);Ke.prototype.name="cancel";function M(a){L.call(this);this.o=1;this.l=[];this.m=0;this.i=[];this.j={};this.B=!!a}
C(M,L);m=M.prototype;m.subscribe=function(a,b,c){var d=this.j[a];d||(d=this.j[a]=[]);var e=this.o;this.i[e]=a;this.i[e+1]=b;this.i[e+2]=c;this.o=e+3;d.push(e);return e};
function Ue(a,b,c,d){if(b=a.j[b]){var e=a.i;(b=$a(b,function(f){return e[f+1]==c&&e[f+2]==d}))&&a.aa(b)}}
m.aa=function(a){var b=this.i[a];if(b){var c=this.j[b];0!=this.m?(this.l.push(a),this.i[a+1]=Ga):(c&&ab(c,a),delete this.i[a],delete this.i[a+1],delete this.i[a+2])}return!!b};
m.U=function(a,b){var c=this.j[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.B)for(e=0;e<c.length;e++){var g=c[e];Ve(this.i[g+1],this.i[g+2],d)}else{this.m++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.i[g+1].apply(this.i[g+2],d)}finally{if(this.m--,0<this.l.length&&0==this.m)for(;c=this.l.pop();)this.aa(c)}}return 0!=e}return!1};
function Ve(a,b,c){qd(function(){a.apply(b,c)})}
m.clear=function(a){if(a){var b=this.j[a];b&&(D(b,this.aa,this),delete this.j[a])}else this.i.length=0,this.j={}};
m.D=function(){M.M.D.call(this);this.clear();this.l.length=0};function We(a){this.h=a}
We.prototype.set=function(a,b){void 0===b?this.h.remove(a):this.h.set(a,ve(b))};
We.prototype.get=function(a){try{var b=this.h.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
We.prototype.remove=function(a){this.h.remove(a)};function Xe(a){this.h=a}
C(Xe,We);function Ye(a){this.data=a}
function Ze(a){return void 0===a||a instanceof Ye?a:new Ye(a)}
Xe.prototype.set=function(a,b){Xe.M.set.call(this,a,Ze(b))};
Xe.prototype.i=function(a){a=Xe.M.get.call(this,a);if(void 0===a||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
Xe.prototype.get=function(a){if(a=this.i(a)){if(a=a.data,void 0===a)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function $e(a){this.h=a}
C($e,Xe);$e.prototype.set=function(a,b,c){if(b=Ze(b)){if(c){if(c<Date.now()){$e.prototype.remove.call(this,a);return}b.expiration=c}b.creation=Date.now()}$e.M.set.call(this,a,b)};
$e.prototype.i=function(a){var b=$e.M.i.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<Date.now()||c&&c>Date.now())$e.prototype.remove.call(this,a);else return b}};function af(){}
;function bf(){}
C(bf,af);bf.prototype.clear=function(){var a=Od(this.O(!0)),b=this;D(a,function(c){b.remove(c)})};function cf(a){this.h=a}
C(cf,bf);m=cf.prototype;m.isAvailable=function(){if(!this.h)return!1;try{return this.h.setItem("__sak","1"),this.h.removeItem("__sak"),!0}catch(a){return!1}};
m.set=function(a,b){try{this.h.setItem(a,b)}catch(c){if(0==this.h.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
m.get=function(a){a=this.h.getItem(a);if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
m.remove=function(a){this.h.removeItem(a)};
m.O=function(a){var b=0,c=this.h,d=new Ld;d.next=function(){if(b>=c.length)throw Kd;var e=c.key(b++);if(a)return e;e=c.getItem(e);if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
return d};
m.clear=function(){this.h.clear()};
m.key=function(a){return this.h.key(a)};function df(){var a=null;try{a=window.localStorage||null}catch(b){}this.h=a}
C(df,cf);function ef(a,b){this.i=a;this.h=null;if(kc&&!(9<=Number(wc))){ff||(ff=new Pd);this.h=ff.get(a);this.h||(b?this.h=document.getElementById(b):(this.h=document.createElement("userdata"),this.h.addBehavior("#default#userData"),document.body.appendChild(this.h)),ff.set(a,this.h));try{this.h.load(this.i)}catch(c){this.h=null}}}
C(ef,bf);var gf={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},ff=null;function hf(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(b){return gf[b]})}
m=ef.prototype;m.isAvailable=function(){return!!this.h};
m.set=function(a,b){this.h.setAttribute(hf(a),b);jf(this)};
m.get=function(a){a=this.h.getAttribute(hf(a));if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
m.remove=function(a){this.h.removeAttribute(hf(a));jf(this)};
m.O=function(a){var b=0,c=this.h.XMLDocument.documentElement.attributes,d=new Ld;d.next=function(){if(b>=c.length)throw Kd;var e=c[b++];if(a)return decodeURIComponent(e.nodeName.replace(/\./g,"%")).substr(1);e=e.nodeValue;if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
return d};
m.clear=function(){for(var a=this.h.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);jf(this)};
function jf(a){try{a.h.save(a.i)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function kf(a,b){this.i=a;this.h=b+"::"}
C(kf,bf);kf.prototype.set=function(a,b){this.i.set(this.h+a,b)};
kf.prototype.get=function(a){return this.i.get(this.h+a)};
kf.prototype.remove=function(a){this.i.remove(this.h+a)};
kf.prototype.O=function(a){var b=this.i.O(!0),c=this,d=new Ld;d.next=function(){for(var e=b.next();e.substr(0,c.h.length)!=c.h;)e=b.next();return a?e.substr(c.h.length):c.i.get(e)};
return d};function lf(a,b){1<b.length?a[b[0]]=b[1]:1===b.length&&Object.assign(a,b[0])}
;var mf=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};z("yt.config_",mf,void 0);function N(a){lf(mf,arguments)}
function F(a,b){return a in mf?mf[a]:b}
;var nf=[];function of(a){nf.forEach(function(b){return b(a)})}
function pf(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){qf(b)}}:a}
function qf(a){var b=A("yt.logging.errors.log");b?b(a,"ERROR",void 0,void 0,void 0):(b=F("ERRORS",[]),b.push([a,"ERROR",void 0,void 0,void 0]),N("ERRORS",b));of(a)}
function rf(a){var b=A("yt.logging.errors.log");b?b(a,"WARNING",void 0,void 0,void 0):(b=F("ERRORS",[]),b.push([a,"WARNING",void 0,void 0,void 0]),N("ERRORS",b))}
;var sf=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};z("yt.msgs_",sf,void 0);function tf(a){lf(sf,arguments)}
;function Q(a){a=uf(a);return"string"===typeof a&&"false"===a?!1:!!a}
function vf(a,b){a=uf(a);return void 0===a&&void 0!==b?b:Number(a||0)}
function uf(a){var b=F("EXPERIMENTS_FORCED_FLAGS",{});return void 0!==b[a]?b[a]:F("EXPERIMENT_FLAGS",{})[a]}
;var wf=0,xf=nc?"webkit":mc?"moz":kc?"ms":jc?"o":"";z("ytDomDomGetNextId",A("ytDomDomGetNextId")||function(){return++wf},void 0);var yf={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function zf(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(var b in a)b in yf||(this[b]=a[b]);var c=a.target||a.srcElement;c&&3==c.nodeType&&(c=c.parentNode);this.target=c;var d=a.relatedTarget;if(d)try{d=d.nodeName?d:null}catch(e){d=null}else"mouseover"==
this.type?d=a.fromElement:"mouseout"==this.type&&(d=a.toElement);this.relatedTarget=d;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.h=a.pageX;this.i=a.pageY}}catch(e){}}
function Af(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.h=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.i=a.clientY+b}}
zf.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
zf.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
zf.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var fb=y.ytEventsEventsListeners||{};z("ytEventsEventsListeners",fb,void 0);var Bf=y.ytEventsEventsCounter||{count:0};z("ytEventsEventsCounter",Bf,void 0);
function Cf(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return eb(function(e){var f="boolean"===typeof e[4]&&e[4]==!!d,g=Ka(e[4])&&Ka(d)&&jb(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
var Df=Va(function(){var a=!1;try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function Ef(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=Cf(a,b,c,d);if(e)return e;e=++Bf.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(h){h=new zf(h);if(!Mc(h.relatedTarget,function(k){return k==a}))return h.currentTarget=a,h.type=b,c.call(a,h)}:function(h){h=new zf(h);
h.currentTarget=a;return c.call(a,h)};
g=pf(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),Df()||"boolean"===typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);fb[e]=[a,b,c,g,d];return e}
function Ff(a){a&&("string"==typeof a&&(a=[a]),D(a,function(b){if(b in fb){var c=fb[b],d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?Df()||"boolean"===typeof c?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete fb[b]}}))}
;var Gf=window.ytcsi&&window.ytcsi.now?window.ytcsi.now:window.performance&&window.performance.timing&&window.performance.now&&window.performance.timing.navigationStart?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};function Hf(a,b){"function"===typeof a&&(a=pf(a));return window.setTimeout(a,b)}
function If(a){window.clearTimeout(a)}
;function Jf(a){this.C=a;this.i=null;this.m=0;this.B=null;this.o=0;this.j=[];for(a=0;4>a;a++)this.j.push(0);this.l=0;this.J=Ef(window,"mousemove",B(this.K,this));a=B(this.F,this);"function"===typeof a&&(a=pf(a));this.L=window.setInterval(a,25)}
C(Jf,L);Jf.prototype.K=function(a){void 0===a.h&&Af(a);var b=a.h;void 0===a.i&&Af(a);this.i=new Ec(b,a.i)};
Jf.prototype.F=function(){if(this.i){var a=Gf();if(0!=this.m){var b=this.B,c=this.i,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.m);this.j[this.l]=.5<Math.abs((d-this.o)/this.o)?1:0;for(c=b=0;4>c;c++)b+=this.j[c]||0;3<=b&&this.C();this.o=d}this.m=a;this.B=this.i;this.l=(this.l+1)%4}};
Jf.prototype.D=function(){window.clearInterval(this.L);Ff(this.J)};function Kf(){}
function Lf(a,b){return Mf(a,0,b)}
function Nf(a,b){return Mf(a,1,b)}
function Of(a,b){Mf(a,2,b)}
;function Pf(){Kf.apply(this,arguments)}
v(Pf,Kf);function Mf(a,b,c){void 0!==c&&Number.isNaN(Number(c))&&(c=void 0);var d=A("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):Hf(a,c||0)}
function Qf(a){if(void 0===a||!Number.isNaN(Number(a))){var b=A("yt.scheduler.instance.cancelJob");b?b(a):If(a)}}
Pf.prototype.start=function(){var a=A("yt.scheduler.instance.start");a&&a()};
Pf.prototype.pause=function(){var a=A("yt.scheduler.instance.pause");a&&a()};Pf.h||(Pf.h=new Pf);var Rf={};
function Sf(a){var b=void 0===a?{}:a;a=void 0===b.Qa?!0:b.Qa;b=void 0===b.eb?!1:b.eb;if(null==A("_lact",window)){var c=parseInt(F("LACT"),10);c=isFinite(c)?Date.now()-Math.max(c,0):-1;z("_lact",c,window);z("_fact",c,window);-1==c&&Tf();Ef(document,"keydown",Tf);Ef(document,"keyup",Tf);Ef(document,"mousedown",Tf);Ef(document,"mouseup",Tf);a&&(b?Ef(window,"touchmove",function(){Uf("touchmove",200)},{passive:!0}):(Ef(window,"resize",function(){Uf("resize",200)}),Ef(window,"scroll",function(){Uf("scroll",200)})));
new Jf(function(){Uf("mouse",100)});
Ef(document,"touchstart",Tf,{passive:!0});Ef(document,"touchend",Tf,{passive:!0})}}
function Uf(a,b){Rf[a]||(Rf[a]=!0,Nf(function(){Tf();Rf[a]=!1},b))}
function Tf(){null==A("_lact",window)&&Sf();var a=Date.now();z("_lact",a,window);-1==A("_fact",window)&&z("_fact",a,window);(a=A("ytglobal.ytUtilActivityCallback_"))&&a()}
function Vf(){var a=A("_lact",window);return null==a?-1:Math.max(Date.now()-a,0)}
;function Wf(){var a=Xf;A("yt.ads.biscotti.getId_")||z("yt.ads.biscotti.getId_",a,void 0)}
function Yf(a){z("yt.ads.biscotti.lastId_",a,void 0)}
;var Zf=/^[\w.]*$/,$f={q:!0,search_query:!0};function ag(a,b){b=a.split(b);for(var c={},d=0,e=b.length;d<e;d++){var f=b[d].split("=");if(1==f.length&&f[0]||2==f.length)try{var g=bg(f[0]||""),h=bg(f[1]||"");g in c?Array.isArray(c[g])?cb(c[g],h):c[g]=[c[g],h]:c[g]=h}catch(n){var k=n,l=f[0],p=String(ag);k.args=[{key:l,value:f[1],query:a,method:cg==p?"unchanged":p}];$f.hasOwnProperty(l)||rf(k)}}return c}
var cg=String(ag);function dg(a){var b=[];db(a,function(c,d){var e=encodeURIComponent(String(d)),f;Array.isArray(c)?f=c:f=[c];D(f,function(g){""==g?b.push(e):b.push(e+"="+encodeURIComponent(String(g)))})});
return b.join("&")}
function eg(a){"?"==a.charAt(0)&&(a=a.substr(1));return ag(a,"&")}
function fg(){var a=window.location.href;return-1!=a.indexOf("?")?(a=(a||"").split("#")[0],a=a.split("?",2),eg(1<a.length?a[1]:a[0])):{}}
function gg(a,b,c){var d=a.split("#",2);a=d[0];d=1<d.length?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=eg(e[1]||"");for(var f in b)!c&&null!==e&&f in e||(e[f]=b[f]);return fc(a,e)+d}
function hg(a){if(!b)var b=window.location.href;var c=a.match(ac)[1]||null,d=cc(a);c&&d?(a=a.match(ac),b=b.match(ac),a=a[3]==b[3]&&a[1]==b[1]&&a[4]==b[4]):a=d?cc(b)==d&&(Number(b.match(ac)[4]||null)||null)==(Number(a.match(ac)[4]||null)||null):!0;return a}
function bg(a){return a&&a.match(Zf)?a:decodeURIComponent(a.replace(/\+/g," "))}
;function ig(a){var b=jg;a=void 0===a?A("yt.ads.biscotti.lastId_")||"":a;var c=Object,d=c.assign,e={};e.dt=Vc;e.flash="0";a:{try{var f=b.h.top.location.href}catch(P){f=2;break a}f=f?f===b.i.location.href?0:1:2}e=(e.frm=f,e);e.u_tz=-(new Date).getTimezoneOffset();var g=void 0===g?K:g;try{var h=g.history.length}catch(P){h=0}e.u_his=h;e.u_java=!!K.navigator&&"unknown"!==typeof K.navigator.javaEnabled&&!!K.navigator.javaEnabled&&K.navigator.javaEnabled();K.screen&&(e.u_h=K.screen.height,e.u_w=K.screen.width,
e.u_ah=K.screen.availHeight,e.u_aw=K.screen.availWidth,e.u_cd=K.screen.colorDepth);K.navigator&&K.navigator.plugins&&(e.u_nplug=K.navigator.plugins.length);K.navigator&&K.navigator.mimeTypes&&(e.u_nmime=K.navigator.mimeTypes.length);h=b.h;try{var k=h.screenX;var l=h.screenY}catch(P){}try{var p=h.outerWidth;var n=h.outerHeight}catch(P){}try{var r=h.innerWidth;var q=h.innerHeight}catch(P){}try{var E=h.screenLeft;var I=h.screenTop}catch(P){}try{r=h.innerWidth,q=h.innerHeight}catch(P){}try{var J=h.screen.availWidth;
var ba=h.screen.availTop}catch(P){}k=[E,I,k,l,J,ba,p,n,r,q];l=b.h.top;try{var U=(l||window).document,O="CSS1Compat"==U.compatMode?U.documentElement:U.body;var oa=(new Fc(O.clientWidth,O.clientHeight)).round()}catch(P){oa=new Fc(-12245933,-12245933)}U=oa;oa={};O=new gd;y.SVGElement&&y.document.createElementNS&&O.set(0);l=Rc();l["allow-top-navigation-by-user-activation"]&&O.set(1);l["allow-popups-to-escape-sandbox"]&&O.set(2);y.crypto&&y.crypto.subtle&&O.set(3);y.TextDecoder&&y.TextEncoder&&O.set(4);
O=hd(O);oa.bc=O;oa.bih=U.height;oa.biw=U.width;oa.brdim=k.join();b=b.i;b=(oa.vis={visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[b.visibilityState||b.webkitVisibilityState||b.mozVisibilityState||""]||0,oa.wgl=!!K.WebGLRenderingContext,oa);c=d.call(c,e,b);c.ca_type="image";a&&(c.bid=a);return c}
var jg=new function(){var a=window.document;this.h=window;this.i=a};
z("yt.ads_.signals_.getAdSignalsString",function(a){return dg(ig(a))},void 0);var kg="XMLHttpRequest"in y?function(){return new XMLHttpRequest}:null;
function lg(){if(!kg)return null;var a=kg();return"open"in a?a:null}
function mg(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;var ng={Authorization:"AUTHORIZATION","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-Youtube-Chrome-Connected":"CHROME_CONNECTED_HEADER","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Delegation-Context":"INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},
og="app debugcss debugjs expflag force_ad_params force_ad_encrypted force_viral_ad_response_params forced_experiments innertube_snapshots innertube_goldens internalcountrycode internalipoverride absolute_experiments conditional_experiments sbb sr_bns_address client_dev_root_url".split(" "),pg=!1;
function qg(a,b){b=void 0===b?{}:b;var c=hg(a),d=Q("web_ajax_ignore_global_headers_if_set"),e;for(e in ng){var f=F(ng[e]);!f||!c&&cc(a)||d&&void 0!==b[e]||(b[e]=f)}if(c||!cc(a))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());if(c||!cc(a)){try{var g=(new Intl.DateTimeFormat).resolvedOptions().timeZone}catch(h){}g&&(b["X-YouTube-Time-Zone"]=g)}if(c||!cc(a))b["X-YouTube-Ad-Signals"]=dg(ig(void 0));return b}
function rg(a){var b=window.location.search,c=cc(a);Q("debug_handle_relative_url_for_query_forward_killswitch")||c||!hg(a)||(c=document.location.hostname);var d=bc(a.match(ac)[5]||null);d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;var e=eg(b),f={};D(og,function(g){e[g]&&(f[g]=e[g])});
return gg(a,f||{},!1)}
function sg(a,b){var c=b.format||"JSON";a=tg(a,b);var d=ug(a,b),e=!1,f=vg(a,function(k){if(!e){e=!0;h&&If(h);var l=mg(k),p=null,n=400<=k.status&&500>k.status,r=500<=k.status&&600>k.status;if(l||n||r)p=wg(a,c,k,b.convertToSafeHtml);if(l)a:if(k&&204==k.status)l=!0;else{switch(c){case "XML":l=0==parseInt(p&&p.return_code,10);break a;case "RAW":l=!0;break a}l=!!p}p=p||{};n=b.context||y;l?b.onSuccess&&b.onSuccess.call(n,k,p):b.onError&&b.onError.call(n,k,p);b.onFinish&&b.onFinish.call(n,k,p)}},b.method,
d,b.headers,b.responseType,b.withCredentials);
if(b.onTimeout&&0<b.timeout){var g=b.onTimeout;var h=Hf(function(){e||(e=!0,f.abort(),If(h),g.call(b.context||y,f))},b.timeout)}return f}
function tg(a,b){b.includeDomain&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=F("XSRF_FIELD_NAME",void 0);if(b=b.urlParams)b[c]&&delete b[c],a=gg(a,b||{},!0);return a}
function ug(a,b){var c=F("XSRF_FIELD_NAME",void 0),d=F("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.postParams,g=F("XSRF_FIELD_NAME",void 0),h;b.headers&&(h=b.headers["Content-Type"]);b.excludeXsrf||cc(a)&&!b.withCredentials&&cc(a)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.postParams&&b.postParams[g]||(f||(f={}),f[c]=d);f&&"string"===typeof e&&(e=eg(e),ob(e,f),e=b.postBodyFormat&&"JSON"==b.postBodyFormat?JSON.stringify(e):ec(e));f=e||f&&!gb(f);!pg&&f&&
"POST"!=b.method&&(pg=!0,qf(Error("AJAX request with postData should use POST")));return e}
function wg(a,b,c,d){var e=null;switch(b){case "JSON":try{var f=c.responseText}catch(g){throw d=Error("Error reading responseText"),d.params=a,rf(d),g;}a=c.getResponseHeader("Content-Type")||"";f&&0<=a.indexOf("json")&&(")]}'\n"===f.substring(0,5)&&(f=f.substring(5)),e=JSON.parse(f));break;case "XML":if(a=(a=c.responseXML)?xg(a):null)e={},D(a.getElementsByTagName("*"),function(g){e[g.tagName]=yg(g)})}d&&zg(e);
return e}
function zg(a){if(Ka(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=Qb(a[b],null);a[c]=d}else zg(a[b])}}
function xg(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function yg(a){var b="";D(a.childNodes,function(c){b+=c.nodeValue});
return b}
function vg(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&pf(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=lg();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;Q("debug_forward_web_query_parameters")&&(a=rg(a));k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=qg(a,e))for(var l in e)k.setRequestHeader(l,e[l]),"content-type"==l.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);
return k}
;var Ag=xc||yc;function Bg(a){var b=Lb;return b?0<=b.toLowerCase().indexOf(a):!1}
;var Cg={},Dg=0;
function Eg(a,b,c,d,e){e=void 0===e?"":e;if(a)if(c&&!Bg("cobalt")){if(a){a instanceof Db||(a="object"==typeof a&&a.Z?a.Y():String(a),Ib.test(a)?a=new Db(a,Eb):(a=String(a),a=a.replace(/(%0A|%0D)/g,""),a=(b=a.match(Hb))&&Gb.test(b[1])?new Db(a,Eb):null));a=Fb(a||Kb);if("about:invalid#zClosurez"===a||a.startsWith("data"))a="";else{if(!(a instanceof Ob)){b="object"==typeof a;var f=null;b&&a.oa&&(f=a.la());a=Qb(vb(b&&a.Z?a.Y():String(a)),f)}a instanceof Ob&&a.constructor===Ob?a=a.h:(Ia(a),a="type_error:SafeHtml");
a=encodeURIComponent(String(ve(a.toString())))}/^[\s\xa0]*$/.test(a)||(a=Jc("IFRAME",{src:'javascript:"<body><img src=\\""+'+a+'+"\\"></body>"',style:"display:none"}),(9==a.nodeType?a:a.ownerDocument||a.document).body.appendChild(a))}}else if(e)vg(a,b,"POST",e,d);else if(F("USE_NET_AJAX_FOR_PING_TRANSPORT",!1)||d)vg(a,b,"GET","",d);else{b:{try{var g=new Ua({url:a});if(g.j&&g.i||g.l){var h=bc(a.match(ac)[5]||null),k;if(!(k=!h||!h.endsWith("/aclk"))){var l=a.search(gc);d:{for(c=0;0<=(c=a.indexOf("ri",
c))&&c<l;){var p=a.charCodeAt(c-1);if(38==p||63==p){var n=a.charCodeAt(c+2);if(!n||61==n||38==n||35==n){var r=c;break d}}c+=3}r=-1}if(0>r)var q=null;else{var E=a.indexOf("&",r);if(0>E||E>l)E=l;r+=3;q=decodeURIComponent(a.substr(r,E-r).replace(/\+/g," "))}k="1"!==q}f=!k;break b}}catch(I){}f=!1}f?Fg(a)?(b&&b(),f=!0):f=!1:f=!1;f||Gg(a,b)}}
function Hg(a,b,c){c=void 0===c?"":c;Fg(a,c)?b&&b():Eg(a,b,void 0,void 0,c)}
function Fg(a,b){try{if(window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,void 0===b?"":b))return!0}catch(c){}return!1}
function Gg(a,b){var c=new Image,d=""+Dg++;Cg[d]=c;c.onload=c.onerror=function(){b&&Cg[d]&&b();delete Cg[d]};
c.src=a}
;var Ig=y.ytPubsubPubsubInstance||new M,Jg=y.ytPubsubPubsubSubscribedKeys||{},Kg=y.ytPubsubPubsubTopicToKeys||{},Lg=y.ytPubsubPubsubIsSynchronous||{};function Mg(a,b){var c=Ng();if(c&&b){var d=c.subscribe(a,function(){var e=arguments;var f=function(){Jg[d]&&b.apply&&"function"==typeof b.apply&&b.apply(window,e)};
try{Lg[a]?f():Hf(f,0)}catch(g){qf(g)}},void 0);
Jg[d]=!0;Kg[a]||(Kg[a]=[]);Kg[a].push(d);return d}return 0}
function Og(a){var b=Ng();b&&("number"===typeof a?a=[a]:"string"===typeof a&&(a=[parseInt(a,10)]),D(a,function(c){b.unsubscribeByKey(c);delete Jg[c]}))}
function Pg(a,b){var c=Ng();c&&c.publish.apply(c,arguments)}
function Qg(a){var b=Ng();if(b)if(b.clear(a),a)Rg(a);else for(var c in Kg)Rg(c)}
function Ng(){return y.ytPubsubPubsubInstance}
function Rg(a){Kg[a]&&(a=Kg[a],D(a,function(b){Jg[b]&&delete Jg[b]}),a.length=0)}
M.prototype.subscribe=M.prototype.subscribe;M.prototype.unsubscribeByKey=M.prototype.aa;M.prototype.publish=M.prototype.U;M.prototype.clear=M.prototype.clear;z("ytPubsubPubsubInstance",Ig,void 0);z("ytPubsubPubsubTopicToKeys",Kg,void 0);z("ytPubsubPubsubIsSynchronous",Lg,void 0);z("ytPubsubPubsubSubscribedKeys",Jg,void 0);var Sg=window,R=Sg.ytcsi&&Sg.ytcsi.now?Sg.ytcsi.now:Sg.performance&&Sg.performance.timing&&Sg.performance.now&&Sg.performance.timing.navigationStart?function(){return Sg.performance.timing.navigationStart+Sg.performance.now()}:function(){return(new Date).getTime()};var Tg=vf("initial_gel_batch_timeout",1E3),Ug=Math.pow(2,16)-1,Vg=null,Wg=0,Xg=void 0,Yg=0,Zg=0,$g=0,ah=!0,bh=y.ytLoggingTransportGELQueue_||new Map;z("ytLoggingTransportGELQueue_",bh,void 0);var ch=y.ytLoggingTransportTokensToCttTargetIds_||{};z("ytLoggingTransportTokensToCttTargetIds_",ch,void 0);
function dh(a,b){if("log_event"===a.endpoint){var c="";a.ga?c="visitorOnlyApprovedKey":a.G&&(ch[a.G.token]=eh(a.G),c=a.G.token);var d=bh.get(c)||[];bh.set(c,d);d.push(a.payload);b&&(Xg=new b);a=vf("tvhtml5_logging_max_batch")||vf("web_logging_max_batch")||100;b=R();d.length>=a?fh({writeThenSend:!0}):10<=b-$g&&(gh(),$g=b)}}
function hh(a,b){if("log_event"===a.endpoint){var c="";a.ga?c="visitorOnlyApprovedKey":a.G&&(ch[a.G.token]=eh(a.G),c=a.G.token);var d=new Map;d.set(c,[a.payload]);b&&(Xg=new b);return new Ce(function(e){Xg&&Xg.isReady()?ih(d,e,{bypassNetworkless:!0}):e()})}}
function fh(a){a=void 0===a?{}:a;new Ce(function(b){If(Yg);If(Zg);Zg=0;Xg&&Xg.isReady()?(ih(bh,b,a),bh.clear()):(gh(),b())})}
function gh(){Q("web_gel_timeout_cap")&&!Zg&&(Zg=Hf(function(){fh({writeThenSend:!0})},6E4));
If(Yg);var a=F("LOGGING_BATCH_TIMEOUT",vf("web_gel_debounce_ms",1E4));Q("shorten_initial_gel_batch_timeout")&&ah&&(a=Tg);Yg=Hf(function(){fh({writeThenSend:!0})},a)}
function ih(a,b,c){var d=Xg;c=void 0===c?{}:c;var e=Math.round(R()),f=a.size;a=u(a);for(var g=a.next();!g.done;g=a.next()){var h=u(g.value);g=h.next().value;var k=h.next().value;h=mb({context:jh(d.h||kh())});h.events=k;(k=ch[g])&&lh(h,g,k);delete ch[g];g="visitorOnlyApprovedKey"===g;mh(h,e,g);Q("send_beacon_before_gel")&&window.navigator&&window.navigator.sendBeacon&&!c.writeThenSend&&Hg("/generate_204");nh(d,"log_event",h,{retry:!0,onSuccess:function(){f--;f||b();Wg=Math.round(R()-e)},
onError:function(){f--;f||b()},
Ea:c,ga:g});ah=!1}}
function mh(a,b,c){a.requestTimeMs=String(b);Q("unsplit_gel_payloads_in_logs")&&(a.unsplitGelPayloadsInLogs=!0);!c&&(b=F("EVENT_ID",void 0))&&((c=F("BATCH_CLIENT_COUNTER",void 0)||0)||(c=Math.floor(Math.random()*Ug/2)),c++,c>Ug&&(c=1),N("BATCH_CLIENT_COUNTER",c),b={serializedEventId:b,clientCounter:String(c)},a.serializedClientEventId=b,Vg&&Wg&&Q("log_gel_rtt_web")&&(a.previousBatchInfo={serializedClientEventId:Vg,roundtripMs:String(Wg)}),Vg=b,Wg=0)}
function lh(a,b,c){if(c.videoId)var d="VIDEO";else if(c.playlistId)d="PLAYLIST";else return;a.credentialTransferTokenTargetId=c;a.context=a.context||{};a.context.user=a.context.user||{};a.context.user.credentialTransferTokens=[{token:b,scope:d}]}
function eh(a){var b={};a.videoId?b.videoId=a.videoId:a.playlistId&&(b.playlistId=a.playlistId);return b}
;var oh=y.ytLoggingGelSequenceIdObj_||{};z("ytLoggingGelSequenceIdObj_",oh,void 0);function ph(a,b,c,d){d=void 0===d?{}:d;var e={},f=Math.round(d.timestamp||R());e.eventTimeMs=f<Number.MAX_SAFE_INTEGER?f:0;e[a]=b;a=Vf();e.context={lastActivityMs:String(d.timestamp||!isFinite(a)?-1:a)};Q("log_sequence_info_on_gel_web")&&d.S&&(a=e.context,b=d.S,oh[b]=b in oh?oh[b]+1:0,a.sequence={index:oh[b],groupKey:b},d.Oa&&delete oh[d.S]);(d.Sk?hh:dh)({endpoint:"log_event",payload:e,G:d.G,ga:d.ga},c)}
;function qh(){if(!y.matchMedia)return"WEB_DISPLAY_MODE_UNKNOWN";try{return y.matchMedia("(display-mode: standalone)").matches?"WEB_DISPLAY_MODE_STANDALONE":y.matchMedia("(display-mode: minimal-ui)").matches?"WEB_DISPLAY_MODE_MINIMAL_UI":y.matchMedia("(display-mode: fullscreen)").matches?"WEB_DISPLAY_MODE_FULLSCREEN":y.matchMedia("(display-mode: browser)").matches?"WEB_DISPLAY_MODE_BROWSER":"WEB_DISPLAY_MODE_UNKNOWN"}catch(a){return"WEB_DISPLAY_MODE_UNKNOWN"}}
;function rh(a,b,c,d,e){cd.set(""+a,b,{ra:c,path:"/",domain:void 0===d?"youtube.com":d,secure:void 0===e?!1:e})}
;var sh=A("ytglobal.prefsUserPrefsPrefs_")||{};z("ytglobal.prefsUserPrefsPrefs_",sh,void 0);function th(){this.h=F("ALT_PREF_COOKIE_NAME","PREF");this.i=F("ALT_PREF_COOKIE_DOMAIN","youtube.com");var a=cd.get(""+this.h,void 0);if(a){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(sh[d]=c.toString())}}}
th.prototype.get=function(a,b){uh(a);vh(a);a=void 0!==sh[a]?sh[a].toString():null;return null!=a?a:b?b:""};
th.prototype.set=function(a,b){uh(a);vh(a);if(null==b)throw Error("ExpectedNotNull");sh[a]=b.toString()};
th.prototype.remove=function(a){uh(a);vh(a);delete sh[a]};
th.prototype.clear=function(){for(var a in sh)delete sh[a]};
function vh(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function uh(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function wh(a){a=void 0!==sh[a]?sh[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
Ha(th);var xh={bluetooth:"CONN_DISCO",cellular:"CONN_CELLULAR_UNKNOWN",ethernet:"CONN_WIFI",none:"CONN_NONE",wifi:"CONN_WIFI",wimax:"CONN_CELLULAR_4G",other:"CONN_UNKNOWN",unknown:"CONN_UNKNOWN","slow-2g":"CONN_CELLULAR_2G","2g":"CONN_CELLULAR_2G","3g":"CONN_CELLULAR_3G","4g":"CONN_CELLULAR_4G"},yh={"slow-2g":"EFFECTIVE_CONNECTION_TYPE_SLOW_2G","2g":"EFFECTIVE_CONNECTION_TYPE_2G","3g":"EFFECTIVE_CONNECTION_TYPE_3G","4g":"EFFECTIVE_CONNECTION_TYPE_4G"};
function zh(){var a=y.navigator;return a?a.connection:void 0}
;function Ah(){return"INNERTUBE_API_KEY"in mf&&"INNERTUBE_API_VERSION"in mf}
function kh(){return{innertubeApiKey:F("INNERTUBE_API_KEY",void 0),innertubeApiVersion:F("INNERTUBE_API_VERSION",void 0),Ra:F("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),Sa:F("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:F("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0),Ua:F("INNERTUBE_CONTEXT_HL",void 0),Ta:F("INNERTUBE_CONTEXT_GL",void 0),Va:F("INNERTUBE_HOST_OVERRIDE",void 0)||"",Xa:!!F("INNERTUBE_USE_THIRD_PARTY_AUTH",!1),Wa:!!F("INNERTUBE_OMIT_API_KEY_WHEN_AUTH_HEADER_IS_PRESENT",
!1),appInstallData:F("SERIALIZED_CLIENT_CONFIG_DATA",void 0)}}
function jh(a){var b={client:{hl:a.Ua,gl:a.Ta,clientName:a.Sa,clientVersion:a.innertubeContextClientVersion,configInfo:a.Ra}},c=y.devicePixelRatio;c&&1!=c&&(b.client.screenDensityFloat=String(c));c=F("EXPERIMENTS_TOKEN","");""!==c&&(b.client.experimentsToken=c);c=[];var d=F("EXPERIMENTS_FORCED_FLAGS",{});for(e in d)c.push({key:e,value:String(d[e])});var e=F("EXPERIMENT_FLAGS",{});for(var f in e)f.startsWith("force_")&&void 0===d[f]&&c.push({key:f,value:String(e[f])});0<c.length&&(b.request={internalExperimentFlags:c});
f=b.client.clientName;if("WEB"===f||"MWEB"===f||1===f||2===f){if(!Q("web_include_display_mode_killswitch")){var g;b.client.mainAppWebInfo=null!=(g=b.client.mainAppWebInfo)?g:{};b.client.mainAppWebInfo.webDisplayMode=qh()}}else if(g=b.client.clientName,("WEB_REMIX"===g||76===g)&&!Q("music_web_display_mode_killswitch")){var h;b.client.Da=null!=(h=b.client.Da)?h:{};b.client.Da.webDisplayMode=qh()}a.appInstallData&&(b.client.configInfo=b.client.configInfo||{},b.client.configInfo.appInstallData=a.appInstallData);
F("DELEGATED_SESSION_ID")&&!Q("pageid_as_header_web")&&(b.user={onBehalfOfUser:F("DELEGATED_SESSION_ID")});a:{if(h=zh()){a=xh[h.type||"unknown"]||"CONN_UNKNOWN";h=xh[h.effectiveType||"unknown"]||"CONN_UNKNOWN";"CONN_CELLULAR_UNKNOWN"===a&&"CONN_UNKNOWN"!==h&&(a=h);if("CONN_UNKNOWN"!==a)break a;if("CONN_UNKNOWN"!==h){a=h;break a}}a=void 0}a&&(b.client.connectionType=a);Q("web_log_effective_connection_type")&&(a=zh(),a=null!==a&&void 0!==a&&a.effectiveType?yh.hasOwnProperty(a.effectiveType)?yh[a.effectiveType]:
"EFFECTIVE_CONNECTION_TYPE_UNKNOWN":void 0,a&&(b.client.effectiveConnectionType=a));a=Object;h=a.assign;g=b.client;f={};e=u(Object.entries(eg(F("DEVICE",""))));for(c=e.next();!c.done;c=e.next())d=u(c.value),c=d.next().value,d=d.next().value,"cbrand"===c?f.deviceMake=d:"cmodel"===c?f.deviceModel=d:"cbr"===c?f.browserName=d:"cbrver"===c?f.browserVersion=d:"cos"===c?f.osName=d:"cosver"===c?f.osVersion=d:"cplatform"===c&&(f.platform=d);b.client=h.call(a,g,f);return b}
function Bh(a,b,c){c=void 0===c?{}:c;var d={"X-Goog-Visitor-Id":c.visitorData||F("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;(b=c.Jk||F("AUTHORIZATION"))||(a?b="Bearer "+A("gapi.auth.getToken")().Ik:b=fd([]));b&&(d.Authorization=b,d["X-Goog-AuthUser"]=F("SESSION_INDEX",0),Q("pageid_as_header_web")&&(d["X-Goog-PageId"]=F("DELEGATED_SESSION_ID")));return d}
;function Ch(a){a=Object.assign({},a);delete a.Authorization;var b=fd();if(b){var c=new xd;c.update(F("INNERTUBE_API_KEY",void 0));c.update(b);a.hash=Cc(c.digest())}return a}
;function Dh(a){var b=new df;(b=b.isAvailable()?a?new kf(b,a):b:null)||(a=new ef(a||"UserDataSharedStore"),b=a.isAvailable()?a:null);this.h=(a=b)?new $e(a):null;this.i=document.domain||window.location.hostname}
Dh.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.h)try{this.h.set(a,b,Date.now()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(ve(b))}catch(f){return}else e=escape(b);rh(a,e,c,this.i)};
Dh.prototype.get=function(a,b){var c=void 0,d=!this.h;if(!d)try{c=this.h.get(a)}catch(e){d=!0}if(d&&(c=cd.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
Dh.prototype.remove=function(a){this.h&&this.h.remove(a);var b=this.i;cd.remove(""+a,"/",void 0===b?"youtube.com":b)};var Eh;function Fh(){Eh||(Eh=new Dh("yt.innertube"));return Eh}
function Gh(a,b,c,d){if(d)return null;d=Fh().get("nextId",!0)||1;var e=Fh().get("requests",!0)||{};e[d]={method:a,request:b,authState:Ch(c),requestTime:Math.round(R())};Fh().set("nextId",d+1,86400,!0);Fh().set("requests",e,86400,!0);return d}
function Hh(a){var b=Fh().get("requests",!0)||{};delete b[a];Fh().set("requests",b,86400,!0)}
function Ih(a){var b=Fh().get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(R())-d.requestTime)){var e=d.authState,f=Ch(Bh(!1));jb(e,f)&&(e=d.request,"requestTimeMs"in e&&(e.requestTimeMs=Math.round(R())),nh(a,d.method,e,{}));delete b[c]}}Fh().set("requests",b,86400,!0)}}
;function Jh(a,b){this.version=a;this.args=b}
;function Kh(a,b){this.topic=a;this.h=b}
Kh.prototype.toString=function(){return this.topic};var Lh=A("ytPubsub2Pubsub2Instance")||new M;M.prototype.subscribe=M.prototype.subscribe;M.prototype.unsubscribeByKey=M.prototype.aa;M.prototype.publish=M.prototype.U;M.prototype.clear=M.prototype.clear;z("ytPubsub2Pubsub2Instance",Lh,void 0);var Mh=A("ytPubsub2Pubsub2SubscribedKeys")||{};z("ytPubsub2Pubsub2SubscribedKeys",Mh,void 0);var Nh=A("ytPubsub2Pubsub2TopicToKeys")||{};z("ytPubsub2Pubsub2TopicToKeys",Nh,void 0);var Oh=A("ytPubsub2Pubsub2IsAsync")||{};z("ytPubsub2Pubsub2IsAsync",Oh,void 0);
z("ytPubsub2Pubsub2SkipSubKey",null,void 0);function Ph(a,b){var c=Qh();c&&c.publish.call(c,a.toString(),a,b)}
function Rh(a){var b=Sh,c=Qh();if(!c)return 0;var d=c.subscribe(b.toString(),function(e,f){var g=A("ytPubsub2Pubsub2SkipSubKey");g&&g==d||(g=function(){if(Mh[d])try{if(f&&b instanceof Kh&&b!=e)try{var h=b.h,k=f;if(!k.args||!k.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");try{if(!h.T){var l=new h;h.T=l.version}var p=h.T}catch(n){}if(!p||k.version!=p)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{f=Reflect.construct(h,
bb(k.args))}catch(n){throw n.message="yt.pubsub2.Data.deserialize(): "+n.message,n;}}catch(n){throw n.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+b.toString()+": "+n.message,n;}a.call(window,f)}catch(n){qf(n)}},Oh[b.toString()]?A("yt.scheduler.instance")?Nf(g):Hf(g,0):g())});
Mh[d]=!0;Nh[b.toString()]||(Nh[b.toString()]=[]);Nh[b.toString()].push(d);return d}
function Th(){var a=Uh,b=Rh(function(c){a.apply(void 0,arguments);Vh(b)});
return b}
function Vh(a){var b=Qh();b&&("number"===typeof a&&(a=[a]),D(a,function(c){b.unsubscribeByKey(c);delete Mh[c]}))}
function Qh(){return A("ytPubsub2Pubsub2Instance")}
;function Wh(){}
;var Xh=[],Yh=!1;function Zh(a){Yh||(Xh.push({type:"ERROR",payload:a}),10<Xh.length&&Xh.shift())}
function $h(a,b){Yh||(Xh.push({type:"EVENT",eventType:a,payload:b}),10<Xh.length&&Xh.shift())}
;var ai=function(){var a;return function(){a||(a=new Dh("ytidb"));return a}}();
function bi(){var a;return null===(a=ai())||void 0===a?void 0:a.get("LAST_RESULT_ENTRY_KEY",!0)}
function ci(a,b,c){this.h=void 0===a?!1:a;this.failureMessage=b;this.j=c;(a=bi())||(a={createdTimestampMs:R(),isSupported:this.h,resultCount:0,hasSucceededOnce:this.h});this.i=a;var d;if(di()){var e;this.i.isSupported===this.h?e=Object.assign(Object.assign({},this.i),{resultCount:this.i.resultCount+1}):e={isSupported:this.h,resultCount:1,createdTimestampMs:R(),hasSucceededOnce:this.i.hasSucceededOnce||this.h};null===(d=ai())||void 0===d?void 0:d.set("LAST_RESULT_ENTRY_KEY",e,2592E3,!0)}}
function ei(a,b){return new ci(!1,a instanceof Error?a.message:"",void 0===b?!1:b)}
ci.prototype.isSupported=function(){return this.h};
ci.prototype.log=function(){di()&&$h("IS_SUPPORTED_COMPLETED",{isSupported:this.h,lastIsSupported:this.i.isSupported,failureMessage:this.failureMessage,sameResultCount:this.i.resultCount,sameResultDurationMs:Math.floor(R()-this.i.createdTimestampMs),canDetectDataOnFailure:this.j})};
function di(){var a;return!!(Q("ytidb_analyze_is_supported")&&(null===(a=ai())||void 0===a?0:a.h))}
;function fi(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];d=Error.call(this,a);this.message=d.message;"stack"in d&&(this.stack=d.stack);this.args=[].concat(c instanceof Array?c:ha(u(c)))}
v(fi,Error);function gi(a){if(0<=a.indexOf(":"))throw Error("Database name cannot contain ':'");}
function hi(a){return a.substr(0,a.indexOf(":"))||a}
;var ii={},ji=(ii.AUTH_INVALID="No user identifier specified.",ii.EXPLICIT_ABORT="Transaction was explicitly aborted.",ii.IDB_NOT_SUPPORTED="IndexedDB is not supported.",ii.MISSING_OBJECT_STORE="Object store not created.",ii.UNKNOWN_ABORT="Transaction was aborted for unknown reasons.",ii.QUOTA_EXCEEDED="The current transaction exceeded its quota limitations.",ii.QUOTA_MAYBE_EXCEEDED="The current transaction may have failed because of exceeding quota limitations.",ii.EXECUTE_TRANSACTION_ON_CLOSED_DB=
"Can't start a transaction on a closed database",ii),ki={},li=(ki.AUTH_INVALID="ERROR",ki.EXECUTE_TRANSACTION_ON_CLOSED_DB="WARNING",ki.EXPLICIT_ABORT="IGNORED",ki.IDB_NOT_SUPPORTED="ERROR",ki.MISSING_OBJECT_STORE="ERROR",ki.QUOTA_EXCEEDED="WARNING",ki.QUOTA_MAYBE_EXCEEDED="WARNING",ki.UNKNOWN_ABORT="WARNING",ki),mi={},ni=(mi.AUTH_INVALID=!1,mi.EXECUTE_TRANSACTION_ON_CLOSED_DB=!1,mi.EXPLICIT_ABORT=!1,mi.IDB_NOT_SUPPORTED=!1,mi.MISSING_OBJECT_STORE=!1,mi.QUOTA_EXCEEDED=!1,mi.QUOTA_MAYBE_EXCEEDED=!0,
mi.UNKNOWN_ABORT=!0,mi);function S(a,b,c,d,e){b=void 0===b?{}:b;c=void 0===c?ji[a]:c;d=void 0===d?li[a]:d;e=void 0===e?ni[a]:e;fi.call(this,c,Object.assign({name:"YtIdbKnownError",isSw:void 0===self.document,isIframe:self!==self.top,type:a},b));this.type=a;this.message=c;this.level=d;this.h=e;Object.setPrototypeOf(this,S.prototype)}
v(S,fi);function oi(a){S.call(this,"MISSING_OBJECT_STORE",{Nk:a},ji.MISSING_OBJECT_STORE);Object.setPrototypeOf(this,oi.prototype)}
v(oi,S);var pi=["The database connection is closing","Can't start a transaction on a closed database","A mutation operation was attempted on a database that did not allow mutations"];
function qi(a,b,c){b=hi(b);var d=a instanceof Error?a:Error("Unexpected error: "+a);if(d instanceof S)return d;if("QuotaExceededError"===d.name)return new S("QUOTA_EXCEEDED",{objectStoreNames:c,dbName:b});if(zc&&"UnknownError"===d.name)return new S("QUOTA_MAYBE_EXCEEDED",{objectStoreNames:c,dbName:b});if("InvalidStateError"===d.name&&pi.some(function(e){return d.message.includes(e)}))return new S("EXECUTE_TRANSACTION_ON_CLOSED_DB",{objectStoreNames:c,
dbName:b});if("AbortError"===d.name)return new S("UNKNOWN_ABORT",{objectStoreNames:c,dbName:b},d.message);d.args=[{name:"IdbError",Ok:d.name,dbName:b,objectStoreNames:c}];d.level="WARNING";return d}
;function ri(a){if(!a)throw Error();throw a;}
function si(a){return a}
function T(a){function b(e){if("PENDING"===d.state.status){d.state={status:"REJECTED",reason:e};e=u(d.onRejected);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
function c(e){if("PENDING"===d.state.status){d.state={status:"FULFILLED",value:e};e=u(d.h);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
var d=this;this.i=a;this.state={status:"PENDING"};this.h=[];this.onRejected=[];try{this.i(c,b)}catch(e){b(e)}}
T.all=function(a){return new T(function(b,c){var d=[],e=a.length;0===e&&b(d);for(var f={W:0};f.W<a.length;f={W:f.W},++f.W)ti(T.resolve(a[f.W]).then(function(g){return function(h){d[g.W]=h;e--;0===e&&b(d)}}(f)),function(g){c(g)})})};
T.resolve=function(a){return new T(function(b,c){a instanceof T?a.then(b,c):b(a)})};
T.reject=function(a){return new T(function(b,c){c(a)})};
T.prototype.then=function(a,b){var c=this,d=null!==a&&void 0!==a?a:si,e=null!==b&&void 0!==b?b:ri;return new T(function(f,g){"PENDING"===c.state.status?(c.h.push(function(){ui(c,c,d,f,g)}),c.onRejected.push(function(){vi(c,c,e,f,g)})):"FULFILLED"===c.state.status?ui(c,c,d,f,g):"REJECTED"===c.state.status&&vi(c,c,e,f,g)})};
function ti(a,b){a.then(void 0,b)}
function ui(a,b,c,d,e){try{if("FULFILLED"!==a.state.status)throw Error("calling handleResolve before the promise is fulfilled.");var f=c(a.state.value);f instanceof T?wi(a,b,f,d,e):d(f)}catch(g){e(g)}}
function vi(a,b,c,d,e){try{if("REJECTED"!==a.state.status)throw Error("calling handleReject before the promise is rejected.");var f=c(a.state.reason);f instanceof T?wi(a,b,f,d,e):d(f)}catch(g){e(g)}}
function wi(a,b,c,d,e){b===c?e(new TypeError("Circular promise chain detected.")):c.then(function(f){f instanceof T?wi(a,b,f,d,e):d(f)},function(f){e(f)})}
;function xi(a,b,c){function d(){c(a.error);f()}
function e(){b(a.result);f()}
function f(){try{a.removeEventListener("success",e),a.removeEventListener("error",d)}catch(g){}}
a.addEventListener("success",e);a.addEventListener("error",d)}
function yi(a){return new Promise(function(b,c){xi(a,b,c)})}
function V(a){return new T(function(b,c){xi(a,b,c)})}
;function zi(a,b){return new T(function(c,d){function e(){var f=a?b(a):null;f?f.then(function(g){a=g;e()},d):c()}
e()})}
;function Ai(a){return new Promise(function(b){Of(function(){b()},a)})}
function Bi(a,b){this.h=a;this.options=b;this.transactionCount=0;this.j=Math.round(R());this.i=!1}
m=Bi.prototype;m.add=function(a,b,c){return Ci(this,[a],{mode:"readwrite",I:!0},function(d){return Di(d,a).add(b,c)})};
m.clear=function(a){return Ci(this,[a],{mode:"readwrite",I:!0},function(b){return Di(b,a).clear()})};
m.close=function(){var a;this.h.close();(null===(a=this.options)||void 0===a?0:a.closed)&&this.options.closed()};
m.count=function(a,b){return Ci(this,[a],{mode:"readonly",I:!0},function(c){return Di(c,a).count(b)})};
function Ei(a,b,c){a=a.h.createObjectStore(b,c);return new Fi(a)}
m.delete=function(a,b){return Ci(this,[a],{mode:"readwrite",I:!0},function(c){return Di(c,a).delete(b)})};
m.get=function(a,b){return Ci(this,[a],{mode:"readonly",I:!0},function(c){return Di(c,a).get(b)})};
function Gi(a,b,c,d){return Ci(a,[b],{mode:"readwrite",I:!0},function(e){e=Di(e,b);return V(e.h.put(c,d))})}
function Ci(a,b,c,d){return H(a,function f(){var g=this,h,k,l,p,n,r,q,E,I,J,ba,U,O,oa;return x(f,function(P){switch(P.h){case 1:var lb={mode:"readonly",I:!1};"string"===typeof c?lb.mode=c:lb=c;h=lb;g.transactionCount++;k=Q("ytidb_transaction_exponential_backoff_retries");l=h.I?vf("ytidb_transaction_try_count",1):1;p=500;n=0;case 2:if(r){P.A(3);break}n++;q=Math.round(R());ta(P,4);E=g.h.transaction(b,h.mode);lb=new Hi(E);lb=Ii(lb,d);return w(P,lb,6);case 6:return I=P.i,J=Math.round(R()),Ji(g,q,J,n,
void 0,b.join(),h),P.return(I);case 4:ba=ua(P);U=Math.round(R());O=qi(ba,g.h.name,b.join());if((oa=O instanceof S&&!O.h)||n>=l){Ji(g,q,U,n,O,b.join(),h);r=O;P.A(2);break}if(!k){P.A(2);break}return w(P,Ai(p),9);case 9:p*=2;P.A(2);break;case 3:return P.return(Promise.reject(r))}})})}
function Ji(a,b,c,d,e,f,g){b=c-b;e?(e instanceof S&&("QUOTA_EXCEEDED"===e.type||"QUOTA_MAYBE_EXCEEDED"===e.type)&&$h("QUOTA_EXCEEDED",{dbName:hi(a.h.name),objectStoreNames:f,transactionCount:a.transactionCount,transactionMode:g.mode}),e instanceof S&&"UNKNOWN_ABORT"===e.type&&($h("TRANSACTION_UNEXPECTEDLY_ABORTED",{objectStoreNames:f,transactionDuration:b,transactionCount:a.transactionCount,dbDuration:c-a.j}),a.i=!0),Ki(a,!1,d,f,b),Zh(e)):Ki(a,!0,d,f,b)}
function Ki(a,b,c,d,e){$h("TRANSACTION_ENDED",{objectStoreNames:d,connectionHasUnknownAbortedTransaction:a.i,duration:e,isSuccessful:b,tryCount:c})}
function Fi(a){this.h=a}
m=Fi.prototype;m.add=function(a,b){return V(this.h.add(a,b))};
m.clear=function(){return V(this.h.clear()).then(function(){})};
m.count=function(a){return V(this.h.count(a))};
function Li(a,b){return Mi(a,{query:b},function(c){return c.delete().then(function(){return c.continue()})}).then(function(){})}
m.delete=function(a){return a instanceof IDBKeyRange?Li(this,a):V(this.h.delete(a))};
m.get=function(a){return V(this.h.get(a))};
m.index=function(a){return new Ni(this.h.index(a))};
m.getName=function(){return this.h.name};
function Mi(a,b,c){a=a.h.openCursor(b.query,b.direction);return Oi(a).then(function(d){return zi(d,c)})}
function Hi(a){var b=this;this.h=a;this.i=new Map;this.aborted=!1;this.done=new Promise(function(c,d){b.h.addEventListener("complete",function(){c()});
b.h.addEventListener("error",function(e){e.currentTarget===e.target&&d(b.h.error)});
b.h.addEventListener("abort",function(){var e=b.h.error;if(e)d(e);else if(!b.aborted){e=S;for(var f=b.h.objectStoreNames,g=[],h=0;h<f.length;h++){var k=f.item(h);if(null===k)throw Error("Invariant: item in DOMStringList is null");g.push(k)}e=new e("UNKNOWN_ABORT",{objectStoreNames:g.join(),dbName:b.h.db.name,mode:b.h.mode});d(e)}})})}
function Ii(a,b){var c=new Promise(function(d,e){ti(b(a).then(function(f){a.commit();d(f)}),e)});
return Promise.all([c,a.done]).then(function(d){return u(d).next().value})}
Hi.prototype.abort=function(){this.h.abort();this.aborted=!0;throw new S("EXPLICIT_ABORT");};
Hi.prototype.commit=function(){var a=this.h;a.commit&&!this.aborted&&a.commit()};
function Di(a,b){b=a.h.objectStore(b);var c=a.i.get(b);c||(c=new Fi(b),a.i.set(b,c));return c}
function Ni(a){this.h=a}
Ni.prototype.count=function(a){return V(this.h.count(a))};
Ni.prototype.delete=function(a){return Pi(this,{query:a},function(b){return b.delete().then(function(){return b.continue()})})};
Ni.prototype.get=function(a){return V(this.h.get(a))};
Ni.prototype.getKey=function(a){return V(this.h.getKey(a))};
function Pi(a,b,c){a=a.h.openCursor(void 0===b.query?null:b.query,void 0===b.direction?"next":b.direction);return Oi(a).then(function(d){return zi(d,c)})}
function Qi(a,b){this.request=a;this.cursor=b}
function Oi(a){return V(a).then(function(b){return null===b?null:new Qi(a,b)})}
m=Qi.prototype;m.advance=function(a){this.cursor.advance(a);return Oi(this.request)};
m.continue=function(a){this.cursor.continue(a);return Oi(this.request)};
m.delete=function(){return V(this.cursor.delete()).then(function(){})};
m.getKey=function(){return this.cursor.key};
m.getValue=function(){return this.cursor.value};
m.update=function(a){return V(this.cursor.update(a))};function Ri(a,b,c){return H(this,function e(){var f,g,h,k,l,p,n,r,q,E;return x(e,function(I){if(1==I.h)return f=self.indexedDB.open(a,b),g=c,h=g.blocked,k=g.blocking,l=g.pb,p=g.upgrade,n=g.closed,q=function(){r||(r=new Bi(f.result,{closed:n}));return r},f.addEventListener("upgradeneeded",function(J){if(null===J.newVersion)throw Error("Invariant: newVersion on IDbVersionChangeEvent is null");
if(null===f.transaction)throw Error("Invariant: transaction on IDbOpenDbRequest is null");J.dataLoss&&"none"!==J.dataLoss&&$h("IDB_DATA_CORRUPTED",{reason:J.dataLossMessage||"unknown reason",dbName:hi(a)});var ba=q(),U=new Hi(f.transaction);p&&p(ba,J.oldVersion,J.newVersion,U)}),h&&f.addEventListener("blocked",function(){h()}),w(I,yi(f),2);
E=I.i;k&&E.addEventListener("versionchange",function(){k(q())});
E.addEventListener("close",function(){$h("IDB_UNEXPECTEDLY_CLOSED",{dbName:hi(a),dbVersion:E.version});l&&l()});
return I.return(q())})})}
function Si(a,b,c){c=void 0===c?{}:c;return Ri(a,b,c)}
function Ti(a,b){b=void 0===b?{}:b;return H(this,function d(){var e,f,g;return x(d,function(h){e=self.indexedDB.deleteDatabase(a);f=b;(g=f.blocked)&&e.addEventListener("blocked",function(){g()});
return w(h,yi(e),0)})})}
;function Ui(a,b){this.name=a;this.options=b;this.j=!1}
Ui.prototype.i=function(a,b,c){c=void 0===c?{}:c;return Si(a,b,c)};
Ui.prototype.delete=function(a){a=void 0===a?{}:a;return Ti(this.name,a)};
Ui.prototype.open=function(){var a=this;if(!this.h){var b,c=function(){a.h===b&&(a.h=void 0)},d={blocking:function(f){f.close()},
closed:c,pb:c,upgrade:this.options.upgrade},e=function(){return H(a,function g(){var h=this,k,l,p;return x(g,function(n){switch(n.h){case 1:return ta(n,2),w(n,h.i(h.name,h.options.version,d),4);case 4:k=n.i;a:{var r=u(Object.keys(h.options.Fa));for(var q=r.next();!q.done;q=r.next())if(q=q.value,!k.h.objectStoreNames.contains(q)){r=q;break a}r=void 0}l=r;if(void 0===l){n.A(5);break}if(h.j){n.A(6);break}h.j=!0;return w(n,h.delete(),7);case 7:return n.return(e());case 6:throw new oi(l);case 5:return n.return(k);
case 2:p=ua(n);if(p instanceof DOMException?"VersionError"===p.name:"DOMError"in self&&p instanceof DOMError?"VersionError"===p.name:p instanceof Object&&"message"in p&&"An attempt was made to open a database using a lower version than the existing version."===p.message)return n.return(h.i(h.name,void 0,Object.assign(Object.assign({},d),{upgrade:void 0})));c();throw p;}})})};
this.h=b=e()}return this.h};var Vi=new Ui("YtIdbMeta",{Fa:{databases:!0},upgrade:function(a,b){1>b&&Ei(a,"databases",{keyPath:"actualName"})}});
function Wi(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,Vi.open(),2);d=e.i;return e.return(Ci(d,["databases"],{I:!0,mode:"readwrite"},function(f){var g=Di(f,"databases");return g.get(a.actualName).then(function(h){if(h?a.actualName!==h.actualName||a.publicName!==h.publicName||a.userIdentifier!==h.userIdentifier||a.clearDataOnAuthChange!==h.clearDataOnAuthChange:1)return V(g.h.put(a,void 0)).then(function(){})})}))})})}
function Xi(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,Vi.open(),2);d=e.i;return e.return(d.delete("databases",a))})})}
function Yi(){return H(this,function b(){var c,d;return x(b,function(e){if(1==e.h)return w(e,Vi.open(),2);if(3!=e.h)return c=e.i,w(e,c.count("databases"),3);d=e.i;return e.return(0<d)})})}
function Zi(a){return H(this,function c(){var d,e;return x(c,function(f){return 1==f.h?(d=[],w(f,Vi.open(),2)):3!=f.h?(e=f.i,w(f,Ci(e,["databases"],{I:!0,mode:"readonly"},function(g){d.length=0;return Mi(Di(g,"databases"),{},function(h){a(h.getValue())&&d.push(h.getValue());return h.continue()})}),3)):f.return(d)})})}
function $i(){return Zi(function(a){return"LogsDatabaseV2"===a.publicName&&void 0!==a.userIdentifier})}
;var aj;
function bj(){return H(this,function b(){var c,d,e,f,g;return x(b,function(h){switch(h.h){case 1:if(Q("ytidb_is_supported_cache_success_result")&&(c=bi(),null===c||void 0===c?0:c.hasSucceededOnce))return h.return(new ci(!0));var k;if(k=Ag)k=/WebKit\/([0-9]+)/.exec(Lb),k=!!(k&&600<=parseInt(k[1],10));k&&(k=/WebKit\/([0-9]+)/.exec(Lb),k=!(k&&602<=parseInt(k[1],10)));if(k)return h.return(ei(Error("YtIdb is not supported on iOS 8 or 9")));if(lc)return h.return(ei(Error("YtIdb is not supported on Edge")));try{if(d=
self,!(d.indexedDB&&d.IDBIndex&&d.IDBKeyRange&&d.IDBObjectStore))return h.return(ei(Error("Non-prefixed indexedDB APIs are missing")))}catch(l){return h.return(ei(l))}if(!("IDBTransaction"in self&&"objectStoreNames"in IDBTransaction.prototype))return h.return(ei(Error("IDBTransaction.prototype.objectStoreNames is missing")));ta(h,2);e={actualName:"yt-idb-test-do-not-use",publicName:"yt-idb-test-do-not-use",userIdentifier:void 0};return w(h,Wi(e),4);case 4:return w(h,Xi("yt-idb-test-do-not-use"),5);
case 5:return h.return(new ci(!0));case 2:f=ua(h);if(!di()){h.A(6);break}ta(h,7);return w(h,Yi(),9);case 9:return g=h.i,h.return(ei(f,g));case 7:return ua(h),h.return(ei(f));case 6:return h.return(ei(f))}})})}
function cj(){if(void 0!==aj)return aj;Yh=!0;return aj=bj().then(function(a){Yh=!1;a.log();return a.isSupported()})}
;function dj(){var a=new S("AUTH_INVALID");Zh(a);throw a;throw Error("Datasync ID not set");}
function ej(a,b,c,d){var e;return H(this,function g(){var h,k;return x(g,function(l){switch(l.h){case 1:return w(l,fj({caller:"openDbImpl",publicName:a,version:b}),2);case 2:return gi(a),c?h={actualName:a,publicName:a,userIdentifier:void 0}:h=dj(),h.clearDataOnAuthChange=null!==(e=d.clearDataOnAuthChange)&&void 0!==e?e:!1,ta(l,3),w(l,Wi(h),5);case 5:return w(l,Si(h.actualName,b,d),6);case 6:return l.return(l.i);case 3:return k=ua(l),ta(l,7),w(l,Xi(h.actualName),9);case 9:l.h=8;l.m=0;break;case 7:ua(l);
case 8:throw k;}})})}
function fj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,cj(),2);if(!e.i)throw d=new S("IDB_NOT_SUPPORTED",{context:a}),Zh(d),d;e.h=0})})}
function gj(a,b,c){c=void 0===c?{}:c;return ej(a,b,!1,c)}
function hj(a,b,c){c=void 0===c?{}:c;return ej(a,b,!0,c)}
function ij(a,b){b=void 0===b?{}:b;return H(this,function d(){var e;return x(d,function(f){if(1==f.h)return w(f,cj(),2);if(3!=f.h){if(!f.i)return f.return();gi(a);e=dj();return w(f,Ti(e.actualName,b),3)}return w(f,Xi(e.actualName),0)})})}
function jj(a,b){var c=this;a=a.map(function(d){return H(c,function f(){return x(f,function(g){return 1==g.h?w(g,Ti(d.actualName,b),2):w(g,Xi(d.actualName),0)})})});
return Promise.all(a).then(function(){})}
function kj(){var a=void 0===a?{}:a;return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,cj(),2);if(3!=e.h){if(!e.i)return e.return();gi("LogsDatabaseV2");return w(e,$i(),3)}d=e.i;return w(e,jj(d,a),0)})})}
function lj(a,b){b=void 0===b?{}:b;return H(this,function d(){return x(d,function(e){if(1==e.h)return w(e,cj(),2);if(3!=e.h){if(!e.i)return e.return();gi(a);return w(e,Ti(a,b),3)}return w(e,Xi(a),0)})})}
;function mj(a,b){Ui.call(this,a,b);this.options=b;gi(a)}
v(mj,Ui);mj.prototype.i=function(a,b,c){c=void 0===c?{}:c;return(this.options.Ia?hj:gj)(a,b,Object.assign(Object.assign({},c),{clearDataOnAuthChange:this.options.clearDataOnAuthChange}))};
mj.prototype.delete=function(a){a=void 0===a?{}:a;return(this.options.Ia?lj:ij)(this.name,a)};
function nj(a){var b;return function(){b||(b=new mj("LogsDatabaseV2",a));return b}}
;function oj(){T.call(this,function(){});
throw Error("Not allowed to instantiate the thennable outside of the core library.");}
v(oj,T);oj.reject=T.reject;oj.resolve=T.resolve;oj.all=T.all;var pj;function qj(){if(!pj){var a={};pj=nj({Fa:(a.LogsRequestsStore=!0,a.sapisid=!0,a.SWHealthLog=!0,a),Ia:!Q("nwl_use_ytidb_partitioning"),upgrade:function(b,c){2>c&&(Ei(b,"LogsRequestsStore",{keyPath:"id",autoIncrement:!0}).h.createIndex("newRequest",["status","authHash","interface","timestamp"],{unique:!1}),Ei(b,"sapisid"));3>c&&Ei(b,"SWHealthLog",{keyPath:"id",autoIncrement:!0}).h.createIndex("swHealthNewRequest",["interface","timestamp"],{unique:!1})},
version:3})}return pj().open()}
function rj(a){return H(this,function c(){var d,e,f,g,h;return x(c,function(k){switch(k.h){case 1:return d={startTime:R(),transactionType:"YT_IDB_TRANSACTION_TYPE_WRITE"},w(k,sj(),2);case 2:return e=k.i,w(k,qj(),3);case 3:return f=k.i,g=Object.assign(Object.assign({},a),{options:JSON.parse(JSON.stringify(a.options)),authHash:e,interface:F("INNERTUBE_CONTEXT_CLIENT_NAME",0)}),w(k,Gi(f,"LogsRequestsStore",g),4);case 4:return h=k.i,d.qb=R(),tj(d),k.return(h)}})})}
function uj(a){return H(this,function c(){var d,e,f,g,h,k,l,p;return x(c,function(n){switch(n.h){case 1:return d={startTime:R(),transactionType:"YT_IDB_TRANSACTION_TYPE_READ"},w(n,sj(),2);case 2:return e=n.i,f=F("INNERTUBE_CONTEXT_CLIENT_NAME",0),g=[a,e,f,0],h=[a,e,f,R()],k=IDBKeyRange.bound(g,h),w(n,qj(),3);case 3:return l=n.i,p=void 0,w(n,Ci(l,["LogsRequestsStore"],{mode:"readwrite",I:!0},function(r){return Pi(Di(r,"LogsRequestsStore").index("newRequest"),{query:k,direction:"prev"},function(q){q.getValue()&&
(p=q.getValue(),"NEW"===a&&(p.status="QUEUED",q.update(p)))})}),4);
case 4:return d.qb=R(),tj(d),n.return(p)}})})}
function vj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,qj(),2);d=e.i;return e.return(Ci(d,["LogsRequestsStore"],{mode:"readwrite",I:!0},function(f){var g=Di(f,"LogsRequestsStore");return g.get(a).then(function(h){if(h)return h.status="QUEUED",V(g.h.put(h,void 0)).then(function(){return h})})}))})})}
function wj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,qj(),2);d=e.i;return e.return(Ci(d,["LogsRequestsStore"],{mode:"readwrite",I:!0},function(f){var g=Di(f,"LogsRequestsStore");return g.get(a).then(function(h){return h?(h.status="NEW",h.sendCount+=1,V(g.h.put(h,void 0)).then(function(){return h})):oj.resolve(void 0)})}))})})}
function xj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,qj(),2);d=e.i;return e.return(d.delete("LogsRequestsStore",a))})})}
function yj(){return H(this,function b(){var c;return x(b,function(d){if(1==d.h)return w(d,qj(),2);c=d.i;return d.return(c.clear("LogsRequestsStore"))})})}
function zj(){return H(this,function b(){var c;return x(b,function(d){if(1==d.h)return w(d,qj(),2);c=d.i;return d.return(c.clear("SWHealthLog"))})})}
function Aj(){return H(this,function b(){var c,d;return x(b,function(e){return 1==e.h?w(e,qj(),2):3!=e.h?(c=e.i,d=R()-2592E6,w(e,Ci(c,["LogsRequestsStore"],{mode:"readwrite",I:!0},function(f){return Mi(Di(f,"LogsRequestsStore"),{},function(g){if(g.getValue().timestamp<=d)return g.delete().then(function(){return g.continue()})})}),3)):Q("web_clean_sw_logs_store")?w(e,Ci(c,["SWHealthLog"],{mode:"readwrite",
I:!0},function(f){return Mi(Di(f,"SWHealthLog"),{},function(g){if(g.getValue().timestamp<=d)return g.delete().then(function(){return g.continue()})})}),0):e.A(0)})})}
function Bj(){return H(this,function b(){return x(b,function(c){return 1==c.h?w(c,kj(),2):w(c,lj("LogsDatabaseV2"),0)})})}
function sj(){return H(this,function b(){var c;return x(b,function(d){if(1==d.h){Wh.h||(Wh.h=new Wh);var e={};var f=fd([]);f&&(e.Authorization=f,f=void 0,void 0===f&&(f=Number(F("SESSION_INDEX",0)),f=isNaN(f)?0:f),e["X-Goog-AuthUser"]=f,"INNERTUBE_HOST_OVERRIDE"in mf||(e["X-Origin"]=window.location.origin),Q("pageid_as_header_web")&&"DELEGATED_SESSION_ID"in mf&&(e["X-Goog-PageId"]=F("DELEGATED_SESSION_ID")));e instanceof Ce||(f=new Ce(Ga),De(f,2,e),e=f);return w(d,e,2)}c=d.i;e=d.return;f=Ch(c);var g=
new xd;g.update(JSON.stringify(f,Object.keys(f).sort()));f=g.digest();g="";for(var h=0;h<f.length;h++)g+="0123456789ABCDEF".charAt(Math.floor(f[h]/16))+"0123456789ABCDEF".charAt(f[h]%16);return e.call(d,g)})})}
function Cj(a){return H(this,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,qj(),2);d=e.i;return w(e,Gi(d,"sapisid",a,"sapisid"),0)})})}
function Dj(){return H(this,function b(){var c,d;return x(b,function(e){if(1==e.h)return w(e,qj(),2);if(3!=e.h)return c=e.i,w(e,c.get("sapisid","sapisid"),3);d=e.i;return e.return(d||"")})})}
function tj(a){var b=vf("nwl_latency_sampling_rate",.01);.02<b||Math.random()<=b&&Ph("nwl_transaction_latency_payload",a)}
;var Ej=["__Secure-1PAPISID","SAPISID","__Secure-3PAPISID"];function Fj(){for(var a=u(Ej),b=a.next();!b.done;b=a.next())if(b=cd.get(b.value))return b;return"LOGGED_OUT"}
function Gj(){se.call(this);this.pollingInterval=3E3;this.i=[null,null,null];this.m=!1;Hj(this)}
v(Gj,se);function Ij(){Gj.h||(Gj.h=new Gj);var a=Gj.h;a.m=!0;a.verifyUser();Jj(a)}
Gj.prototype.verifyUser=function(){var a=Hj(this),b=a.Za;if(!a.ob)return Jj(this),!0;te(this,"ytsessionchange");b&&te(this,"ytuserinvalid");Jj(this);return!1};
function Hj(a){var b=Ej.map(function(e){var f;return null!==(f=cd.get(e))&&void 0!==f?f:""}),c=b.some(function(e,f){return a.i&&""!==a.i[f]&&""===e}),d=b.some(function(e,f){return a.i&&a.i[f]!==e});
a.i=b;return{Za:c,ob:d}}
function Jj(a){a.m&&(Kj(a),a.l=Lf(function(){a.verifyUser()},a.pollingInterval))}
function Kj(a){a.l&&(Qf(a.l),a.l=void 0)}
;var Lj;function Mj(){Lj||(Lj=new Dh("yt.offline"));return Lj}
function Nj(a){if(Q("offline_error_handling")){var b=Mj().get("errors",!0)||{};b[a.message]={name:a.name,stack:a.stack};a.level&&(b[a.message].level=a.level);Mj().set("errors",b,2592E3,!0)}}
function Oj(){if(Q("offline_error_handling")){var a=Mj().get("errors",!0);if(a){for(var b in a)if(a[b]){var c=new fi(b,"sent via offline_errors");c.name=a[b].name;c.stack=a[b].stack;c.level=a[b].level;qf(c)}Mj().set("errors",{},2592E3,!0)}}}
;var Pj=vf("network_polling_interval",3E4);function Qj(){se.call(this);this.K=0;this.o=this.l=!1;this.B=0;this.m=this.J=!1;this.i=Rj();this.m=Q("validate_network_status");Sj(this);Tj(this)}
v(Qj,se);function Uj(a,b){a.l=!0;if(void 0===b?0:b)a.K||Vj(a)}
function Rj(){var a=window.navigator.onLine;return void 0===a?!0:a}
function Tj(a){window.addEventListener("online",function(){return H(a,function c(){var d=this;return x(c,function(e){if(1==e.h)return d.m?w(e,Wj(d),2):(d.i=!0,d.l&&te(d,"ytnetworkstatus-online"),e.A(2));Xj(d);d.J&&Oj();e.h=0})})})}
function Sj(a){window.addEventListener("offline",function(){return H(a,function c(){var d=this;return x(c,function(e){if(1==e.h)return d.m?w(e,Wj(d),2):(d.i=!1,d.l&&te(d,"ytnetworkstatus-offline"),e.A(2));Xj(d);e.h=0})})})}
function Vj(a){a.K=Lf(function(){return H(a,function c(){var d=this;return x(c,function(e){if(1==e.h){if(Q("trigger_nsm_validation_checks_with_nwl")&&!d.i)return w(e,Wj(d),3);if(Rj()){if(!1!==d.i)return e.A(3);d.o=!0;d.B=R();return d.l?d.m?w(e,Wj(d),11):(d.i=!0,te(d,"ytnetworkstatus-online"),e.A(11)):e.A(11)}if(!0!==d.i)return e.A(3);d.o=!0;d.B=R();return d.l?d.m?w(e,Wj(d),3):(d.i=!1,te(d,"ytnetworkstatus-offline"),e.A(3)):e.A(3)}if(3!=e.h)return d.J&&Oj(),e.A(3);Vj(d);e.h=0})})},Pj)}
function Xj(a){a.o&&(rf(new fi("NetworkStatusManager state did not match poll",R()-a.B)),a.o=!1)}
function Wj(a,b){return a.C?a.C:a.C=new Promise(function(c){return H(a,function e(){var f,g,h,k=this;return x(e,function(l){switch(l.h){case 1:return f=new AbortController,g=f.signal,h=!1,ta(l,2,3),k.L=Nf(function(){f.abort()},b||2E4),w(l,fetch("/generate_204",{method:"HEAD",
signal:g}),5);case 5:h=!0;case 3:va(l);k.C=void 0;Qf(k.L);h!==k.i&&(k.i=h,k.i&&k.l?te(k,"ytnetworkstatus-online"):k.l&&te(k,"ytnetworkstatus-offline"));c(h);wa(l);break;case 2:ua(l),h=!1,l.A(3)}})})})}
;function Yj(a){a=void 0===a?{}:a;se.call(this);var b=this;this.l=this.o=0;Qj.h||(Qj.h=new Qj);this.i=Qj.h;Uj(this.i,a.Na);a.Ya&&(this.i.J=!0);a.ia?(this.ia=a.ia,je(this.i,"ytnetworkstatus-online",function(){Zj(b,"publicytnetworkstatus-online")}),je(this.i,"ytnetworkstatus-offline",function(){Zj(b,"publicytnetworkstatus-offline")})):(je(this.i,"ytnetworkstatus-online",function(){te(b,"publicytnetworkstatus-online")}),je(this.i,"ytnetworkstatus-offline",function(){te(b,"publicytnetworkstatus-offline")}))}
v(Yj,se);function ak(){var a=bk().i;a.m||a.i===Rj()||rf(new fi("NetworkStatusManager isOnline does not match window status"));return a.i}
function ck(){var a=bk();return H(a,function c(){var d=this;return x(c,function(e){return e.return(Wj(d.i,void 0))})})}
function Zj(a,b){a.ia?a.l?(Qf(a.o),a.o=Nf(function(){a.m!==b&&(te(a,b),a.m=b,a.l=R())},a.ia-(R()-a.l))):(te(a,b),a.m=b,a.l=R()):te(a,b)}
;var dk=!1,ek=!1,fk=0,gk=0,hk;function ik(){H(this,function b(){var c,d,e,f;return x(b,function(g){switch(g.h){case 1:return w(g,cj(),2);case 2:(c=g.i)&&(ek=!0);d=Q("networkless_logging");if(c&&d)return Q("nwl_use_ytidb_partitioning")?w(g,lj("LogsDatabaseV2"),8):w(g,kj(),8);if(!c){g.A(0);break}return w(g,Bj(),0);case 8:return Ij(),document.addEventListener("ytsessionchange",function(){jk()}),w(g,Dj(),11);
case 11:e=g.i;f=Fj();if(e===f){g.A(12);break}jk();return w(g,Cj(f),12);case 12:if(!(Q("enable_nwl_cleaning_logic")&&Math.random()<=vf("nwl_cleaning_rate",.1))){g.A(14);break}return w(g,Aj(),14);case 14:dk=!0;kk();ak()&&lk();je(bk(),"publicytnetworkstatus-online",lk);je(bk(),"publicytnetworkstatus-offline",mk);if(!Q("networkless_immediately_drop_sw_health_store")){g.A(16);break}return w(g,nk(),16);case 16:if(Q("networkless_immediately_drop_all_requests"))return w(g,Bj(),0);g.A(0)}})})}
function ok(a,b){function c(d){var e=ak();if(!dk||!d||e&&Q("vss_networkless_bypass_write"))pk(a,b);else{var f={url:a,options:b,timestamp:R(),status:"NEW",sendCount:0};rj(f).then(function(g){f.id=g;(ak()||Q("networkless_always_online"))&&qk(f)}).catch(function(g){qk(f);
ak()?qf(g):Nj(g)})}}
b=void 0===b?{}:b;Q("skip_is_supported_killswitch")?cj().then(function(d){c(d)}):c(ek)}
function rk(a,b){function c(d){if(dk&&d){var e={url:a,options:b,timestamp:R(),status:"NEW",sendCount:0},f=!1,g=b.onSuccess?b.onSuccess:function(){};
e.options.onSuccess=function(h,k){void 0!==e.id?xj(e.id):f=!0;g(h,k)};
pk(e.url,e.options);rj(e).then(function(h){e.id=h;f&&xj(e.id)}).catch(function(h){ak()?qf(h):Nj(h)})}else pk(a,b)}
b=void 0===b?{}:b;Q("skip_is_supported_killswitch")?cj().then(function(d){c(d)}):c(ek)}
function lk(){var a=this;fk||(fk=Nf(function(){return H(a,function c(){var d;return x(c,function(e){if(1==e.h)return w(e,uj("NEW"),2);if(3!=e.h)return d=e.i,d?w(e,qk(d),3):(mk(),e.return());fk=0;lk();e.h=0})})},100))}
function mk(){Qf(fk);fk=0}
function qk(a){return H(this,function c(){var d;return x(c,function(e){switch(e.h){case 1:if(void 0===a.id){e.A(2);break}return w(e,vj(a.id),3);case 3:(d=e.i)?a=d:rf(Error("The request cannot be found in the database."));case 2:if(sk(a,2592E6)){e.A(4);break}rf(Error("Networkless Logging: Stored logs request expired age limit"));if(void 0===a.id){e.A(5);break}return w(e,xj(a.id),5);case 5:return e.return();case 4:var f=a=tk(a),g,h;if(null===(h=null===(g=null===f||void 0===f?void 0:f.options)||void 0===
g?void 0:g.postParams)||void 0===h?0:h.requestTimeMs)f.options.postParams.requestTimeMs=Math.round(R());(a=f)&&pk(a.url,a.options);e.h=0}})})}
function tk(a){var b=this,c=a.options.onError?a.options.onError:function(){};
a.options.onError=function(e,f){return H(b,function h(){return x(h,function(k){switch(k.h){case 1:if(!(Q("trigger_nsm_validation_checks_with_nwl")&&gk<=vf("potential_esf_error_limit",10))){k.A(2);break}return w(k,ck(),3);case 3:if(ak())gk++;else return c(e,f),k.return();case 2:if(void 0===(null===a||void 0===a?void 0:a.id)){k.A(4);break}return 1>a.sendCount?w(k,wj(a.id),8):w(k,xj(a.id),4);case 8:Nf(function(){ak()&&lk()},5E3);
case 4:c(e,f),k.h=0}})})};
var d=a.options.onSuccess?a.options.onSuccess:function(){};
a.options.onSuccess=function(e,f){return H(b,function h(){return x(h,function(k){if(1==k.h)return void 0===(null===a||void 0===a?void 0:a.id)?k.A(2):w(k,xj(a.id),2);d(e,f);k.h=0})})};
return a}
function sk(a,b){a=a.timestamp;return R()-a>=b?!1:!0}
function kk(){var a=this;uj("QUEUED").then(function(b){b&&!sk(b,12E4)&&Nf(function(){return H(a,function d(){return x(d,function(e){if(1==e.h)return void 0===b.id?e.A(2):w(e,wj(b.id),2);kk();e.h=0})})})})}
function jk(){yj().catch(function(a){qf(a)})}
function nk(){return H(this,function b(){return x(b,function(c){return c.return(zj().catch(function(d){qf(d)}))})})}
function bk(){hk||(hk=new Yj({Ya:!0,Na:Q("trigger_nsm_validation_checks_with_nwl")}));return hk}
function pk(a,b){if(Q("networkless_with_beacon")){var c=["method","postBody"];if(Object.keys(b).length>c.length)var d=!0;else{d=0;c=u(c);for(var e=c.next();!e.done;e=c.next())b.hasOwnProperty(e.value)&&d++;d=Object.keys(b).length!==d}d?sg(a,b):Hg(a,void 0,b.postBody)}else sg(a,b)}
;function uk(a){var b=this;this.h=null;a?this.h=a:Ah()&&(this.h=kh());Lf(function(){Ih(b)},5E3)}
uk.prototype.isReady=function(){!this.h&&Ah()&&(this.h=kh());return!!this.h};
function nh(a,b,c,d){function e(r){r=void 0===r?!1:r;var q;if(d.retry&&"www.youtube-nocookie.com"!=h&&(r||(q=Gh(b,c,l,k)),q)){var E=g.onSuccess,I=g.onFetchSuccess;g.onSuccess=function(J,ba){Hh(q);E(J,ba)};
c.onFetchSuccess=function(J,ba){Hh(q);I(J,ba)}}try{r&&d.retry&&!d.Ea.bypassNetworkless?(g.method="POST",!d.Ea.writeThenSend&&Q("nwl_send_fast_on_unload")?rk(n,g):ok(n,g)):(g.method="POST",g.postParams||(g.postParams={}),sg(n,g))}catch(J){if("InvalidAccessError"==J.name)q&&(Hh(q),q=0),rf(Error("An extension is blocking network request."));
else throw J;}q&&Lf(function(){Ih(a)},5E3)}
!F("VISITOR_DATA")&&"visitor_id"!==b&&.01>Math.random()&&rf(new fi("Missing VISITOR_DATA when sending innertube request.",b,c,d));if(!a.isReady()){var f=new fi("innertube xhrclient not ready",b,c,d);qf(f);throw f;}var g={headers:{"Content-Type":"application/json"},method:"POST",postParams:c,postBodyFormat:"JSON",onTimeout:function(){d.onTimeout()},
onFetchTimeout:d.onTimeout,onSuccess:function(r,q){if(d.onSuccess)d.onSuccess(q)},
onFetchSuccess:function(r){if(d.onSuccess)d.onSuccess(r)},
onError:function(r,q){if(d.onError)d.onError(q)},
onFetchError:function(r){if(d.onError)d.onError(r)},
timeout:d.timeout,withCredentials:!0},h="";(f=a.h.Va)&&(h=f);var k=a.h.Xa||!1,l=Bh(k,h,d);Object.assign(g.headers,l);g.headers.Authorization&&!h&&(g.headers["x-origin"]=window.location.origin);f="/youtubei/"+a.h.innertubeApiVersion+"/"+b;var p={alt:"json"};a.h.Wa&&g.headers.Authorization||(p.key=a.h.innertubeApiKey);var n=gg(""+h+f,p||{},!0);dk?cj().then(function(r){e(r)}):e(!1)}
;function vk(a,b,c){c=void 0===c?{}:c;var d=uk;F("ytLoggingEventsDefaultDisabled",!1)&&uk==uk&&(d=null);ph(a,b,d,c)}
;var wk=[{Ca:function(a){return"Cannot read property '"+a.key+"'"},
sa:{TypeError:[{regexp:/Cannot read property '([^']+)' of (null|undefined)/,groups:["key","value"]},{regexp:/\u65e0\u6cd5\u83b7\u53d6\u672a\u5b9a\u4e49\u6216 (null|undefined) \u5f15\u7528\u7684\u5c5e\u6027\u201c([^\u201d]+)\u201d/,groups:["value","key"]},{regexp:/\uc815\uc758\ub418\uc9c0 \uc54a\uc74c \ub610\ub294 (null|undefined) \ucc38\uc870\uc778 '([^']+)' \uc18d\uc131\uc744 \uac00\uc838\uc62c \uc218 \uc5c6\uc2b5\ub2c8\ub2e4./,groups:["value","key"]},{regexp:/No se puede obtener la propiedad '([^']+)' de referencia nula o sin definir/,
groups:["key"]},{regexp:/Unable to get property '([^']+)' of (undefined or null) reference/,groups:["key","value"]}],Error:[{regexp:/(Permission denied) to access property "([^']+)"/,groups:["reason","key"]}]}},{Ca:function(a){return"Cannot call '"+a.key+"'"},
sa:{TypeError:[{regexp:/(?:([^ ]+)?\.)?([^ ]+) is not a function/,groups:["base","key"]},{regexp:/([^ ]+) called on (null or undefined)/,groups:["key","value"]},{regexp:/Object (.*) has no method '([^ ]+)'/,groups:["base","key"]},{regexp:/Object doesn't support property or method '([^ ]+)'/,groups:["key"]},{regexp:/\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u306f '([^']+)' \u30d7\u30ed\u30d1\u30c6\u30a3\u307e\u305f\u306f\u30e1\u30bd\u30c3\u30c9\u3092\u30b5\u30dd\u30fc\u30c8\u3057\u3066\u3044\u307e\u305b\u3093/,
groups:["key"]},{regexp:/\uac1c\uccb4\uac00 '([^']+)' \uc18d\uc131\uc774\ub098 \uba54\uc11c\ub4dc\ub97c \uc9c0\uc6d0\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4./,groups:["key"]}]}}];var yk={R:[],P:[{wa:xk,weight:500}]};function xk(a){a=a.stack;return a.includes("chrome://")||a.includes("chrome-extension://")||a.includes("moz-extension://")}
;function zk(){this.P=[];this.R=[]}
var Ak;function Bk(){if(!Ak){var a=Ak=new zk;a.R.length=0;a.P.length=0;yk.R&&a.R.push.apply(a.R,yk.R);yk.P&&a.P.push.apply(a.P,yk.P)}return Ak}
;var Ck=new M;function Dk(a){function b(){return a.charCodeAt(d++)}
var c=a.length,d=0;do{var e=Ek(b);if(Infinity===e)break;var f=e>>3;switch(e&7){case 0:e=Ek(b);if(2===f)return e;break;case 1:if(2===f)return;d+=8;break;case 2:e=Ek(b);if(2===f)return a.substr(d,e);d+=e;break;case 5:if(2===f)return;d+=4;break;default:return}}while(d<c)}
function Ek(a){var b=a(),c=b&127;if(128>b)return c;b=a();c|=(b&127)<<7;if(128>b)return c;b=a();c|=(b&127)<<14;if(128>b)return c;b=a();return 128>b?c|(b&127)<<21:Infinity}
;function Fk(a,b,c,d){if(a)if(Array.isArray(a)){var e=d;for(d=0;d<a.length&&!(a[d]&&(e+=Gk(d,a[d],b,c),500<e));d++);d=e}else if("object"===typeof a)for(e in a){if(a[e]){var f=e;var g=a[e],h=b,k=c;f="string"!==typeof g||"clickTrackingParams"!==f&&"trackingParams"!==f?0:(g=Dk(atob(g.replace(/-/g,"+").replace(/_/g,"/"))))?Gk(f+".ve",g,h,k):0;d+=f;d+=Gk(e,a[e],b,c);if(500<d)break}}else c[b]=Hk(a),d+=c[b].length;else c[b]=Hk(a),d+=c[b].length;return d}
function Gk(a,b,c,d){c+="."+a;a=Hk(b);d[c]=a;return c.length+a.length}
function Hk(a){return("string"===typeof a?a:String(JSON.stringify(a))).substr(0,500)}
;var Ik=new Set,Jk=0,Kk=0,Lk=0,Mk=[],Nk=["PhantomJS","Googlebot","TO STOP THIS SECURITY SCAN go/scan"];function Ok(a){Pk(a,"WARNING")}
function Pk(a,b,c,d,e,f){f=void 0===f?{}:f;f.name=c||F("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||F("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0);c=f||{};b=void 0===b?"ERROR":b;b=void 0===b?"ERROR":b;if(a&&(a.hasOwnProperty("level")&&a.level&&(b=a.level),Q("console_log_js_exceptions")&&(d=[],d.push("Name: "+a.name),d.push("Message: "+a.message),a.hasOwnProperty("params")&&d.push("Error Params: "+JSON.stringify(a.params)),a.hasOwnProperty("args")&&d.push("Error args: "+JSON.stringify(a.args)),d.push("File name: "+
a.fileName),d.push("Stacktrace: "+a.stack),window.console.log(d.join("\n"),a)),!(5<=Jk))){var g=zd(a);d=g.message||"Unknown Error";e=g.name||"UnknownError";var h=g.stack||a.i||"Not available";h.startsWith(e+": "+d)&&(f=h.split("\n"),f.shift(),h=f.join("\n"));f=g.lineNumber||"Not available";g=g.fileName||"Not available";var k=0;if(a.hasOwnProperty("args")&&a.args&&a.args.length)for(var l=0;l<a.args.length&&!(k=Fk(a.args[l],"params."+l,c,k),500<=k);l++);else if(a.hasOwnProperty("params")&&a.params){var p=
a.params;if("object"===typeof a.params)for(l in p){if(p[l]){var n="params."+l,r=Hk(p[l]);c[n]=r;k+=n.length+r.length;if(500<k)break}}else c.params=Hk(p)}if(Mk.length)for(l=0;l<Mk.length&&!(k=Fk(Mk[l],"params.context."+l,c,k),500<=k);l++);navigator.vendor&&!c.hasOwnProperty("vendor")&&(c["device.vendor"]=navigator.vendor);l={message:d,name:e,lineNumber:f,fileName:g,stack:h,params:c,sampleWeight:1};c=Number(a.columnNumber);isNaN(c)||(l.lineNumber=l.lineNumber+":"+c);if("IGNORED"===a.level)a=0;else a:{a=
Bk();c=u(a.R);for(d=c.next();!d.done;d=c.next())if(d=d.value,l.message&&l.message.match(d.Mk)){a=d.weight;break a}a=u(a.P);for(c=a.next();!c.done;c=a.next())if(c=c.value,c.wa(l)){a=c.weight;break a}a=1}l.sampleWeight=a;a=u(wk);for(c=a.next();!c.done;c=a.next())if(c=c.value,c.sa[l.name])for(e=u(c.sa[l.name]),d=e.next();!d.done;d=e.next())if(f=d.value,d=l.message.match(f.regexp)){l.params["params.error.original"]=d[0];e=f.groups;f={};for(g=0;g<e.length;g++)f[e[g]]=d[g+1],l.params["params.error."+e[g]]=
d[g+1];l.message=c.Ca(f);break}l.params||(l.params={});a=Bk();l.params["params.errorServiceSignature"]="msg="+a.R.length+"&cb="+a.P.length;l.params["params.serviceWorker"]="false";y.document&&y.document.querySelectorAll&&(l.params["params.fscripts"]=String(document.querySelectorAll("script:not([nonce])").length));window.yterr&&"function"===typeof window.yterr&&window.yterr(l);if(0!==l.sampleWeight&&!Ik.has(l.message)){"ERROR"===b?(Ck.U("handleError",l),Q("record_app_crashed_web")&&0===Lk&&1===l.sampleWeight&&
(Lk++,vk("appCrashed",{appCrashType:"APP_CRASH_TYPE_BREAKPAD"})),Kk++):"WARNING"===b&&Ck.U("handleWarning",l);if(Q("kevlar_gel_error_routing")){a=b;b:{c=u(Nk);for(d=c.next();!d.done;d=c.next())if(Bg(d.value.toLowerCase())){c=!0;break b}c=!1}if(c)c=void 0;else{d={stackTrace:l.stack};l.fileName&&(d.filename=l.fileName);c=l.lineNumber&&l.lineNumber.split?l.lineNumber.split(":"):[];0!==c.length&&(1!==c.length||isNaN(Number(c[0]))?2!==c.length||isNaN(Number(c[0]))||isNaN(Number(c[1]))||(d.lineNumber=Number(c[0]),
d.columnNumber=Number(c[1])):d.lineNumber=Number(c[0]));c={level:"ERROR_LEVEL_UNKNOWN",message:l.message,errorClassName:l.name,sampleWeight:l.sampleWeight};"ERROR"===a?c.level="ERROR_LEVEL_ERROR":"WARNING"===a&&(c.level="ERROR_LEVEL_WARNNING");d={isObfuscated:!0,browserStackInfo:d};e={pageUrl:window.location.href,kvPairs:[]};F("FEXP_EXPERIMENTS")&&(e.experimentIds=F("FEXP_EXPERIMENTS"));if(f=l.params)for(g=u(Object.keys(f)),h=g.next();!h.done;h=g.next())h=h.value,e.kvPairs.push({key:"client."+h,value:String(f[h])});
f=F("SERVER_NAME",void 0);g=F("SERVER_VERSION",void 0);f&&g&&(e.kvPairs.push({key:"server.name",value:f}),e.kvPairs.push({key:"server.version",value:g}));c={errorMetadata:e,stackTrace:d,logMessage:c}}c&&(vk("clientError",c),("ERROR"===a||Q("errors_flush_gel_always_killswitch"))&&fh())}if(!Q("suppress_error_204_logging")){a=l.params||{};b={urlParams:{a:"logerror",t:"jserror",type:l.name,msg:l.message.substr(0,250),line:l.lineNumber,level:b,"client.name":a.name},postParams:{url:F("PAGE_NAME",window.location.href),
file:l.fileName},method:"POST"};a.version&&(b["client.version"]=a.version);if(b.postParams){l.stack&&(b.postParams.stack=l.stack);c=u(Object.keys(a));for(d=c.next();!d.done;d=c.next())d=d.value,b.postParams["client."+d]=a[d];if(a=F("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(c=u(Object.keys(a)),d=c.next();!d.done;d=c.next())d=d.value,b.postParams[d]=a[d];a=F("SERVER_NAME",void 0);c=F("SERVER_VERSION",void 0);a&&c&&(b.postParams["server.name"]=a,b.postParams["server.version"]=c)}sg(F("ECATCHER_REPORT_HOST",
"")+"/error_204",b)}Ik.add(l.message);Jk++}}}
function Qk(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];a.args||(a.args=[]);a.args.push.apply(a.args,c instanceof Array?c:ha(u(c)))}
;var Rk={Xb:29434,ac:3611,Qe:3854,kg:42993,Si:4724,Dj:96370,rb:27686,sb:85013,tb:23462,vb:42016,wb:62407,xb:26926,ub:43781,yb:51236,zb:79148,Ab:50160,Bb:77504,Nb:87907,Ob:18630,Pb:54445,Qb:80935,Rb:105675,Sb:37521,Tb:47786,Ub:98349,Vb:123695,Wb:6827,Yb:7282,Zb:124448,ec:32276,dc:76278,fc:93911,hc:106531,ic:27259,jc:27262,kc:27263,mc:21759,nc:27107,oc:62936,pc:49568,qc:38408,sc:80637,tc:68727,uc:68728,wc:80353,xc:80356,yc:74610,zc:45707,Ac:83962,Bc:83970,Cc:46713,Dc:89711,Ec:74612,Fc:93265,Gc:74611,
Ic:113533,Jc:93252,Kc:99357,Mc:94521,Nc:114252,Oc:113532,Pc:94522,Lc:94583,Qc:88E3,Rc:93253,Sc:93254,Tc:94387,Uc:94388,Vc:93255,Wc:97424,Hc:72502,Xc:110111,Yc:76019,bd:117092,cd:117093,Zc:89431,dd:110466,ed:77240,fd:60508,gd:105350,hd:73393,jd:113534,kd:92098,ld:84517,md:83759,nd:80357,od:86113,pd:72598,qd:72733,rd:107349,sd:124275,td:118203,ud:117431,vd:117429,wd:117430,xd:117432,yd:120080,zd:117259,Ad:121692,Bd:97615,Cd:31402,Dd:84774,Ed:95117,Fd:98930,Gd:98931,Hd:98932,Id:43347,Jd:45474,Kd:100352,
Ld:84758,Md:98443,Nd:117985,Od:74613,Pd:74614,Qd:64502,Rd:74615,Sd:74616,Td:122224,Ud:74617,Vd:77820,Wd:74618,Xd:93278,Yd:93274,Zd:93275,ae:93276,be:22110,ce:29433,ee:120541,he:82047,ie:113550,je:75836,ke:75837,le:42352,me:84512,ne:76065,oe:75989,pe:16623,qe:32594,re:27240,se:32633,te:74858,we:3945,ue:16989,xe:45520,ye:25488,ze:25492,Ae:25494,Be:55760,Ce:14057,De:18451,Ee:57204,Fe:57203,Ge:17897,He:57205,Ie:18198,Je:17898,Ke:17909,Le:43980,Me:46220,Ne:11721,Oe:49954,Pe:96369,Re:56251,Se:25624,Te:16906,
Ue:99999,Ve:68172,We:27068,Xe:47973,Ye:72773,Ze:26970,af:26971,bf:96805,cf:17752,df:73233,ef:109512,ff:22256,gf:14115,hf:22696,jf:89278,kf:89277,lf:109513,mf:43278,nf:43459,pf:43464,qf:89279,rf:43717,sf:55764,tf:22255,uf:89281,vf:40963,wf:43277,xf:43442,yf:91824,zf:120137,Af:96367,Bf:36850,Cf:72694,Df:37414,Ef:36851,Gf:124863,Ff:121343,Hf:73491,If:54473,Jf:43375,Kf:46674,Lf:32473,Mf:72901,Nf:72906,Of:50947,Pf:50612,Qf:50613,Rf:50942,Sf:84938,Tf:84943,Uf:84939,Vf:84941,Wf:84944,Xf:84940,Yf:84942,Zf:35585,
ag:51926,cg:79983,dg:63238,eg:18921,fg:63241,gg:57893,hg:41182,ig:33424,jg:22207,lg:36229,mg:22206,ng:22205,og:18993,pg:19001,qg:18990,rg:18991,sg:18997,tg:18725,ug:19003,vg:36874,wg:44763,xg:33427,yg:67793,zg:22182,Ag:37091,Bg:34650,Cg:50617,Dg:47261,Eg:22287,Fg:25144,Gg:97917,Hg:62397,Ig:36961,Jg:108035,Kg:27426,Lg:27857,Mg:27846,Ng:27854,Og:69692,Pg:61411,Qg:39299,Rg:38696,Sg:62520,Tg:36382,Ug:108701,Vg:50663,Wg:36387,Xg:14908,Yg:37533,Zg:105443,ah:61635,bh:62274,dh:65702,eh:65703,fh:65701,gh:76256,
hh:37671,ih:49953,kh:36216,lh:28237,mh:39553,nh:29222,oh:26107,ph:38050,qh:26108,sh:120745,rh:26109,th:26110,uh:66881,vh:28236,wh:14586,xh:57929,yh:74723,zh:44098,Ah:44099,Bh:23528,Ch:61699,Dh:59149,Eh:101951,Fh:97346,Gh:118051,Hh:95102,Ih:64882,Jh:119505,Kh:63595,Lh:63349,Mh:95101,Nh:75240,Oh:27039,Ph:68823,Qh:21537,Rh:83464,Sh:75707,Th:83113,Uh:101952,Vh:101953,Xh:79610,Yh:24402,Zh:24400,ai:32925,bi:57173,ci:122502,di:64423,fi:64424,gi:33986,hi:100828,ii:21409,ji:11070,ki:11074,li:17880,mi:14001,
oi:30709,ri:30707,si:30711,ti:30710,vi:30708,ni:26984,wi:63648,xi:63649,yi:51879,zi:111059,Ai:5754,Bi:20445,Ci:110386,Di:113746,Ei:66557,Fi:17310,Gi:28631,Hi:21589,Ii:68012,Ji:60480,Ki:31571,Li:76980,Mi:41577,Ni:45469,Oi:38669,Pi:13768,Qi:13777,Ri:62985,Ti:59369,Ui:43927,Vi:43928,Wi:12924,Xi:100355,aj:56219,bj:27669,cj:10337,Zi:47896,dj:122629,ej:121258,fj:107598,gj:96639,hj:107536,ij:96661,jj:96658,kj:116646,lj:121122,mj:96660,nj:104443,oj:96659,pj:106442,qj:63667,rj:63668,sj:63669,tj:78314,uj:55761,
vj:96368,wj:67374,xj:48992,yj:49956,zj:31961,Aj:26388,Bj:23811,Cj:5E4,Ej:47355,Fj:47356,Gj:37935,Hj:45521,Ij:21760,Jj:83769,Kj:49977,Lj:49974,Mj:93497,Nj:93498,Oj:34325,Pj:115803,Qj:123707,Rj:100081,Sj:35309,Tj:68314,Uj:25602,Vj:100339,Wj:59018,Xj:18248,Yj:50625,Zj:9729,ak:37168,bk:37169,ck:21667,dk:16749,ek:18635,fk:39305,gk:18046,hk:53969,ik:8213,jk:93926,kk:102852,lk:110099,mk:22678,nk:69076,qk:100856,rk:17736,sk:3832,tk:55759,uk:64031,vk:93044,wk:93045,xk:34388,yk:17657,zk:17655,Ak:39579,Bk:39578,
Ck:77448,Dk:8196,Ek:11357,Fk:69877,Gk:8197,Hk:82039};function Sk(a,b,c){L.call(this);var d=this;c=c||F("POST_MESSAGE_ORIGIN",void 0)||window.document.location.protocol+"//"+window.document.location.hostname;this.j=b||null;this.C="*";this.l=c;this.sessionId=null;this.channel="widget";this.F=!!a;this.B=function(e){a:if(!("*"!=d.l&&e.origin!=d.l||d.j&&e.source!=d.j||"string"!==typeof e.data)){try{var f=JSON.parse(e.data)}catch(g){break a}if(!(null==f||d.F&&(d.sessionId&&d.sessionId!=f.id||d.channel&&d.channel!=f.channel))&&f)switch(f.event){case "listening":"null"!=
e.origin&&(d.l=d.C=e.origin);d.j=e.source;d.sessionId=f.id;d.i&&(d.i(),d.i=null);break;case "command":d.m&&(!d.o||0<=Wa(d.o,f.func))&&d.m(f.func,f.args,e.origin)}}};
this.o=this.i=this.m=null;window.addEventListener("message",this.B)}
v(Sk,L);Sk.prototype.sendMessage=function(a,b){if(b=b||this.j){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var c=JSON.stringify(a);b.postMessage(c,this.C)}catch(d){rf(d)}}};
Sk.prototype.D=function(){window.removeEventListener("message",this.B);L.prototype.D.call(this)};function Tk(){this.l=[];this.isReady=!1;this.u={};var a=this.i=new Sk(!!F("WIDGET_ID_ENFORCE")),b=this.fb.bind(this);a.m=b;a.o=null;this.i.channel="widget";if(a=F("WIDGET_ID"))this.i.sessionId=a}
m=Tk.prototype;m.fb=function(a,b,c){"addEventListener"===a&&b?(a=b[0],this.u[a]||"onReady"===a||(this.addEventListener(a,Uk(this,a)),this.u[a]=!0)):this.ta(a,b,c)};
m.ta=function(){};
function Uk(a,b){return function(c){return a.sendMessage(b,c)}}
m.addEventListener=function(){};
m.Pa=function(){this.isReady=!0;this.sendMessage("initialDelivery",this.na());this.sendMessage("onReady");D(this.l,this.Ha,this);this.l=[]};
m.na=function(){return null};
function Vk(a,b){a.sendMessage("infoDelivery",b)}
m.Ha=function(a){this.isReady?this.i.sendMessage(a):this.l.push(a)};
m.sendMessage=function(a,b){this.Ha({event:a,info:void 0===b?null:b})};
m.dispose=function(){this.i=null};function Wk(a){return(0===a.search("cue")||0===a.search("load"))&&"loadModule"!==a}
function Xk(a,b,c){"string"===typeof a&&(a={mediaContentUrl:a,startSeconds:b,suggestedQuality:c});a:{if((b=a.mediaContentUrl)&&(b=/\/([ve]|embed)\/([^#?]+)/.exec(b))&&b[2]){b=b[2];break a}b=null}a.videoId=b;return Yk(a)}
function Yk(a,b,c){if("string"===typeof a)return{videoId:a,startSeconds:b,suggestedQuality:c};b=["endSeconds","startSeconds","mediaContentUrl","suggestedQuality","videoId"];c={};for(var d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}
function Zk(a,b,c,d){if(Ka(a)&&!Array.isArray(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};"string"===typeof a&&16===a.length?b.list="PL"+a:b.playlist=a;return b}
;function $k(a){Tk.call(this);this.h=a;this.j=[];this.addEventListener("onReady",B(this.bb,this));this.addEventListener("onVideoProgress",B(this.lb,this));this.addEventListener("onVolumeChange",B(this.mb,this));this.addEventListener("onApiChange",B(this.gb,this));this.addEventListener("onPlaybackQualityChange",B(this.ib,this));this.addEventListener("onPlaybackRateChange",B(this.jb,this));this.addEventListener("onStateChange",B(this.kb,this));this.addEventListener("onWebglSettingsChanged",B(this.nb,
this))}
v($k,Tk);m=$k.prototype;m.ta=function(a,b,c){if(this.h.isExternalMethodAvailable(a,c)){b=b||[];if(0<b.length&&Wk(a)){var d=b;if(Ka(d[0])&&!Array.isArray(d[0]))d=d[0];else{var e={};switch(a){case "loadVideoById":case "cueVideoById":e=Yk.apply(window,d);break;case "loadVideoByUrl":case "cueVideoByUrl":e=Xk.apply(window,d);break;case "loadPlaylist":case "cuePlaylist":e=Zk.apply(window,d)}d=e}b.length=1;b[0]=d}this.h.handleExternalCall(a,b,c);Wk(a)&&Vk(this,this.na())}};
m.bb=function(){var a=this.Pa.bind(this);this.i.i=a};
m.addEventListener=function(a,b){this.j.push({eventType:a,listener:b});this.h.addEventListener(a,b)};
m.na=function(){if(!this.h)return null;var a=this.h.getApiInterface();ab(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c];if(0===e.search("get")||0===e.search("is")){var f=0;0===e.search("get")?f=3:0===e.search("is")&&(f=2);f=e.charAt(f).toLowerCase()+e.substr(f+1);try{var g=this.h[e]();b[f]=g}catch(h){}}}b.videoData=this.h.getVideoData();b.currentTimeLastUpdated_=Date.now()/1E3;return b};
m.kb=function(a){a={playerState:a,currentTime:this.h.getCurrentTime(),duration:this.h.getDuration(),videoData:this.h.getVideoData(),videoStartBytes:0,videoBytesTotal:this.h.getVideoBytesTotal(),videoLoadedFraction:this.h.getVideoLoadedFraction(),playbackQuality:this.h.getPlaybackQuality(),availableQualityLevels:this.h.getAvailableQualityLevels(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.h.getPlaybackRate(),mediaReferenceTime:this.h.getMediaReferenceTime()};this.h.getVideoUrl&&(a.videoUrl=
this.h.getVideoUrl());this.h.getVideoContentRect&&(a.videoContentRect=this.h.getVideoContentRect());this.h.getProgressState&&(a.progressState=this.h.getProgressState());this.h.getPlaylist&&(a.playlist=this.h.getPlaylist());this.h.getPlaylistIndex&&(a.playlistIndex=this.h.getPlaylistIndex());this.h.getStoryboardFormat&&(a.storyboardFormat=this.h.getStoryboardFormat());Vk(this,a)};
m.ib=function(a){Vk(this,{playbackQuality:a})};
m.jb=function(a){Vk(this,{playbackRate:a})};
m.gb=function(){for(var a=this.h.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.h.getOptions(e);b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],l=this.h.getOption(e,k);b[e][k]=l}}this.sendMessage("apiInfoDelivery",b)};
m.mb=function(){Vk(this,{muted:this.h.isMuted(),volume:this.h.getVolume()})};
m.lb=function(a){a={currentTime:a,videoBytesLoaded:this.h.getVideoBytesLoaded(),videoLoadedFraction:this.h.getVideoLoadedFraction(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.h.getPlaybackRate(),mediaReferenceTime:this.h.getMediaReferenceTime()};this.h.getProgressState&&(a.progressState=this.h.getProgressState());Vk(this,a)};
m.nb=function(){var a={sphericalProperties:this.h.getSphericalProperties()};Vk(this,a)};
m.dispose=function(){Tk.prototype.dispose.call(this);for(var a=0;a<this.j.length;a++){var b=this.j[a];this.h.removeEventListener(b.eventType,b.listener)}this.j=[]};function al(){var a=kb(bl),b;return Je(new Ce(function(c,d){a.onSuccess=function(e){mg(e)?c(new cl(e)):d(new dl("Request failed, status="+(e&&"status"in e?e.status:-1),"net.badstatus",e))};
a.onError=function(e){d(new dl("Unknown request error","net.unknown",e))};
a.onTimeout=function(e){d(new dl("Request timed out","net.timeout",e))};
b=sg("//googleads.g.doubleclick.net/pagead/id",a)}),function(c){c instanceof Ke&&b.abort();
return He(c)})}
function dl(a,b,c){Ta.call(this,a+", errorCode="+b);this.errorCode=b;this.xhr=c;this.name="PromiseAjaxError"}
v(dl,Ta);function cl(a){this.xhr=a}
;function el(){this.i=0;this.h=null}
el.prototype.then=function(a,b,c){return 1===this.i&&a?(a=a.call(c,this.h),Be(a)?a:fl(a)):2===this.i&&b?(a=b.call(c,this.h),Be(a)?a:gl(a)):this};
el.prototype.getValue=function(){return this.h};
el.prototype.$goog_Thenable=!0;function gl(a){var b=new el;a=void 0===a?null:a;b.i=2;b.h=void 0===a?null:a;return b}
function fl(a){var b=new el;a=void 0===a?null:a;b.i=1;b.h=void 0===a?null:a;return b}
;function hl(a){Ta.call(this,a.message||a.description||a.name);this.isMissing=a instanceof il;this.isTimeout=a instanceof dl&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof Ke}
v(hl,Ta);hl.prototype.name="BiscottiError";function il(){Ta.call(this,"Biscotti ID is missing from server")}
v(il,Ta);il.prototype.name="BiscottiMissingError";var bl={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},jl=null;function Xf(){if(Q("condition_biscotti_fetch_on_consent_cookie_html5_clients")&&!cd.get("CONSENT","").startsWith("YES+"))return He(Error("User has not consented - not fetching biscotti id."));if("1"==ib())return He(Error("Biscotti ID is not available in private embed mode"));jl||(jl=Je(al().then(kl),function(a){return ll(2,a)}));
return jl}
function kl(a){a=a.xhr.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new il;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new il;a=a.id;Yf(a);jl=fl(a);ml(18E5,2);return a}
function ll(a,b){b=new hl(b);Yf("");jl=gl(b);0<a&&ml(12E4,a-1);throw b;}
function ml(a,b){Hf(function(){Je(al().then(kl,function(c){return ll(b,c)}),Ga)},a)}
function nl(){try{var a=A("yt.ads.biscotti.getId_");return a?a():Xf()}catch(b){return He(b)}}
;function ol(a){if("1"!=ib()){a&&Wf();try{nl().then(function(){},function(){}),Hf(ol,18E5)}catch(b){qf(b)}}}
;var pl=Date.now().toString();
function ql(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;16>a;a++){b=Date.now();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(256*Math.random())}if(pl)for(a=1,b=0;b<pl.length;b++)d[a%16]=d[a%16]^d[(a-1)%16]/4^pl.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(d[b]&63));
return a.join("")}
;var rl,sl=y.ytLoggingDocDocumentNonce_;sl||(sl=ql(),Ra("ytLoggingDocDocumentNonce_",sl));rl=sl;var tl={de:0,cc:1,lc:2,jh:3,ge:4,pk:5,Wh:6,Yi:7,0:"DEFAULT",1:"CHAT",2:"CONVERSATIONS",3:"MINIPLAYER",4:"DIALOG",5:"VOZ",6:"MUSIC_WATCH_TABS",7:"SHARE"};function ul(a){this.h=a}
function vl(a){return new ul({trackingParams:a})}
ul.prototype.getAsJson=function(){var a={};void 0!==this.h.trackingParams?a.trackingParams=this.h.trackingParams:(a.veType=this.h.veType,void 0!==this.h.veCounter&&(a.veCounter=this.h.veCounter),void 0!==this.h.elementIndex&&(a.elementIndex=this.h.elementIndex));void 0!==this.h.dataElement&&(a.dataElement=this.h.dataElement.getAsJson());void 0!==this.h.youtubeData&&(a.youtubeData=this.h.youtubeData);return a};
ul.prototype.toString=function(){return JSON.stringify(this.getAsJson())};
ul.prototype.isClientVe=function(){return!this.h.trackingParams&&!!this.h.veType};function wl(a){a=void 0===a?0:a;return 0==a?"client-screen-nonce":"client-screen-nonce."+a}
function xl(a){a=void 0===a?0:a;return 0==a?"ROOT_VE_TYPE":"ROOT_VE_TYPE."+a}
function yl(a){return F(xl(void 0===a?0:a),void 0)}
z("yt_logging_screen.getRootVeType",yl,void 0);function zl(a){return(a=yl(void 0===a?0:a))?new ul({veType:a,youtubeData:void 0}):null}
function Al(){var a=F("csn-to-ctt-auth-info");a||(a={},N("csn-to-ctt-auth-info",a));return a}
function Bl(a){a=void 0===a?0:a;var b=F(wl(a));if(!b&&!F("USE_CSN_FALLBACK",!0))return null;b||0!=a||(b="UNDEFINED_CSN");return b?b:null}
z("yt_logging_screen.getCurrentCsn",Bl,void 0);function Cl(a,b,c){var d=Al();(c=Bl(c))&&delete d[c];b&&(d[a]=b)}
function Dl(a){return Al()[a]}
z("yt_logging_screen.getCttAuthInfo",Dl,void 0);function El(a,b,c,d){c=void 0===c?0:c;if(a!==F(wl(c))||b!==F(xl(c)))Cl(a,d,c),N(wl(c),a),N(xl(c),b),b=function(){setTimeout(function(){a&&ph("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:rl,clientScreenNonce:a},uk)},0)},"requestAnimationFrame"in window?window.requestAnimationFrame(b):b()}
z("yt_logging_screen.setCurrentScreen",El,void 0);function Fl(a){Jh.call(this,1,arguments);this.csn=a}
v(Fl,Jh);var Sh=new Kh("screen-created",Fl),Gl=[],Il=Hl,Jl=0;function Kl(a,b,c,d){var e=d;Q("web_dedupe_ve_grafting")&&(e=d.filter(function(f){f.csn!==b?(f.csn=b,f=!0):f=!1;return f}));
c={csn:b,parentVe:c.getAsJson(),childVes:Ya(e,function(f){return f.getAsJson()})};
d=u(d);for(e=d.next();!e.done;e=d.next())e=e.value.getAsJson(),(gb(e)||!e.trackingParams&&!e.veType)&&Ok(Error("Child VE logged with no data"));d={G:Dl(b),S:b};"UNDEFINED_CSN"==b?Ll("visualElementAttached",c,d):a?ph("visualElementAttached",c,a,d):vk("visualElementAttached",c,d)}
function Hl(){for(var a=Math.random()+"",b=[],c=0,d=0;d<a.length;d++){var e=a.charCodeAt(d);255<e&&(b[c++]=e&255,e>>=8);b[c++]=e}return Cc(b)}
function Ll(a,b,c){Gl.push({payloadName:a,payload:b,options:c});Jl||(Jl=Th())}
function Uh(a){if(Gl){for(var b=u(Gl),c=b.next();!c.done;c=b.next())c=c.value,c.payload&&(c.payload.csn=a.csn,ph(c.payloadName,c.payload,null,c.options));Gl.length=0}Jl=0}
;function Ml(){this.i=new Set;this.h=new Set;this.j=new Map}
Ml.prototype.clear=function(){this.i.clear();this.h.clear();this.j.clear()};
Ha(Ml);function Nl(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];if(!Ol(a)||c.some(function(e){return!Ol(e)}))throw Error("Only objects may be merged.");
c=u(c);for(d=c.next();!d.done;d=c.next())Pl(a,d.value);return a}
function Pl(a,b){for(var c in b)if(Ol(b[c])){if(c in a&&!Ol(a[c]))throw Error("Cannot merge an object into a non-object.");c in a||(a[c]={});Pl(a[c],b[c])}else if(Ql(b[c])){if(c in a&&!Ql(a[c]))throw Error("Cannot merge an array into a non-array.");c in a||(a[c]=[]);Rl(a[c],b[c])}else a[c]=b[c];return a}
function Rl(a,b){b=u(b);for(var c=b.next();!c.done;c=b.next())c=c.value,Ol(c)?a.push(Pl({},c)):Ql(c)?a.push(Rl([],c)):a.push(c);return a}
function Ol(a){return"object"===typeof a&&!Array.isArray(a)}
function Ql(a){return"object"===typeof a&&Array.isArray(a)}
;function Sl(a,b){Jh.call(this,1,arguments)}
v(Sl,Jh);function Tl(a,b){Jh.call(this,1,arguments)}
v(Tl,Jh);var Ul=new Kh("aft-recorded",Sl),Vl=new Kh("timing-sent",Tl);var Wl=window;function Xl(){this.timing={};this.clearResourceTimings=function(){};
this.webkitClearResourceTimings=function(){};
this.mozClearResourceTimings=function(){};
this.msClearResourceTimings=function(){};
this.oClearResourceTimings=function(){}}
var W=Wl.performance||Wl.mozPerformance||Wl.msPerformance||Wl.webkitPerformance||new Xl;var Yl=!1,Zl={'script[name="scheduler/scheduler"]':"sj",'script[name="player/base"]':"pj",'link[rel="stylesheet"][name="www-player"]':"pc",'link[rel="stylesheet"][name="player/www-player"]':"pc",'script[name="desktop_polymer/desktop_polymer"]':"dpj",'link[rel="import"][name="desktop_polymer"]':"dph",'script[name="mobile-c3/mobile-c3"]':"mcj",'link[rel="stylesheet"][name="mobile-c3"]':"mcc",'script[name="player-plasma-ias-phone/base"]':"mcppj",'script[name="player-plasma-ias-tablet/base"]':"mcptj",
'link[rel="stylesheet"][name="mobile-polymer-player-ias"]':"mcpc",'link[rel="stylesheet"][name="mobile-polymer-player-svg-ias"]':"mcpsc",'script[name="mobile_blazer_core_mod"]':"mbcj",'link[rel="stylesheet"][name="mobile_blazer_css"]':"mbc",'script[name="mobile_blazer_logged_in_users_mod"]':"mbliuj",'script[name="mobile_blazer_logged_out_users_mod"]':"mblouj",'script[name="mobile_blazer_noncore_mod"]':"mbnj","#player_css":"mbpc",'script[name="mobile_blazer_desktopplayer_mod"]':"mbpj",'link[rel="stylesheet"][name="mobile_blazer_tablet_css"]':"mbtc",
'script[name="mobile_blazer_watch_mod"]':"mbwj"};B(W.clearResourceTimings||W.webkitClearResourceTimings||W.mozClearResourceTimings||W.msClearResourceTimings||W.oClearResourceTimings||Ga,W);function $l(a){var b=am(a);if(b.aft)return b.aft;a=F((a||"")+"TIMING_AFT_KEYS",["ol"]);for(var c=a.length,d=0;d<c;d++){var e=b[a[d]];if(e)return e}return NaN}
function bm(){var a;if(Q("csi_use_performance_navigation_timing")){var b,c,d,e=null===(d=null===(c=null===(b=null===(a=null===W||void 0===W?void 0:W.getEntriesByType)||void 0===a?void 0:a.call(W,"navigation"))||void 0===b?void 0:b[0])||void 0===c?void 0:c.toJSON)||void 0===d?void 0:d.call(c);e?(e.requestStart=cm(e.requestStart),e.responseEnd=cm(e.responseEnd),e.redirectStart=cm(e.redirectStart),e.redirectEnd=cm(e.redirectEnd),e.domainLookupEnd=cm(e.domainLookupEnd),e.connectStart=cm(e.connectStart),
e.connectEnd=cm(e.connectEnd),e.responseStart=cm(e.responseStart),e.secureConnectionStart=cm(e.secureConnectionStart),e.domainLookupStart=cm(e.domainLookupStart),e.isPerformanceNavigationTiming=!0,a=e):a=W.timing}else a=W.timing;return a}
function dm(){return Q("csi_use_time_origin")&&W.timeOrigin?Math.floor(W.timeOrigin):W.timing.navigationStart}
function cm(a){return Math.round(dm()+a)}
function em(a){var b;(b=A("ytcsi."+(a||"")+"data_"))||(b={tick:{},info:{}},Ra("ytcsi."+(a||"")+"data_",b));return b}
function fm(a){a=em(a);a.info||(a.info={});return a.info}
function am(a){a=em(a);a.tick||(a.tick={});return a.tick}
function gm(a){var b=em(a).nonce;b||(b=ql(),em(a).nonce=b);return b}
function hm(a){var b=am(a||""),c=$l(a);c&&!Yl&&(Ph(Ul,new Sl(Math.round(c-b._start),a)),Yl=!0)}
;function im(){if(W.getEntriesByType){var a=W.getEntriesByType("paint");if(a=$a(a,function(b){return"first-paint"===b.name}))return cm(a.startTime)}a=W.timing;
return a.ab?Math.max(0,a.ab):0}
;function jm(){var a=A("ytcsi.debug");a||(a=[],z("ytcsi.debug",a,void 0),z("ytcsi.reference",{},void 0));return a}
function km(a){a=a||"";var b=A("ytcsi.reference");b||(jm(),b=A("ytcsi.reference"));if(b[a])return b[a];var c=jm(),d={timerName:a,info:{},tick:{},span:{}};c.push(d);return b[a]=d}
;var lm=y.ytLoggingLatencyUsageStats_||{};z("ytLoggingLatencyUsageStats_",lm,void 0);function mm(){this.h=0}
function nm(){mm.h||(mm.h=new mm);return mm.h}
mm.prototype.tick=function(a,b,c){om(this,"tick_"+a+"_"+b)||vk("latencyActionTicked",{tickName:a,clientActionNonce:b},{timestamp:c})};
mm.prototype.info=function(a,b){var c=Object.keys(a).join("");om(this,"info_"+c+"_"+b)||(a=Object.assign({},a),a.clientActionNonce=b,vk("latencyActionInfo",a))};
mm.prototype.span=function(a,b){var c=Object.keys(a).join("");om(this,"span_"+c+"_"+b)||(a.clientActionNonce=b,vk("latencyActionSpan",a))};
function om(a,b){lm[b]=lm[b]||{count:0};var c=lm[b];c.count++;c.time=R();a.h||(a.h=Lf(function(){var d=R(),e;for(e in lm)lm[e]&&6E4<d-lm[e].time&&delete lm[e];a&&(a.h=0)},5E3));
return 5<c.count?(6===c.count&&1>1E5*Math.random()&&(c=new fi("CSI data exceeded logging limit with key",b.split("_")),0<=b.indexOf("plev")||Ok(c)),!0):!1}
;var X={},pm=(X.auto_search="LATENCY_ACTION_AUTO_SEARCH",X.ad_to_ad="LATENCY_ACTION_AD_TO_AD",X.ad_to_video="LATENCY_ACTION_AD_TO_VIDEO",X.app_startup="LATENCY_ACTION_APP_STARTUP",X["artist.analytics"]="LATENCY_ACTION_CREATOR_ARTIST_ANALYTICS",X["artist.events"]="LATENCY_ACTION_CREATOR_ARTIST_CONCERTS",X["artist.presskit"]="LATENCY_ACTION_CREATOR_ARTIST_PROFILE",X.browse="LATENCY_ACTION_BROWSE",X.channels="LATENCY_ACTION_CHANNELS",X.creator_channel_dashboard="LATENCY_ACTION_CREATOR_CHANNEL_DASHBOARD",
X["channel.analytics"]="LATENCY_ACTION_CREATOR_CHANNEL_ANALYTICS",X["channel.comments"]="LATENCY_ACTION_CREATOR_CHANNEL_COMMENTS",X["channel.content"]="LATENCY_ACTION_CREATOR_POST_LIST",X["channel.copyright"]="LATENCY_ACTION_CREATOR_CHANNEL_COPYRIGHT",X["channel.editing"]="LATENCY_ACTION_CREATOR_CHANNEL_EDITING",X["channel.monetization"]="LATENCY_ACTION_CREATOR_CHANNEL_MONETIZATION",X["channel.music"]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC",X["channel.translations"]="LATENCY_ACTION_CREATOR_CHANNEL_TRANSLATIONS",
X["channel.videos"]="LATENCY_ACTION_CREATOR_CHANNEL_VIDEOS",X["channel.live_streaming"]="LATENCY_ACTION_CREATOR_LIVE_STREAMING",X.chips="LATENCY_ACTION_CHIPS",X["dialog.copyright_strikes"]="LATENCY_ACTION_CREATOR_DIALOG_COPYRIGHT_STRIKES",X["dialog.uploads"]="LATENCY_ACTION_CREATOR_DIALOG_UPLOADS",X.embed="LATENCY_ACTION_EMBED",X.entity_key_serialization_perf="LATENCY_ACTION_ENTITY_KEY_SERIALIZATION_PERF",X.entity_key_deserialization_perf="LATENCY_ACTION_ENTITY_KEY_DESERIALIZATION_PERF",X.home="LATENCY_ACTION_HOME",
X.library="LATENCY_ACTION_LIBRARY",X.live="LATENCY_ACTION_LIVE",X.live_pagination="LATENCY_ACTION_LIVE_PAGINATION",X.onboarding="LATENCY_ACTION_KIDS_ONBOARDING",X.parent_profile_settings="LATENCY_ACTION_KIDS_PARENT_PROFILE_SETTINGS",X.parent_tools_collection="LATENCY_ACTION_PARENT_TOOLS_COLLECTION",X.parent_tools_dashboard="LATENCY_ACTION_PARENT_TOOLS_DASHBOARD",X.player_att="LATENCY_ACTION_PLAYER_ATTESTATION",X["post.comments"]="LATENCY_ACTION_CREATOR_POST_COMMENTS",X["post.edit"]="LATENCY_ACTION_CREATOR_POST_EDIT",
X.prebuffer="LATENCY_ACTION_PREBUFFER",X.prefetch="LATENCY_ACTION_PREFETCH",X.profile_settings="LATENCY_ACTION_KIDS_PROFILE_SETTINGS",X.profile_switcher="LATENCY_ACTION_KIDS_PROFILE_SWITCHER",X.results="LATENCY_ACTION_RESULTS",X.search_ui="LATENCY_ACTION_SEARCH_UI",X.search_suggest="LATENCY_ACTION_SUGGEST",X.search_zero_state="LATENCY_ACTION_SEARCH_ZERO_STATE",X.secret_code="LATENCY_ACTION_KIDS_SECRET_CODE",X.seek="LATENCY_ACTION_PLAYER_SEEK",X.settings="LATENCY_ACTION_SETTINGS",X.tenx="LATENCY_ACTION_TENX",
X.video_to_ad="LATENCY_ACTION_VIDEO_TO_AD",X.watch="LATENCY_ACTION_WATCH",X.watch_it_again="LATENCY_ACTION_KIDS_WATCH_IT_AGAIN",X["watch,watch7"]="LATENCY_ACTION_WATCH",X["watch,watch7_html5"]="LATENCY_ACTION_WATCH",X["watch,watch7ad"]="LATENCY_ACTION_WATCH",X["watch,watch7ad_html5"]="LATENCY_ACTION_WATCH",X.wn_comments="LATENCY_ACTION_LOAD_COMMENTS",X.ww_rqs="LATENCY_ACTION_WHO_IS_WATCHING",X["video.analytics"]="LATENCY_ACTION_CREATOR_VIDEO_ANALYTICS",X["video.comments"]="LATENCY_ACTION_CREATOR_VIDEO_COMMENTS",
X["video.edit"]="LATENCY_ACTION_CREATOR_VIDEO_EDIT",X["video.translations"]="LATENCY_ACTION_CREATOR_VIDEO_TRANSLATIONS",X["video.video_editor"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR",X["video.video_editor_async"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR_ASYNC",X["video.monetization"]="LATENCY_ACTION_CREATOR_VIDEO_MONETIZATION",X.voice_assistant="LATENCY_ACTION_VOICE_ASSISTANT",X.cast_load_by_entity_to_watch="LATENCY_ACTION_CAST_LOAD_BY_ENTITY_TO_WATCH",X.networkless_performance="LATENCY_ACTION_NETWORKLESS_PERFORMANCE",
X),Y={},qm=(Y.ad_allowed="adTypesAllowed",Y.yt_abt="adBreakType",Y.ad_cpn="adClientPlaybackNonce",Y.ad_docid="adVideoId",Y.yt_ad_an="adNetworks",Y.ad_at="adType",Y.aida="appInstallDataAgeMs",Y.browse_id="browseId",Y.p="httpProtocol",Y.t="transportProtocol",Y.cpn="clientPlaybackNonce",Y.ccs="creatorInfo.creatorCanaryState",Y.csn="clientScreenNonce",Y.docid="videoId",Y.GetHome_rid="requestIds",Y.GetSearch_rid="requestIds",Y.GetPlayer_rid="requestIds",Y.GetWatchNext_rid="requestIds",Y.GetBrowse_rid=
"requestIds",Y.GetLibrary_rid="requestIds",Y.is_continuation="isContinuation",Y.is_nav="isNavigation",Y.b_p="kabukiInfo.browseParams",Y.is_prefetch="kabukiInfo.isPrefetch",Y.is_secondary_nav="kabukiInfo.isSecondaryNav",Y.prev_browse_id="kabukiInfo.prevBrowseId",Y.query_source="kabukiInfo.querySource",Y.voz_type="kabukiInfo.vozType",Y.yt_lt="loadType",Y.mver="creatorInfo.measurementVersion",Y.yt_ad="isMonetized",Y.nr="webInfo.navigationReason",Y.nrsu="navigationRequestedSameUrl",Y.ncnp="webInfo.nonPreloadedNodeCount",
Y.pnt="performanceNavigationTiming",Y.prt="playbackRequiresTap",Y.plt="playerInfo.playbackType",Y.pis="playerInfo.playerInitializedState",Y.paused="playerInfo.isPausedOnLoad",Y.yt_pt="playerType",Y.fmt="playerInfo.itag",Y.yt_pl="watchInfo.isPlaylist",Y.yt_pre="playerInfo.preloadType",Y.yt_ad_pr="prerollAllowed",Y.pa="previousAction",Y.yt_red="isRedSubscriber",Y.rce="mwebInfo.responseContentEncoding",Y.scrh="screenHeight",Y.scrw="screenWidth",Y.st="serverTimeMs",Y.ssdm="shellStartupDurationMs",Y.br_trs=
"tvInfo.bedrockTriggerState",Y.kebqat="kabukiInfo.earlyBrowseRequestInfo.abandonmentType",Y.kebqa="kabukiInfo.earlyBrowseRequestInfo.adopted",Y.label="tvInfo.label",Y.is_mdx="tvInfo.isMdx",Y.preloaded="tvInfo.isPreloaded",Y.upg_player_vis="playerInfo.visibilityState",Y.query="unpluggedInfo.query",Y.upg_chip_ids_string="unpluggedInfo.upgChipIdsString",Y.yt_vst="videoStreamType",Y.vph="viewportHeight",Y.vpw="viewportWidth",Y.yt_vis="isVisible",Y.rcl="mwebInfo.responseContentLength",Y.GetSettings_rid=
"requestIds",Y.GetTrending_rid="requestIds",Y.GetMusicSearchSuggestions_rid="requestIds",Y.REQUEST_ID="requestIds",Y),rm="isContinuation isNavigation kabukiInfo.earlyBrowseRequestInfo.adopted kabukiInfo.isPrefetch kabukiInfo.isSecondaryNav isMonetized navigationRequestedSameUrl performanceNavigationTiming playerInfo.isPausedOnLoad prerollAllowed isRedSubscriber tvInfo.isMdx tvInfo.isPreloaded isVisible watchInfo.isPlaylist playbackRequiresTap".split(" "),sm={},tm=(sm.ccs="CANARY_STATE_",sm.mver="MEASUREMENT_VERSION_",
sm.pis="PLAYER_INITIALIZED_STATE_",sm.yt_pt="LATENCY_PLAYER_",sm.pa="LATENCY_ACTION_",sm.yt_vst="VIDEO_STREAM_TYPE_",sm),um="all_vc ap aq c cver cbrand cmodel cplatform ctheme ei l_an l_mm plid srt yt_fss yt_li vpst vpni2 vpil2 icrc icrt pa GetAccountOverview_rid GetHistory_rid cmt d_vpct d_vpnfi d_vpni nsru pc pfa pfeh pftr pnc prerender psc rc start tcrt tcrc ssr vpr vps yt_abt yt_fn yt_fs yt_pft yt_pre yt_pt yt_pvis ytu_pvis yt_ref yt_sts tds".split(" ");
function vm(a){return!!F("FORCE_CSI_ON_GEL",!1)||Q("csi_on_gel")||!!em(a).useGel}
function wm(a,b,c){var d=xm(c);d.gelTicks&&(d.gelTicks["tick_"+a]=!0);c||b||R();return vm(c)?(km(c||"").tick[a]=b||R(),d=gm(c),"_start"===a?(a=nm(),om(a,"baseline_"+d)||vk("latencyActionBaselined",{clientActionNonce:d},{timestamp:b})):nm().tick(a,d,b),hm(c),!0):!1}
function ym(a,b,c){c=xm(c);if(c.gelInfos)c.gelInfos["info_"+a]=!0;else{var d={};c.gelInfos=(d["info_"+a]=!0,d)}if(a.match("_rid")){var e=a.split("_rid")[0];a="REQUEST_ID"}if(a in qm){c=qm[a];0<=Wa(rm,c)&&(b=!!b);a in tm&&"string"===typeof b&&(b=tm[a]+b.toUpperCase());a=b;b=c.split(".");for(var f=d={},g=0;g<b.length-1;g++){var h=b[g];f[h]={};f=f[h]}f[b[b.length-1]]="requestIds"===c?[{id:a,endpoint:e}]:a;return Nl({},d)}0<=Wa(um,a)||Ok(new fi("Unknown label logged with GEL CSI",a))}
function xm(a){a=em(a);if(a.gel){var b=a.gel;b.gelInfos||(b.gelInfos={});b.gelTicks||(b.gelTicks={})}else a.gel={gelTicks:{},gelInfos:{}};return a.gel}
function zm(a){a=xm(a);a.gelInfos||(a.gelInfos={});return a.gelInfos}
;function Am(a,b,c){null!==b&&(fm(c)[a]=b,vm(c)?(a=ym(a,b,c))&&vm(c)&&(b=km(c||""),Nl(b.info,a),Nl(zm(c),a),c=gm(c),nm().info(a,c)):km(c||"").info[a]=b)}
function Z(a,b,c){var d=am(c);if(!b&&"_"!==a[0]){var e=a;W.mark&&(0==e.lastIndexOf("mark_",0)||(e="mark_"+e),c&&(e+=" ("+c+")"),W.mark(e))}e=b||R();d[a]=e;wm(a,b,c)||(Bm(c),km(c||"").tick[a]=b||R());return d[a]}
function Cm(a,b){if(vm(void 0)){var c=xm(void 0);if(c.gelSpans)c.gelSpans[a]=!0;else{var d={};c.gelSpans=(d[a]=!0,d)}a={spanName:a,spanLengthUsec:String(Math.round(1E3*b))};km("").span[String(a.spanName)]=a;b=xm(void 0);b.gelSpans||(b.gelSpans={});Nl(b.gelSpans,a);b=gm(void 0);nm().span(a,b)}}
function Dm(){var a=gm(void 0);requestAnimationFrame(function(){setTimeout(function(){a===gm(void 0)&&Z("ol",void 0,void 0)},0)})}
function Bm(a){if(!A("yt.timing."+(a||"")+"pingSent_")){var b=F((a||"")+"TIMING_ACTION",void 0),c=am(a);if(b=!!A("ytglobal.timing"+(a||"")+"ready_")&&b)b="_start"in am(void 0);if(b&&$l(a))if(hm(a),a)Em(a);else{b=!0;var d=F("TIMING_WAIT",[]);if(d.length)for(var e=0,f=d.length;e<f;++e)if(!(d[e]in c)){b=!1;break}b&&Em(a)}}}
function Fm(){var a=document;if("visibilityState"in a)a=a.visibilityState;else{var b=xf+"VisibilityState";a=b in a?a[b]:void 0}switch(a){case "hidden":return 0;case "visible":return 1;case "prerender":return 2;case "unloaded":return 3;default:return-1}}
function Em(a){if(!vm(a)){var b=am(a),c=fm(a),d=b._start,e=F("CSI_SERVICE_NAME","youtube"),f={v:2,s:e,action:F((a||"")+"TIMING_ACTION",void 0)},g=c.srt;void 0!==b.srt&&delete c.srt;b.aft=$l(a);var h=am(a),k=h.pbr,l=h.vc;h=h.pbs;k&&l&&h&&k<l&&l<h&&fm(a).yt_pvis&&"youtube"===e&&(Am("yt_lt","hot_bg",a),e=b.vc,k=b.pbs,delete b.aft,c.aft=Math.round(k-e));for(var p in c)"_"!==p.charAt(0)&&(f[p]=c[p]);b.ps=R();p={};e=[];for(var n in b)"_"!==n.charAt(0)&&(k=Math.round(b[n]-d),p[n]=k,e.push(n+"."+k));f.rt=
e.join(",");b=!!c.ap;c="";for(var r in f)f.hasOwnProperty(r)&&(c+="&"+r+"="+f[r]);f="/csi_204?"+c.substring(1);window.navigator&&window.navigator.sendBeacon&&(b||Q("always_send_csi_204_with_beacon"))?Hg(f):Eg(f);z("yt.timing."+(a||"")+"pingSent_",!0,void 0);Ph(Vl,new Tl(p.aft+(Number(g)||0),a))}}
function Gm(a,b){a=document.querySelector(a);if(!a)return!1;var c="",d=a.nodeName;"SCRIPT"===d?(c=a.src,c||(c=a.getAttribute("data-timing-href"))&&(c=window.location.protocol+c)):"LINK"===d&&(c=a.href);Wb()&&a.setAttribute("nonce",Wb());return c?(a=W.getEntriesByName(c))&&a[0]&&(a=a[0],c=dm(),Z("rsf_"+b,c+Math.round(a.fetchStart)),Z("rse_"+b,c+Math.round(a.responseEnd)),void 0!==a.transferSize&&(b=fm(void 0),c=zm(void 0),"rc"in b||"rc"in c||Am("rc",""),0===a.transferSize))?!0:!1:!1}
function Hm(){var a=window.location.protocol,b=W.getEntriesByType("resource");b=Xa(b,function(c){return 0===c.name.indexOf(a+"//fonts.gstatic.com/s/")});
(b=Za(b,function(c,d){return d.duration>c.duration?d:c},{duration:0}))&&0<b.startTime&&0<b.responseEnd&&(Z("wffs",cm(b.startTime)),Z("wffe",cm(b.responseEnd)))}
var Im=window;Im.ytcsi&&(Im.ytcsi.info=Am,Im.ytcsi.tick=Z);function Jm(){this.l=[];this.u=[];this.h=[];this.i=new Set;this.m=new Map}
function Km(a,b,c){c=void 0===c?0:c;b.then(function(d){var e,f;a.i.has(c)&&a.j&&a.j();var g=Bl(c),h=zl(c);g&&h&&(d.csn=g,(null===(e=d.response)||void 0===e?0:e.trackingParams)&&Kl(a.client,g,h,[vl(d.response.trackingParams)]),(null===(f=d.playerResponse)||void 0===f?0:f.trackingParams)&&Kl(a.client,g,h,[vl(d.playerResponse.trackingParams)]))})}
function Lm(a,b,c,d){d=void 0===d?0:d;if(a.i.has(d))a.l.push([b,c]);else{var e=Bl(d);c=c||zl(d);e&&c&&Kl(a.client,e,c,[b])}}
Jm.prototype.clickCommand=function(a,b,c){c=Bl(void 0===c?0:c);if(!a.clickTrackingParams||!c)return!1;var d=this.client;var e="INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK";a={csn:c,ve:vl(a.clickTrackingParams).getAsJson(),gestureType:e};b&&(a.clientData=b);b={G:Dl(c),S:c};"UNDEFINED_CSN"==c?Ll("visualElementGestured",a,b):d?ph("visualElementGestured",a,d,b):vk("visualElementGestured",a,b);return!0};
function Mm(a,b,c){c=void 0===c?{}:c;a.i.add(c.layer||0);a.j=function(){Nm(a,b,c);var f=zl(c.layer);if(f){for(var g=u(a.l),h=g.next();!h.done;h=g.next())h=h.value,Lm(a,h[0],h[1]||f,c.layer);f=u(a.u);for(g=f.next();!g.done;g=f.next()){var k=g.value;g=void 0;g=void 0===g?0:g;h=Bl(g);var l=k[0]||zl(g);h&&l&&(g=a.client,k=k[1],k={csn:h,ve:l.getAsJson(),clientData:k},l={G:Dl(h),S:h},"UNDEFINED_CSN"==h?Ll("visualElementStateChanged",k,l):g?ph("visualElementStateChanged",k,g,l):vk("visualElementStateChanged",
k,l))}}};
Bl(c.layer)||a.j();if(c.za)for(var d=u(c.za),e=d.next();!e.done;e=d.next())Km(a,e.value,c.layer);else Pk(Error("Delayed screen needs a data promise."))}
function Nm(a,b,c){c=void 0===c?{}:c;c.layer||(c.layer=0);var d=void 0!==c.cb?c.cb:c.layer;var e=Bl(d);d=zl(d);var f;d&&(void 0!==c.parentCsn?f={clientScreenNonce:c.parentCsn,visualElement:d}:e&&"UNDEFINED_CSN"!==e&&(f={clientScreenNonce:e,visualElement:d}));try{var g=a.client,h=f,k=c.ya,l=c.G,p=Il(),n={csn:p,pageVe:(new ul({veType:b,youtubeData:void 0})).getAsJson()};h&&h.visualElement?n.implicitGesture={parentCsn:h.clientScreenNonce,gesturedVe:h.visualElement.getAsJson()}:h&&Ok(new fi("newScreen() parent element does not have a VE - rootVe",
b));k&&(n.cloneCsn=k);k={G:l,S:p};g?ph("screenCreated",n,g,k):vk("screenCreated",n,k);Ph(Sh,new Fl(p));var r=p}catch(q){Qk(q,{Qk:b,rootVe:d,parentVisualElement:void 0,Lk:e,Pk:f,ya:c.ya});Pk(q);return}El(r,b,c.layer,c.G);if((b=e&&"UNDEFINED_CSN"!==e&&d)&&!(b=Q("screen_manager_skip_hide_killswitch"))){a:{b=u(Object.values(tl));for(f=b.next();!f.done;f=b.next())if(Bl(f.value)==e){b=!0;break a}b=!1}b=!b}b&&(b=a.client,f=!0,g=(f=void 0===f?!1:f)?16:8,d={csn:e,ve:d.getAsJson(),eventType:g},f={G:Dl(e),S:e,
Oa:f},"UNDEFINED_CSN"==e?Ll("visualElementHidden",d,f):b?ph("visualElementHidden",d,b,f):vk("visualElementHidden",d,f));a.h[a.h.length-1]&&!a.h[a.h.length-1].csn&&(a.h[a.h.length-1].csn=r||"");Am("csn",r);Ml.getInstance().clear();d=zl(c.layer);e&&"UNDEFINED_CSN"!==e&&d&&(Q("web_mark_root_visible")||Q("music_web_mark_root_visible"))&&(e=r,r=Q("use_default_events_client")?void 0:uk,b={csn:e,ve:d.getAsJson(),eventType:1},f={G:Dl(e),S:e},"UNDEFINED_CSN"==e?Ll("visualElementShown",b,f):r?ph("visualElementShown",
b,r,f):vk("visualElementShown",b,f));a.i.delete(c.layer||0);a.j=void 0;e=u(a.m);for(r=e.next();!r.done;r=e.next())r=u(r.value),b=r.next().value,r.next().value.has(c.layer)&&d&&Lm(a,b,d,c.layer)}
;function Om(a){a&&(a.dataset?a.dataset[Pm("loaded")]="true":a.setAttribute("data-loaded","true"))}
function Qm(a,b){return a?a.dataset?a.dataset[Pm(b)]:a.getAttribute("data-"+b):null}
var Rm={};function Pm(a){return Rm[a]||(Rm[a]=String(a).replace(/\-([a-z])/g,function(b,c){return c.toUpperCase()}))}
;var Sm=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,Tm=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function Um(a,b,c){c=void 0===c?null:c;if(window.spf&&spf.script){c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(Sm,""),c=c.replace(Tm,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else Vm(a,b,c)}
function Vm(a,b,c){c=void 0===c?null:c;var d=Wm(a),e=document.getElementById(d),f=e&&Qm(e,"loaded"),g=e&&!f;f?b&&b():(b&&(f=Mg(d,b),b=""+La(b),Xm[b]=f),g||(e=Ym(a,d,function(){Qm(e,"loaded")||(Om(e),Pg(d),Hf(Qa(Qg,d),0))},c)))}
function Ym(a,b,c,d){d=void 0===d?null:d;var e=Kc(document,"SCRIPT");e.id=b;e.onload=function(){c&&setTimeout(c,0)};
e.onreadystatechange=function(){switch(e.readyState){case "loaded":case "complete":e.onload()}};
d&&e.setAttribute("nonce",d);Vb(e,Sc(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(e,a.firstChild);return e}
function Zm(a){a=Wm(a);var b=document.getElementById(a);b&&(Qg(a),b.parentNode.removeChild(b))}
function $m(a,b){a&&b&&(a=""+La(b),(a=Xm[a])&&Og(a))}
function Wm(a){var b=document.createElement("a");Rb(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+$b(a)}
var Xm={};var an=[],bn=!1;function cn(){if((!Q("condition_ad_status_fetch_on_consent_cookie_html5_clients")||cd.get("CONSENT","").startsWith("YES+"))&&"1"!=ib()){var a=function(){bn=!0;"google_ad_status"in window?N("DCLKSTAT",1):N("DCLKSTAT",2)};
try{Um("//static.doubleclick.net/instream/ad_status.js",a)}catch(b){}an.push(Nf(function(){if(!(bn||"google_ad_status"in window)){try{$m("//static.doubleclick.net/instream/ad_status.js",a)}catch(b){}bn=!0;N("DCLKSTAT",3)}},5E3))}}
function dn(){var a=Number(F("DCLKSTAT",0));return isNaN(a)?0:a}
;function en(){this.i=!1;this.h=null}
en.prototype.initialize=function(a,b,c,d,e,f){var g=this;f=void 0===f?!1:f;b?(this.i=!0,Um(b,function(){g.i=!1;var h=0<=b.indexOf("/th/");(h?window.trayride:window.botguard)?fn(g,c,!!f,h,d):(Zm(b),Ok(new fi("Unable to load Botguard","from "+b)))},e)):a&&(e=Kc(document,"SCRIPT"),e.textContent=a,e.nonce=Wb(),document.head.appendChild(e),document.head.removeChild(e),((a=a.includes("trayride"))?window.trayride:window.botguard)?fn(this,c,!!f,a,d):Ok(Error("Unable to load Botguard from JS")))};
function fn(a,b,c,d,e){var f,g;if(d=d?null===(f=window.trayride)||void 0===f?void 0:f.ad:null===(g=window.botguard)||void 0===g?void 0:g.bg)if(c)try{gn(a,new d(b,e?function(){return e(b)}:Ga))}catch(h){h instanceof Error&&Ok(h)}else{try{gn(a,new d(b))}catch(h){h instanceof Error&&Ok(h)}e&&e(b)}else Ok(Error("Failed to finish initializing VM"))}
en.prototype.invoke=function(a){a=void 0===a?{}:a;return this.h?this.h.hasOwnProperty("hot")?this.h.hot(void 0,void 0,a):this.h.invoke(void 0,void 0,a):null};
en.prototype.dispose=function(){this.h=null};
function gn(a,b){a.h=b}
;var hn=new en;function jn(){return!!hn.h}
function kn(a){a=void 0===a?{}:a;return hn.invoke(a)}
;function ln(a){L.call(this);this.i={};this.started=!1;this.connection=a;this.connection.subscribe("command",this.Ga,this)}
v(ln,L);m=ln.prototype;m.start=function(){this.started||this.h||(this.started=!0,this.connection.V("RECEIVING"))};
m.V=function(a,b){this.started&&!this.h&&this.connection.V(a,b)};
m.Ga=function(a,b,c){if(this.started&&!this.h){var d=b||{};switch(a){case "addEventListener":"string"===typeof d.event&&this.addListener(d.event);break;case "removeEventListener":"string"===typeof d.event&&this.removeListener(d.event);break;default:this.api.isReady()&&this.api.isExternalMethodAvailable(a,c||null)&&(b=mn(a,b||{}),c=this.api.handleExternalCall(a,b,c||null),(c=nn(a,c))&&this.V(a,c))}}};
m.addListener=function(a){if(!(a in this.i)){var b=this.hb.bind(this,a);this.i[a]=b;this.addEventListener(a,b)}};
m.hb=function(a,b){this.started&&!this.h&&this.connection.V(a,this.ma(a,b))};
m.ma=function(a,b){if(null!=b)return{value:b}};
m.removeListener=function(a){a in this.i&&(this.removeEventListener(a,this.i[a]),delete this.i[a])};
m.D=function(){var a=this.connection;a.h||Ue(a.i,"command",this.Ga,this);this.connection=null;for(var b in this.i)this.i.hasOwnProperty(b)&&this.removeListener(b);L.prototype.D.call(this)};function on(a,b){ln.call(this,b);this.api=a;this.start()}
v(on,ln);on.prototype.addEventListener=function(a,b){this.api.addEventListener(a,b)};
on.prototype.removeEventListener=function(a,b){this.api.removeEventListener(a,b)};
function mn(a,b){switch(a){case "loadVideoById":return a=Yk(b),[a];case "cueVideoById":return a=Yk(b),[a];case "loadVideoByPlayerVars":return[b];case "cueVideoByPlayerVars":return[b];case "loadPlaylist":return a=Zk(b),[a];case "cuePlaylist":return a=Zk(b),[a];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];case "setLoop":return[b.loopPlaylists];
case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey,b.ctrlKey,b.altKey,b.metaKey,b.key,b.code]}return[]}
function nn(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
on.prototype.ma=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return ln.prototype.ma.call(this,a,b)};
on.prototype.D=function(){ln.prototype.D.call(this);delete this.api};function pn(a){a=void 0===a?!1:a;L.call(this);this.i=new M(a);Fd(this,Qa(Dd,this.i))}
C(pn,L);pn.prototype.subscribe=function(a,b,c){return this.h?0:this.i.subscribe(a,b,c)};
pn.prototype.l=function(a,b){this.h||this.i.U.apply(this.i,arguments)};function qn(a,b,c){pn.call(this);this.j=a;this.destination=b;this.id=c}
v(qn,pn);qn.prototype.V=function(a,b){this.h||this.j.V(this.destination,this.id,a,b)};
qn.prototype.D=function(){this.destination=this.j=null;pn.prototype.D.call(this)};function rn(a,b,c){L.call(this);this.destination=a;this.origin=c;this.i=Ef(window,"message",this.j.bind(this));this.connection=new qn(this,a,b);Fd(this,Qa(Dd,this.connection))}
v(rn,L);rn.prototype.V=function(a,b,c,d){this.h||a!==this.destination||(a={id:b,command:c},d&&(a.data=d),this.destination.postMessage(ve(a),this.origin))};
rn.prototype.j=function(a){var b;if(b=!this.h)if(b=a.origin===this.origin)a:{b=this.destination;do{b:{var c=a.source;do{if(c===b){c=!0;break b}if(c===c.parent)break;c=c.parent}while(null!=c);c=!1}if(c){b=!0;break a}b=b.opener}while(null!=b);b=!1}if(b&&(b=a.data,"string"===typeof b)){try{b=JSON.parse(b)}catch(d){return}b.command&&(c=this.connection,c.h||c.l("command",b.command,b.data,a.origin))}};
rn.prototype.D=function(){Ff(this.i);this.destination=null;L.prototype.D.call(this)};function sn(){L.call(this);this.i=[]}
v(sn,L);sn.prototype.D=function(){for(;this.i.length;){var a=this.i.pop();a.target.removeEventListener(a.name,a.wa)}L.prototype.D.call(this)};function tn(a){a=a||{};var b={},c={};this.url=a.url||"";this.args=a.args||kb(b);this.assets=a.assets||{};this.attrs=a.attrs||kb(c);this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
tn.prototype.clone=function(){var a=new tn,b;for(b in this)if(this.hasOwnProperty(b)){var c=this[b];"object"==Ia(c)?a[b]=kb(c):a[b]=c}return a};var un=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function vn(a){a=a||"";if(window.spf){var b=a.match(un);spf.style.load(a,b?b[1]:"",void 0)}else wn(a)}
function wn(a){var b=xn(a),c=document.getElementById(b),d=c&&Qm(c,"loaded");d||c&&!d||(c=yn(a,b,function(){Qm(c,"loaded")||(Om(c),Pg(b),Hf(Qa(Qg,b),0))}))}
function yn(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Sc(a);Sb(d,a);(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function xn(a){var b=Kc(document,"A");Rb(b,new Db(a,Eb));a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+$b(a)}
;function zn(a,b,c,d){L.call(this);var e=this;this.F=b;this.webPlayerContextConfig=d;this.ja=!1;this.api={};this.X=this.m=null;this.J=new M;this.i={};this.L=this.ca=this.elementId=this.ka=this.config=null;this.K=!1;this.l=this.B=null;this.da={};this.Ja=["onReady"];this.lastError=null;this.va=NaN;this.C={};this.Ka=new sn(this);this.N=0;this.j=this.o=a;Fd(this,Qa(Dd,this.J));An(this);Bn(this);Fd(this,Qa(Dd,this.Ka));c?this.N=Hf(function(){e.loadNewVideoConfig(c)},0):d&&(Cn(this),Dn(this))}
v(zn,L);m=zn.prototype;m.getId=function(){return this.F};
m.loadNewVideoConfig=function(a){if(!this.h){this.N&&(If(this.N),this.N=0);var b=a||{};b instanceof tn||(b=new tn(b));this.config=b;this.setConfig(a);Dn(this);this.isReady()&&En(this)}};
function Cn(a){var b,c;a.webPlayerContextConfig?c=a.webPlayerContextConfig.rootElementId:c=a.config.attrs.id;a.elementId=c||a.elementId;"video-player"===a.elementId&&(a.elementId=a.F,a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.F:a.config.attrs.id=a.F);(null===(b=a.j)||void 0===b?void 0:b.id)===a.elementId&&(a.elementId+="-player",a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.elementId:a.config.attrs.id=a.elementId)}
m.setConfig=function(a){var b;this.ka=a;this.config=Fn(a);Cn(this);this.ca||(this.ca=Gn(this,(null===(b=this.config.args)||void 0===b?void 0:b.jsapicallback)||"onYouTubePlayerReady"));this.config.args?this.config.args.jsapicallback=null:this.config.args={jsapicallback:null};var c;if(null===(c=this.config)||void 0===c?0:c.attrs)a=this.config.attrs,(c=a.width)&&this.j&&(this.j.style.width=Uc(Number(c)||c)),(a=a.height)&&this.j&&(this.j.style.height=Uc(Number(a)||a))};
function En(a){var b;a.config&&!0!==a.config.loaded&&(a.config.loaded=!0,!a.config.args||"0"!==a.config.args.autoplay&&0!==a.config.args.autoplay&&!1!==a.config.args.autoplay?a.api.loadVideoByPlayerVars(null!==(b=a.config.args)&&void 0!==b?b:null):a.api.cueVideoByPlayerVars(a.config.args))}
function Hn(a){var b=!0,c=In(a);c&&a.config&&(a=Jn(a),b=Qm(c,"version")===a);return b&&!!A("yt.player.Application.create")}
function Dn(a){if(!a.h&&!a.K){var b=Hn(a);if(b&&"html5"===(In(a)?"html5":null))a.L="html5",a.isReady()||Kn(a);else if(Ln(a),a.L="html5",b&&a.l&&a.o)a.o.appendChild(a.l),Kn(a);else{a.config&&(a.config.loaded=!0);var c=!1;a.B=function(){c=!0;var d=Mn(a,"player_bootstrap_method")?A("yt.player.Application.createAlternate")||A("yt.player.Application.create"):A("yt.player.Application.create");var e=a.config?Fn(a.config):void 0;d&&d(a.o,e,a.webPlayerContextConfig);Kn(a)};
a.K=!0;b?a.B():(Um(Jn(a),a.B),(b=Nn(a))&&vn(b),On(a)&&!c&&z("yt.player.Application.create",null,void 0))}}}
function In(a){var b=Gc(a.elementId);!b&&a.j&&a.j.querySelector&&(b=a.j.querySelector("#"+a.elementId));return b}
function Kn(a){var b;if(!a.h){var c=In(a),d=!1;c&&c.getApiInterface&&c.getApiInterface()&&(d=!0);d?(a.K=!1,!Mn(a,"html5_remove_not_servable_check_killswitch")&&(null===c||void 0===c?0:c.isNotServable)&&a.config&&(null===c||void 0===c?0:c.isNotServable(null===(b=a.config.args)||void 0===b?void 0:b.video_id))||Pn(a)):a.va=Hf(function(){Kn(a)},50)}}
function Pn(a){An(a);a.ja=!0;var b=In(a);if(b){a.m=Qn(a,b,"addEventListener");a.X=Qn(a,b,"removeEventListener");var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=a.api,e=0;e<c.length;e++){var f=c[e];d[f]||(d[f]=Qn(a,b,f))}}for(var g in a.i)a.i.hasOwnProperty(g)&&a.m&&a.m(g,a.i[g]);En(a);a.ca&&a.ca(a.api);a.J.U("onReady",a.api)}
function Qn(a,b,c){var d=b[c];return function(e){for(var f=[],g=0;g<arguments.length;++g)f[g-0]=arguments[g];try{return a.lastError=null,d.apply(b,f)}catch(h){"sendAbandonmentPing"!==c&&(h.params=c,a.lastError=h,Ok(h))}}}
function An(a){a.ja=!1;if(a.X)for(var b in a.i)a.i.hasOwnProperty(b)&&a.X(b,a.i[b]);for(var c in a.C)a.C.hasOwnProperty(c)&&If(Number(c));a.C={};a.m=null;a.X=null;b=a.api;for(var d in b)b.hasOwnProperty(d)&&(b[d]=null);b.addEventListener=function(e,f){a.addEventListener(e,f)};
b.removeEventListener=function(e,f){a.removeEventListener(e,f)};
b.destroy=function(){a.dispose()};
b.getLastError=function(){return a.getLastError()};
b.getPlayerType=function(){return a.getPlayerType()};
b.getCurrentVideoConfig=function(){return a.ka};
b.loadNewVideoConfig=function(e){a.loadNewVideoConfig(e)};
b.isReady=function(){return a.isReady()}}
m.isReady=function(){return this.ja};
function Bn(a){a.addEventListener("WATCH_LATER_VIDEO_ADDED",function(b){Pg("WATCH_LATER_VIDEO_ADDED",b)});
a.addEventListener("WATCH_LATER_VIDEO_REMOVED",function(b){Pg("WATCH_LATER_VIDEO_REMOVED",b)});
a.addEventListener("onAdAnnounce",function(b){Pg("a11y-announce",b)})}
m.addEventListener=function(a,b){var c=this,d=Gn(this,b);d&&(0<=Wa(this.Ja,a)||this.i[a]||(b=Rn(this,a),this.m&&this.m(a,b)),this.J.subscribe(a,d),"onReady"===a&&this.isReady()&&Hf(function(){d(c.api)},0))};
m.removeEventListener=function(a,b){this.h||(b=Gn(this,b))&&Ue(this.J,a,b)};
function Gn(a,b){var c=b;if("string"===typeof b){if(a.da[b])return a.da[b];c=function(d){for(var e=[],f=0;f<arguments.length;++f)e[f-0]=arguments[f];(f=A(b))&&f.apply(y,e)};
a.da[b]=c}return c?c:null}
function Rn(a,b){var c="ytPlayer"+b+a.F;a.i[b]=c;y[c]=function(d){var e=Hf(function(){if(!a.h){a.J.U(b,d);var f=a.C,g=String(e);g in f&&delete f[g]}},0);
hb(a.C,String(e))};
return c}
m.getPlayerType=function(){return this.L||(In(this)?"html5":null)};
m.getLastError=function(){return this.lastError};
function Ln(a){a.cancel();An(a);a.L=null;a.config&&(a.config.loaded=!1);var b=In(a);b&&(Hn(a)||!On(a)?a.l=b:(b&&b.destroy&&b.destroy(),a.l=null));if(a.o)for(a=a.o;b=a.firstChild;)a.removeChild(b)}
m.cancel=function(){this.B&&$m(Jn(this),this.B);If(this.va);this.K=!1};
m.D=function(){Ln(this);if(this.l&&this.config&&this.l.destroy)try{this.l.destroy()}catch(b){Pk(b)}this.da=null;for(var a in this.i)this.i.hasOwnProperty(a)&&(y[this.i[a]]=null);this.ka=this.config=this.api=null;delete this.o;delete this.j;L.prototype.D.call(this)};
function On(a){var b,c;a=null===(c=null===(b=a.config)||void 0===b?void 0:b.args)||void 0===c?void 0:c.fflags;return!!a&&-1!==a.indexOf("player_destroy_old_version=true")}
function Jn(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.jsUrl:(a=a.config.assets)?a.js:""}
function Nn(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.cssUrl:(a=a.config.assets)?a.css:""}
function Mn(a,b){var c;if(a.webPlayerContextConfig)var d=a.webPlayerContextConfig.serializedExperimentFlags;else if(null===(c=a.config)||void 0===c?0:c.args)d=a.config.args.fflags;return"true"===ag(d||"","&")[b]}
function Fn(a){for(var b={},c=u(Object.keys(a)),d=c.next();!d.done;d=c.next()){d=d.value;var e=a[d];b[d]="object"===typeof e?kb(e):e}return b}
;var Sn={},Tn="player_uid_"+(1E9*Math.random()>>>0);function Un(a,b,c){var d="player";c=void 0===c?!0:c;d="string"===typeof d?Gc(d):d;var e=Tn+"_"+La(d),f=Sn[e];if(f&&c)return Vn(a,b)?f.api.loadVideoByPlayerVars(a.args||null):f.loadNewVideoConfig(a),f.api;f=new zn(d,e,a,b);Sn[e]=f;Pg("player-added",f.api);Fd(f,function(){delete Sn[f.getId()]});
return f.api}
function Vn(a,b){return b&&b.serializedExperimentFlags?b.serializedExperimentFlags.includes("web_player_remove_playerproxy=true"):a&&a.args&&a.args.fflags?a.args.fflags.includes("web_player_remove_playerproxy=true"):!1}
;var Wn=null,Xn=null,Yn=null;function Zn(){var a=Wn.getVideoData(1);a=a.title?a.title+" - YouTube":"YouTube";document.title!==a&&(document.title=a)}
;function $n(a,b,c){a="ST-"+$b(a).toString(36);b=b?ec(b):"";c=c||5;var d=cd.get("CONSENT",void 0);d&&!d.startsWith("YES+")||rh(a,b,c)}
;function ao(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=F("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){d=a;var e=void 0===e?!0:e;var f=F("VALID_SESSION_TEMPDATA_DOMAINS",[]),g=cc(window.location.href);g&&f.push(g);g=cc(d);if(0<=Wa(f,g)||!g&&0==d.lastIndexOf("/",0))if(Q("autoescape_tempdata_url")&&(f=document.createElement("a"),Rb(f,d),d=f.href),d){g=d.match(ac);d=g[5];f=g[6];g=g[7];var h="";d&&(h+=d);f&&(h+="?"+f);g&&(h+="#"+g);d=h;f=d.indexOf("#");if(d=0>f?d:d.substr(0,f))if(e&&!b.csn&&(b.itct||b.ved)&&
(b=Object.assign({csn:Bl()},b)),k){var k=parseInt(k,10);isFinite(k)&&0<k&&$n(d,b,k)}else $n(d,b)}}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var l=void 0===l?{}:l;var p=void 0===p?"":p;var n=void 0===n?window:n;c=n.location;a=fc(a,l)+p;a=a instanceof Db?a:Jb(a);c.href=Fb(a)}return!0}
;z("yt.setConfig",N,void 0);z("yt.config.set",N,void 0);z("yt.setMsg",tf,void 0);z("yt.msgs.set",tf,void 0);z("yt.logging.errors.log",Pk,void 0);
z("writeEmbed",function(){var a=F("PLAYER_CONFIG",void 0);if(!a){var b=F("PLAYER_VARS",void 0);b&&(a={args:b})}ol(!0);"gvn"===a.args.ps&&(document.body.style.backgroundColor="transparent");a.attrs||(a.attrs={width:"100%",height:"100%",id:"video-player"});var c=document.referrer;b=F("POST_MESSAGE_ORIGIN");window!==window.top&&c&&c!==document.URL&&(a.args.loaderUrl=c);F("EXPERIMENT_FLAGS").embeds_js_api_set_1p_cookie&&(c=fg(),c.embedsTokenValue&&(a.args.embedsTokenValue=c.embedsTokenValue));F("EXPERIMENT_FLAGS").embeds_web_force_csi_on_gel&&
N("FORCE_CSI_ON_GEL",!0);c=["ol"];km("").info.actionType="embed";c&&N("TIMING_AFT_KEYS",c);N("TIMING_ACTION","embed");c=F("TIMING_INFO",{});for(var d in c)c.hasOwnProperty(d)&&Am(d,c[d]);Am("is_nav",1);(d=Bl())&&Am("csn",d);(d=F("PREVIOUS_ACTION",void 0))&&!vm()&&Am("pa",d);d=fm();c=F("CLIENT_PROTOCOL");var e=F("CLIENT_TRANSPORT");c&&Am("p",c);e&&Am("t",e);Am("yt_vis",Fm());Am("yt_lt","cold");c=bm();if(e=dm())Z("srt",c.responseStart),1!==d.prerender&&(Am("yt_sts","n",void 0),Z("_start",e,void 0));
d=im();0<d&&Z("fpt",d);if(!Q("log_deltas_killswitch")){var f,g,h,k;W&&W.timing&&(W.timeOrigin&&W.timing.navigationStart&&Cm("startTimeDelta",Math.floor(W.timeOrigin)-W.timing.navigationStart),(d=null===(k=null===(h=null===(g=null===(f=W.getEntriesByType)||void 0===f?void 0:f.call(W,"navigation"))||void 0===g?void 0:g[0])||void 0===h?void 0:h.toJSON)||void 0===k?void 0:k.call(h))&&d.responseEnd&&W.timing.responseEnd&&Cm("responseEndDelta",cm(d.responseEnd)-W.timing.responseEnd))}f=bm();f.isPerformanceNavigationTiming&&
Am("pnt",1,void 0);Z("nreqs",f.requestStart,void 0);Z("nress",f.responseStart,void 0);Z("nrese",f.responseEnd,void 0);0<f.redirectEnd-f.redirectStart&&(Z("nrs",f.redirectStart,void 0),Z("nre",f.redirectEnd,void 0));0<f.domainLookupEnd-f.domainLookupStart&&(Z("ndnss",f.domainLookupStart,void 0),Z("ndnse",f.domainLookupEnd,void 0));0<f.connectEnd-f.connectStart&&(Z("ntcps",f.connectStart,void 0),Z("ntcpe",f.connectEnd,void 0));f.secureConnectionStart>=dm()&&0<f.connectEnd-f.secureConnectionStart&&(Z("nstcps",
f.secureConnectionStart,void 0),Z("ntcpe",f.connectEnd,void 0));W&&W.getEntriesByType&&Hm();f=[];if(document.querySelector&&W&&W.getEntriesByName)for(var l in Zl)Zl.hasOwnProperty(l)&&(g=Zl[l],Gm(l,g)&&f.push(g));f.length&&Am("rc",f.join(","));if(vm(void 0)){l={actionType:pm[F("TIMING_ACTION",void 0)]||"LATENCY_ACTION_UNKNOWN",previousAction:pm[F("PREVIOUS_ACTION",void 0)]||"LATENCY_ACTION_UNKNOWN"};if(f=Bl())l.clientScreenNonce=f;f=gm(void 0);nm().info(l,f)}l=fm();g=am();if("cold"===l.yt_lt&&(f=
xm(),h=f.gelTicks?f.gelTicks:f.gelTicks={},f=f.gelInfos?f.gelInfos:f.gelInfos={},vm())){for(var p in g)"tick_"+p in h||wm(p,g[p]);p=zm();g=gm();h={};for(var n in l)"info_"+n in f||!(k=ym(n,l[n]))||(Nl(p,k),Nl(h,k));nm().info(h,g)}z("ytglobal.timingready_",!0,void 0);Bm();(n=F("WEB_PLAYER_CONTEXT_CONFIGS",void 0))&&"WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER"in n?(n=n.WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER,n.serializedForcedExperimentIds||(p=fg(),p.forced_experiments&&(n.serializedForcedExperimentIds=
p.forced_experiments)),Wn=Un(a,n,!1)):Wn=Un(a);Wn.addEventListener("onVideoDataChange",Zn);a=F("POST_MESSAGE_ID","player");F("ENABLE_JS_API")?Yn=new $k(Wn):F("ENABLE_POST_API")&&"string"===typeof a&&"string"===typeof b&&(Xn=new rn(window.parent,a,b),Yn=new on(Wn,Xn.connection));cn();F("EXPERIMENT_FLAGS").networkless_logging_web_embedded&&ik()},void 0);
var bo=pf(function(){Dm();var a=th.getInstance(),b=!!((wh("f"+(Math.floor(119/31)+1))||0)&67108864),c=1<window.devicePixelRatio;if(document.body&&Id(document.body,"exp-invert-logo"))if(c&&!Id(document.body,"inverted-hdpi")){var d=document.body;if(d.classList)d.classList.add("inverted-hdpi");else if(!Id(d,"inverted-hdpi")){var e=Gd(d);Hd(d,e+(0<e.length?" inverted-hdpi":"inverted-hdpi"))}}else!c&&Id(document.body,"inverted-hdpi")&&Jd();if(b!=c){b="f"+(Math.floor(119/31)+1);d=wh(b)||0;d=c?d|67108864:
d&-67108865;0==d?delete sh[b]:(c=d.toString(16),sh[b]=c.toString());c=!0;Q("web_secure_pref_cookie_killswitch")&&(c=!1);b=a.h;d=[];for(var f in sh)d.push(f+"="+encodeURIComponent(String(sh[f])));rh(b,d.join("&"),63072E3,a.i,c)}Jm.h||(Jm.h=new Jm);a=Jm.h;f=16623;var g=void 0===g?{}:g;Object.values(Rk).includes(f)||(Ok(new fi("createClientScreen() called with a non-page VE",f)),f=83769);g.isHistoryNavigation||a.h.push({rootVe:f,key:g.key||""});a.l=[];a.u=[];g.za?Mm(a,f,g):Nm(a,f,g)}),co=pf(function(){Wn&&
Wn.sendAbandonmentPing&&Wn.sendAbandonmentPing();
F("PL_ATT")&&hn.dispose();for(var a=0,b=an.length;a<b;a++)Qf(an[a]);an.length=0;Zm("//static.doubleclick.net/instream/ad_status.js");bn=!1;N("DCLKSTAT",0);Ed(Yn,Xn);Wn&&(Wn.removeEventListener("onVideoDataChange",Zn),Wn.destroy())});
window.addEventListener?(window.addEventListener("load",bo),window.addEventListener("unload",co)):window.attachEvent&&(window.attachEvent("onload",bo),window.attachEvent("onunload",co));Ra("yt.abuse.player.botguardInitialized",A("yt.abuse.player.botguardInitialized")||jn);Ra("yt.abuse.player.invokeBotguard",A("yt.abuse.player.invokeBotguard")||kn);Ra("yt.abuse.dclkstatus.checkDclkStatus",A("yt.abuse.dclkstatus.checkDclkStatus")||dn);
Ra("yt.player.exports.navigate",A("yt.player.exports.navigate")||ao);Ra("yt.util.activity.init",A("yt.util.activity.init")||Sf);Ra("yt.util.activity.getTimeSinceActive",A("yt.util.activity.getTimeSinceActive")||Vf);Ra("yt.util.activity.setTimestamp",A("yt.util.activity.setTimestamp")||Tf);}).call(this);
