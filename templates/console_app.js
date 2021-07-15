var stdIn = $("#std-in")[0];
var stdOut = $("#std-out")[0];
var script_data = {input_code: ''};
var run_button = $("#run")[0];
var Compiler = 'https://circuitalminds-storage-app.herokuapp.com/console_app';


run_button.onclick = function () {
	input_code = '';
	lines = stdIn.childNodes;
	for ( line of lines ) {
		line_code = line.textContent;
		if ( line_code != '' ) {
            input_code += line.textContent + ';';
		};
	};
	script_data.input_code = input_code;
	var getOutput = $.get( Compiler, script_data );
    getOutput.done( function( data )  {
        code_lines = data['std_out'];
        console.log(code_lines);
        Out_Template(code_lines);
    });
};

function Out_Template ( code_lines ) {
    date = Date().split(" ");
    out_line = date[1] + ' / ' + date[2] + ' / ' + date[3] + ' | ' + date[4] + ' >>> Output [#]: CODE';
    html_line = function ( line_index, code_line ) {
        console.log( line_index, code_line );
        return out_line.replace('#', stdOut.childNodes.length + line_index).replace('CODE', code_line);
    };
    for ( var n = 0; n < code_lines.length; n++ ) {
        if ( code_lines[n] != '' ) {
            line = document.createElement('p');
            line.innerHTML = html_line(n, code_lines[n]);
            stdOut.appendChild(line);
        };
    };
};
