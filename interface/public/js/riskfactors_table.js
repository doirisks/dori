/**
 * riskfactors_table
 * 
 * class to write and maintain the risk factors table (risk factors in use)
 **/

function riskfactors_table(master) {
    this.master = master;
    var text = "            <form id = 'riskfactors' style='width:400px'>\n";
    // TODO make cell formats into a css class
    text    += '                <span id="riskfactortitles" style="width:300px"> <span style="width:20px"></span> <span style="width:180px">Risk Factor</span> <span style="width:50px"><p>Value</p></span> <span style="width:50px">Units</span> </span>';
    text    += '                <div id="allriskfactors" class="wrapper"></div>\n';
    text    += '                <!-- risk factor inputs added by getrisk.js -->\n';
    text    += '            </form>\n';
    this.base = text;
    
    this.buttons = $("<div style='float:left; width:30px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    this.names = $("<div style='float:left; width:150px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    this.values = $("<div style='float:left; width:120px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    this.unit_names = $("<div style='style='width:50px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    
    // the most recent addition
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
