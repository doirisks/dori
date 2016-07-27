/**
 * main.js
 *
 * js classes and procedures for the main demo interface
 */



/**
 * whole_interface
 * 
 * class to write and maintain the main div of the doirisks interface
 **/

function whole_interface(own_div_id, init_riskfactors = []) {
    // the id of the div where the interface will be placed
    this.own_div_id = own_div_id;
    
    // all data stored on models and CUIs 
    this.all_models = {};
    this.all_CUIs = {};
    
    // list of visible models and CUIs
    vis_models = [];
    vis_CUIs = [];
    
    // the left side of the interface - models
    this.left = new models_interface(this);
    // the right side of the interface - risk factors
    this.right = new riskfactors_interface(this, init_riskfactors);
    
    // the base text of the interface
    var text = '<table class="table-condensed" ><tr>\n'
    text    += '    <td style="vertical-align:Top;border:1px solid">\n';
    text    += this.left.base;
    text    += '    </td>\n';
    text    += '    <td style="vertical-align:Top;border:1px solid">\n';
    text    += this.right.base;
    text    += '    </td>\n';
    text    += '</tr></table>\n';
    this.base = text;
    
    // add a CUI
    this.addCUI = function (CUI, vis = true) {
        // TODO
    }
    
    // update procedure
    this.update = function() {
        // TODO
    }
    
    $('#'+own_div_id).html(this.base);
    // iterate through given risk factors and add them
    for (i in init_riskfactors) {
        this.addCUI(init_riskfactors[i]);
    }
    this.update();
}

/**
 * models_interface
 * 
 * class to write and maintain the models half of the main div of the doirisks interface
 **/

function models_interface(master) {
    this.table = new models_table(this);
    this.finder = new models_finder(this);
    var text = '        <h4 >Models</h4>\n';
    text    += this.table.base;
    text    += '        <br>\n';
    text    += this.finder.base;
    this.base = text;
}

/**
 * riskfactors_interface
 * 
 * class to write and maintain the risk factors half of the main div of the doirisks interface
 **/

function riskfactors_interface(master, init_riskfactors) {
    this.table = new riskfactors_table(this);
    this.finder = new riskfactors_finder(this);
    var text = '        <h4>Risk Factors</h4>\n';
    text    += '        <div>\n';
    text    += this.table.base;
    text    += '            <br>\n';
    text    += this.finder.base;
    text    += '        </div>\n';
    this.base = text;
}

/**
 * models_table
 * 
 * class to write and maintain the models table (active models)
 **/

function models_table(master) {
    var text = "        <div id = 'models'>\n";
    text    += '            <!-- available models are added here -->\n';
    text    += '        </div>\n';
    this.base = text;
}

/**
 * riskfactors_table
 * 
 * class to write and maintain the risk factors table (risk factors in use)
 **/

function riskfactors_table(master) {
    var text = "            <form id = 'riskfactors' >\n";
    text    += '                <!-- risk factor inputs added by getrisk.js -->\n';
    text    += '            </form>\n';
    this.base = text;
    
    // makes a CUI visible in the table
    this.push = function (CUI) {
        //TODO
    }
    
    // remove a CUI from the table
    this.pop = function (CUI) {
    
    }
}

/**
 * models_finder
 * 
 * class to hold the search for new models
 **/
function models_finder(master) {
    var text = "        <form id = 'newmodel'> <!-- add a new risk factor -->\n";
    text    += '            <span class="searchform">\n';
    text    += '                <span><b>Search for Models</b></span>\n';
    text    += '                <div>\n';
    text    += '                    <span><button>Find</button></span>\n';
    text    += '                    <span><input type="text" name="search"  style="text-align:center;width:100px"></input></span>\n';
    text    += '                </div>\n';
    text    += '            </span>\n';
    text    += '        </form>\n';
    this.base = text;
}

/**
 * riskfactors_finder
 * 
 * class to hold the search for new models
 **/
function riskfactors_finder(master) {
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

// document.ready
$(document).ready( function () {
    the_interface = new whole_interface("main");
});
