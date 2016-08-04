/**
 * riskfactors_table
 * 
 * class to write and maintain the risk factors table (risk factors in use)
 **/

function riskfactor_list(master) {
    this.master = master;
    
    
    this.all_CUIs = {};    // all data stored on CUIs 
    this.vis_CUIs = [];    // list of visible CUIs
    
    
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
        this.vis_CUIs.push(CUI_obj.CUI); 
        CUI_obj.show(this, this.head);
        this.head = CUI_obj;
    }
    
    // remove a CUI from the table
    this.pop = function (CUI_obj) {
        // TODO make it so that the entire list is not rebuilt every time...
        var CUI = CUI_obj.CUI;
        var vis_CUIs = [];
        for (var i in this.vis_CUIs) {
            if (this.vis_CUIs[i] != CUI) {
                vis_CUIs.push(this.vis_CUIs[i]);
            }
        }
        this.vis_CUIs = vis_CUIs;
        
        if (this.head == CUI_obj) {
            this.head = CUI_obj.prev;
        }
        CUI_obj.hide();
    }
    
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
                    // store the pertinent pointer
                    var master = this.master; 
                    
                    // parse the reply
                    var data = JSON.parse(reply);
                    var CUI = Object.keys(data)[0];
                    
                    // store the data in the all_CUIs array
                    master.all_CUIs[CUI] = data[CUI]; 
                    master.all_CUIs[CUI]["local_obj"] = new riskfactor_single(master, CUI); 
                    
                    // show the CUI
                    if (vis) {
                        master.push(master.all_CUIs[CUI]["local_obj"]);
                    }
                }
            });
            // TODO add a memory variable to make sure that the CUIs are added in the right order
        } else if ( this.all_CUIs[CUI]['CUI'] == CUI ) {
            // browser already has CUI data, but it is hidden => unhide it!
            this.vis_CUIs.push(CUI);
            this.all_CUIs[CUI]['local_obj'].show();
        } else {
            // do nothing - CUI is either being gotten already or it is bad
        }
    }
    
    // get data from inputs
    this.getInputData = function() {
        var data = {};
        for (var i in this.vis_CUIs) {
            var CUI = this.vis_CUIs[i];
            var obj = this.all_CUIs[CUI]["local_obj"];
            data[CUI] = obj.getVal();
        }
        return(data);
    }
}
