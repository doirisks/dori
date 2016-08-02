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
    this.modellist  =  new model_list(this);
    this.modelfinder = new model_finder(this);
    // the right side of the interface - risk factors
    this.CUIlist  =  new riskfactor_list(this);
    this.CUIfinder = new riskfactor_finder(this);
    
    // the base text of the interface
    this.base = document.createElement("div");
    var left  = document.createElement("div");
    var right = document.createElement("div");
    this.base.setAttribute("style","width:800px;overflow:hidden;");
    left.setAttribute("style", "width:400px;overflow:hidden;border:1px solid;float:left;");
    right.setAttribute("style","width:400px;overflow:hidden;border:1px solid;");
    
    var modeltitle = document.createElement('h4')
    modeltitle.appendChild(document.createTextNode("Models"));
    left.appendChild(modeltitle);
    left.appendChild(this.modellist.base);
    left.appendChild(this.modelfinder.base);
    var rftitle = document.createElement('h4')
    rftitle.appendChild(document.createTextNode("Risk Factors"));
    right.appendChild(rftitle);
    right.appendChild(this.CUIlist.base);
    right.appendChild(this.CUIfinder.base);
    
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
                    master.vis_CUIs.push(CUI); 
                    master.CUIlist.push(master.all_CUIs[CUI]["local_obj"]);
                }
            });
            // TODO add a memory variable to make sure that the CUIs are added in the right order
        } else if ( this.all_CUIs[CUI]['CUI'] == CUI ) {
            // browser already has CUI data, but it is hidden => unhide it!
            this.vis_CUIs.push(CUI);
            this.update();
        } else {
            // do nothing - CUI is either being gotten already or it is bad
        }
    }
    
    this.fetchmodels = function(vis = true) {
        var CUIs = this.getInputData();
        // request to check for new models
        $.ajax({
            url : "api/model/by_riskfactors/", 
            data : CUIs,
            master : this, 
            headers: {"Content-Type": "application/json"},
            success: function(reply) {
                console.log("model request succeeded");
                // store the pertinent pointer
                var master = this.master; 
                
                // parse the reply
                var data = JSON.parse(reply);
                
                // identify new ids
                var new_ids = [];
                for (id in data) {
                    // log any error messages
                    if (id == "error") {
                        console.log("error: " + data["error"]);
                    }
                    else if ( !(id in master.all_models) ) {
                        new_ids.push(id);
                    }
                }
                if (new_ids.length > 0 ) {
                    // request to find data and add it to all_models
                    $.ajax({
                        url : "api/model/by_id",
                        data : {"ids" : new_ids},
                        master: master,
                        headers: {"Content-Type": "application/json"},
                        success: function(reply) {
                            // store the pertinent pointer
                            var master = this.master; 
                            
                            // parse the reply
                            var data = JSON.parse(reply);
                            
                            // store data on all newly acquired models
                            // TODO find a way to prevent extraneous multi-requesting of the same models
                            // TODO maybe just make a variable whole_interface.requesting models that 
                            // TODO will stall requests...
                            for (id in data) {
                                if (!(id in master.all_models)) {
                                    // parse the json encoded fields from the db
                                    data[id]['authors'] = JSON.parse(data[id]['authors']);
                                    data[id]['inpCUI'] = JSON.parse(data[id]['inpCUI']);
                                    data[id]['inpname'] = JSON.parse(data[id]['inpname']);
                                    data[id]['inpdatatype'] = JSON.parse(data[id]['inpdatatype']);
                                    data[id]['upper'] = JSON.parse(data[id]['upper']);
                                    data[id]['lower'] = JSON.parse(data[id]['lower']);
                                    
                                    master.all_models[id] = data[id];
                                    master.all_models[id]["local_obj"] = new model_single(master, id);
                                }
                                // show the model
                                master.vis_models.push(id); 
                                master.modellist.push(master.all_models[id]["local_obj"]);
                            }
                        }
                        
                    });
                }
                
                // TODO make models visible as appropriate
                
            }
        });
    }
    
    this.getInputData = function() {
        var data = {};
        for (i in this.vis_CUIs) {
            var obj = this.all_CUIs[this.vis_CUIs[i]]["local_obj"];
            data[this.vis_CUIs[i]] = obj.getVal();
        }
        return(data);
    }
    
    this.base.appendChild(left);
    this.base.appendChild(right);
    $('#'+own_div_id).append(this.base);
    
    // iterate through given risk factors and add them
    for (CUI in init_riskfactors) {
        this.fetchCUI(CUI);
    }
}



// document.ready
$(document).ready( function () {
    the_interface = new whole_interface("main", riskfactors);
});
