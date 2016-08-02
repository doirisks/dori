/**
 * riskfactors_table
 * 
 * class to write and maintain the risk factors table (risk factors in use)
 **/

function riskfactor_list(master) {
    this.master = master;
    
    this.base = document.createElement("div");
    this.base.setAttribute("style","width:400px");
    
    var removetitle = $("<div style='float:left; width:30px; display:block; overflow:hidden'></div>");
    removetitle.append($('<p></p>'));
    var nametitle = $("<div style='float:left; width:150px; display:block; overflow:hidden'></div>"); 
    nametitle.append($('<p>Risk Factor</p>'));
    var inputtitle = $("<div style='float:left; width:120px; display:block; overflow:hidden'></div>"); 
    inputtitle.append($('<p>Input</p>'));
    var unitstitle = $("<div style='width:50px; display:block; overflow:hidden'></div>"); 
    unitstitle.append($('<p>Units</p>'));
    
    var titlebar = $("<div style='float:clear'></div>");
    titlebar.append(removetitle);
    titlebar.append(nametitle);
    titlebar.append(inputtitle);
    titlebar.append(unitstitle);
    
    $(this.base).append(titlebar);
    
    // buttons, names, inputs, and units lists
    this.buttons = $("<div style='float:left; width:30px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    this.names = $("<div style='float:left; width:150px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    this.values = $("<div style='float:left; width:120px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    this.unit_names = $("<div style='width:50px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    
    var holder = $("<div style='float:clear'></div>");
    
    $(holder).append(this.buttons);
    $(holder).append(this.names);
    $(holder).append(this.values);
    $(holder).append(this.unit_names);
    $(this.base).append(holder);
    
    // the most recent addition
    this.head = null;
    
    // makes a CUI visible in the table
    this.push = function (CUI_obj) {
        CUI_obj.show(this, this.head);
        this.head = CUI_obj;
    }
    
    // remove a CUI from the table
    this.pop = function (CUI_obj) {
        if (this.head == CUI_obj) {
            this.head = CUI_obj.prev;
        }
        CUI_obj.remove();
    }
}
