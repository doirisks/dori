/**
 * models_finder
 * 
 * class to hold the search for new models
 **/
function models_finder(master) {
    this.id = "newmodel";
    this.master = master;
    var text = "        <form> <!-- add a new risk factor -->\n";
    text    += '            <span class="searchform">\n';
    text    += '                <span><b>Search for Models</b></span>\n';
    text    += '                <div>\n';
    text    += '                    <span><button id="'+this.id+'" onclick="the_interface.fetchmodels">Find</button></span>\n';
    text    += '                    <span><input type="text" name="search"  style="text-align:center;width:100px"></input></span>\n';
    text    += '                </div>\n';
    text    += '            </span>\n';
    text    += '        </form>\n';
    this.base = text;
}
