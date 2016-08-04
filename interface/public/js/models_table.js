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
    scoretitle.append($('<button>Score</button>'));
    var _this = this;
    scoretitle.click(function() {
        _this.master.scoremodels();
    });
    
    var titlebar = $("<div style='height:30px;float:clear'></div>");
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
    
    // makes a model visible in the table
    this.push = function (model_obj) {
        this.vis_models.push(model_obj.model); 
        model_obj.show(this, this.head);
        this.head = model_obj;
    }
    
    // remove a model from the table
    this.pop = function (model_obj) {
        var index = this.vis_models.indexOf(model_obj);
        if (index > -1) {
            this.vis_models.splice(index, 1); 
        }
        
        if (this.head == model_obj) {
            this.head = model_obj.prev;
        }
        
        model_obj.remove();
    }
    
    // get models from the server based on data
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
                var supported_models = {};
                var new_ids = [];
                for (var id in data) {
                    supported_models[id] = true;
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
                            for (var id in data) {
                                if (!(id in master.all_models)) {
                                    // parse the json encoded fields from the db
                                    data[id]['authors'] = JSON.parse(data[id]['authors']);
                                    data[id]['inpCUI'] = JSON.parse(data[id]['inpCUI']);
                                    data[id]['inpname'] = JSON.parse(data[id]['inpname']);
                                    data[id]['inpdatatype'] = JSON.parse(data[id]['inpdatatype']);
                                    data[id]['upper'] = JSON.parse(data[id]['upper']);
                                    data[id]['lower'] = JSON.parse(data[id]['lower']);
                                    data[id]['mustnotCUI'] = JSON.parse(data[id]['mustnotCUI']);
                                    data[id]['mustnot'] = JSON.parse(data[id]['mustnot']);
                                    data[id]['mustCUI'] = JSON.parse(data[id]['mustCUI']);
                                    data[id]['must'] = JSON.parse(data[id]['must']);
                                    
                                    master.all_models[id] = data[id];
                                    master.all_models[id]["local_obj"] = new model_single(master, id);
                                }
                                // show the model
                                if (vis) {
                                    master.push(master.all_models[id]["local_obj"]);
                                }
                            }
                        }
                        
                    });
                    
                }
                // hide unwanted models
                for (var i in master.vis_models){
                    if (!(master.vis_models[i].model in supported_models)) {
                        master.pop(master.vis_models[i]);
                    }
                }
                // TODO make models visible as appropriate
                
            }
        });
    }
    
    
    this.scoremodels = function(CUIs) {
        console.log("models beings scored...");
        console.log(CUIs);
        var data = CUIs;
        data['models'] = [];
        for (var id in this.vis_models) {
            var model = this.vis_models[id];
            var valid = true
            // validate each model
            for (var i in model['inpCUI']) {
                var CUI = model['inpCUI'][i];
                var mustCUIcounter = 0;
                if ((this.master.CUIlist.all_CUIs[CUI]['datatype'] == 'float') || 
                    (this.master.CUIlist.all_CUIs[CUI]['datatype'] == 'int') || 
                    (this.master.CUIlist.all_CUIs[CUI]['datatype'] == 'integer') ) 
                {
                    // check for CUIs outside of boundaries
                        if ((model['upper'][i] != null) && (data[CUI] > model['upper'][i])) valid = false;
                        if ((model['upper'][i] != null) && (data[CUI] < model['lower'][i])) valid = false;
                }
                // TODO implement population checks with CUI expansion HERE or on the SERVER
                
                /*if ((this.master.CUIlist.all_CUIs[CUI]['datatype'].toLowerCase() == 'bool') || 
                    (this.master.CUIlist.all_CUIs[CUI]['datatype'].toLowerCase() == 'boolean') ) 
                {
                    if (data[CUI] === true){
                        // check for banned CUIs
                        for (var j in model['mustnot']){
                            if (CUI == model['mustnot'][j]) valid = false;
                        }
                    }
                    // increment the necessary conditions satisfied if applicable
                    for (k in model['mustCUI']) {
                        if (CUI == model['mustCUI'][k]) mustCUIcounter += 1;
                    }
                }
                if (mustCUIcounter < model['mustCUI'].length) valid = false;
                */
                // TODO anything else to check locally?
            }
            if (valid) {
                data['models'].push(model)
            }
        }
        if (data['models'].length == 0) console.log("no models are being sent!");
        else 
        {
            console.log(data['models']);
            console.log(this.all_models);
            // request for model scores
            $.ajax({
                url : "api/score/by_models",
                data : data,
                master: this,
                headers: {"Content-Type": "application/json"},
                success: function(reply) {
                    // store the pertinent pointer
                    var master = this.master; 
                    
                    // parse the reply
                    var data = JSON.parse(reply);
                    console.log(data);
                    
                    // record scores on all models
                    for (var model in data) {
                        console.log(model, data[model]);
                        // display if possible
                        if (model in master.all_models) {
                            // clean up the score
                            var score = (parseFloat(data[model]['score']) == NaN) ? data[model]['score'] : parseFloat(data[model]['score']) ; // NaN untested
                            if (typeof(score) == "number") {
                                score = (Math.round(score*1000)/10).toString() + "%";
                            }
                            $(master.all_models[model]['local_obj'].score).text(score);
                        // otherwise report
                        } else {
                            console.log(data[model], "unsupported model");
                        }
                    }
                }
            
            });
        }
    }
}
