/**
 * riskfactors_table
 * 
 * class to write and maintain the risk factors table (risk factors in use)
 **/

function riskfactor_list(master) {
    this.master = master;
    
    this.base = document.createElement("div");
    this.base.setAttribute("style","width:400px");
    
    //titlebar
    var removetitle = document.createElement("p");
    titletitle.setAttribute("style","width:30px;text-align:center;float:left;");
    scoretitle.appendChild(docuemnt.createTextNode("Models");
    var nametitle = document.createElement("p");
    scoretitle.setAttribute("style","width:150px;text-align:center;");
    scoretitle.appendChild(docuemnt.createTextNode("Scores");
    var inputtitle = document.createElement("p");
    scoretitle.setAttribute("style","width:120px;text-align:center;");
    scoretitle.appendChild(docuemnt.createTextNode("Scores");
    var unitstitle = document.createElement("p");
    scoretitle.setAttribute("style","width:50px;text-align:center;");
    scoretitle.appendChild(docuemnt.createTextNode("Units");
    var titlebar = document.createElement("span");
    titlebar.setAttribute("style","width:400px");
    titlebar.appendChild(removetitle);
    titlebar.appendChild(namestitle);
    titlebar.appendChild(inputtitle);
    titlebar.appendChild(unitstitle);
    
    this.base.append(titlebar);
    
    // buttons, names, inputs, and units lists
    this.buttons = $("<div style='float:left; width:30px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    this.names = $("<div style='float:left; width:150px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    this.values = $("<div style='float:left; width:120px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    this.unit_names = $("<div style='width:50px; display:block; overflow:hidden'></div>"); //document.createElement('span');
    
    this.base.append(this.buttons);
    this.base.append(this.names);
    this.base.append(this.values);
    this.base.append(this.unit_names);
    
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
