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
    this.vis_models = [];
    this.vis_CUIs = [];
    
    // the left side of the interface - models
    this.lefttable  =  new models_table(this);
    this.leftfinder = new models_finder(this);
    // the right side of the interface - risk factors
    this.righttable  =  new riskfactors_table(this);
    this.rightfinder = new riskfactors_finder(this);
    
    // the base text of the interface
    var text = '<table class="table-condensed" ><tr>\n'
    text    += '    <td style="vertical-align:Top;border:1px solid">\n';
    
    // left interface
    text    += '        <h4 >Models</h4>\n';
    text    += this.lefttable.base;
    text    += '        <br>\n';
    text    += this.leftfinder.base;
    
    text    += '    </td>\n';
    text    += '    <td style="vertical-align:Top;border:1px solid">\n';
    
    // right interface
    text    += '        <h4>Risk Factors</h4>\n';
    text    += '        <div>\n';
    text    += this.righttable.base;
    text    += '            <br>\n';
    text    += this.rightfinder.base;
    text    += '        </div>\n';
    
    text    += '    </td>\n';
    text    += '</tr></table>\n';
    this.base = text;
    
    // add a CUI
    this.fetchCUI = function (CUI, vis = true) {
        // try to fetch the CUI
        if (this.all_CUIs[CUI] == null){
            // fetch and handle data from server
            this.all_CUIs[CUI] = $.ajax({
                url : "api/cui/by_cui/", 
                data : {"CUIs": [CUI]},
                master : this, 
                headers: {"Content-Type": "application/json"},
                success: function(reply) {
                    // store the pertinent pointers
                    var master = this.master; 
                    
                    // parse the reply
                    var data = JSON.parse(reply);
                    var CUI = Object.keys(data)[0];
                    
                    // store the data in the all_CUIs array
                    master.all_CUIs[CUI] = data[CUI]; 
                    master.all_CUIs[CUI]["local_obj"] = new riskfactors_single(master, CUI); 
                    
                    // show the CUI
                    master.vis_CUIs.push(CUI); 
                    master.update(); 
                }
            });
        } else if ( this.all_CUIs[CUI]['CUI'] == CUI ) {
            // browser already has CUI data, but it is hidden => unhide it!
            this.vis_CUIs.push(CUI);
            this.update();
        } else {
            // do nothing - CUI is either being gotten already or it is bad
        }
    }
    
    // update procedure
    this.update = function() {
        // temporary procedure: just show all of the data
        for (i in this.vis_CUIs) {
            this.righttable.push(this.all_CUIs[this.vis_CUIs[i]]["local_obj"]);
        }
        // TODO
    }
    
    $('#'+own_div_id).html(this.base);
    // iterate through given risk factors and add them
    for (CUI in init_riskfactors) {
        this.fetchCUI(CUI);
    }
}

/**
 * models_table
 * 
 * class to write and maintain the models table (active models)
 **/

function models_table(master) {
    this.master = master;
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
    this.master = master;
    var text = "            <form id = 'riskfactors' >\n";
    text    += '                <!-- risk factor inputs added by getrisk.js -->\n';
    text    += '            </form>\n';
    this.base = text;
    
    // the most 
    this.head = null;
    
    // makes a CUI visible in the table
    this.push = function (CUI_obj) {
        CUI_obj.show(this.head);
        this.head = CUI_obj;
    }
    
    // remove a CUI from the table
    this.pop = function (CUI_obj) {
        CUI_obj.remove();
    }
}

/**
 * models_finder
 * 
 * class to hold the search for new models
 **/
function models_finder(master) {
    this.master = master;
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

/**
 * riskfactors_finder
 * 
 * class to hold the search for new models
 **/
 
function models_single(master, model, vis = true) {
    var text = ""; //TODO
    this.text = text;
   
    // previous and next in the table
    this.prev = null;
    this.next = null;
    
    this.show = function (prev) {
        // adjust place in list
        this.prev = prev;
        if (prev != null && prev.next != null) {
            this.next = prev.next;
        }
        prev.next = this;
        
        // show in html
        $("#" + prev.id).after(this.content);
    }
}

/**
 * riskfactors_finder
 * 
 * class to hold the search for new models
 **/
 
function riskfactors_single(master,CUI) {
    this.master = master;
    this.CUI = CUI;
    this.id = CUI;
    this.vis = false;
    //TODO this.datatype = master.;
    
    //TODO this.val = ;
    
    var text = '                <div id="' + this.id + '">\n';
    text    += "                    <p>TESTING 1, 2... " + master.all_CUIs[CUI]["name1"] + "</p>\n"; //temporary filler text
    text    += "                </div>\n";
    this.content = text;
    
    // previous and next in the table
    this.prev = null;
    this.next = null;
   
    this.show = function (prev) {
        if (!this.vis) {
            // adjust list pointers
            this.prev = prev;
            if (prev != null && prev.next != null) {
                this.next = prev.next;
            }
            if (prev != null) {
                prev.next = this;
            }
            
            // show in html
            if (prev == null){
                $("#riskfactors").html(this.content);
            }
            else {
                $("#" + prev.id).after(this.content);
            }
            this.vis = true;
        }
    }
    
    this.hide = function () {
        if (this.vis) {
            // adjust list pointers
            if (this.prev !== null) {
                this.prev.next = this.next;
            }
            if (this.next !== null) {
                this.next.prev = this.prev;
            }
            else {
                // change head of table if appropriate
                master.righttable.head = this.prev;
            }
            
            // remove html
            $("#" + this.id).remove()
            this.vis = false;
        }
    }
    
    this.getVal = function () {
        //TODO
    }
}

// document.ready
$(document).ready( function () {
    the_interface = new whole_interface("main", riskfactors);
});
