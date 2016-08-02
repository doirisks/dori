/**
 * models_table
 * 
 * class to write and maintain the models table (active models)
 **/

function model_list(master) {
    // identify the master
    this.master = master;
    
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
}
