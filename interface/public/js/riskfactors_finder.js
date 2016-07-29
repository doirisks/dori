/**
 * riskfactors_finder
 * 
 * class to hold the search for new models
 **/
function riskfactors_finder(master) {
    this.id = "newriskfactor";
    this.master = master;
    var text = "            <form id = 'newriskfactor'> <!-- add a new risk factor -->\n";
    text    += '                <span class="searchform">\n';
    text    += '                    <span><b>Search for Risk Factors</b></span>\n';
    text    += '                    <div>\n';
    text    += '                        <span><button>Add</button></span>\n';
    text    += '                        <span><input type="text" name="search"  style="text-align:center;width:100px"></input></span>\n';
    text    += '                    </div>\n';
    text    += '                </span>\n';
    text    += '            </form>\n';
    this.base = text;
}
