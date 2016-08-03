/**
 * models_table
 * 
 * class to write and maintain the models table (active models)
 **/

function model_list(master) {
    // identify the master
    this.master = master;
    
    this.all_models = {};   // all models (data)
    this.vis_models = [];   // currently visible models
    
    
    this.base = document.createElement("div");
    this.base.setAttribute("style","width:400px");
    
    //titlebar
    
    var titletitle = $("<div style='float:left; width:300px; display:block; overflow:hidden;'></div>");
    titletitle.append($('<p>Models</p>'));
    var scoretitle = $("<div style='float:left; width:75px; display:block;'></div>"); 
    scoretitle.append($('<p>Score</p>'));
    
    var titlebar = $("<div style='float:clear'></div>");
    titlebar.append(titletitle);
    titlebar.append(scoretitle);
    
    $(this.base).append(titlebar);
    
    // titles and scores lists
    this.titles = $("<div style='float:left; width:300px; display:block; overflow:hidden'></div>"); 
    this.scores = $("<div style='width:75px; display:block; overflow:hidden'></div>"); 
    
    $(this.base).append(this.titles);
    $(this.base).append(this.scores);
    
    // the most recent addition
    this.head = null;
    
    // makes a CUI visible in the table
    this.push = function (model_obj) {
        model_obj.show(this, this.head);
        this.head = model_obj;
    }
    
    // remove a CUI from the table
    this.pop = function (model_obj) {
        if (this.head == model_obj) {
            this.head = model_obj.prev;
        }
        model_obj.remove();
    }
    
    this.fetchmodels = function(CUIs, vis = true) {
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
                                master.push(master.all_models[id]["local_obj"]);
                            }
                        }
                        
                    });
                }
                
                // TODO make models visible as appropriate
                
            }
        });
    }
}
