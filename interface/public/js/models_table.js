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
    var titletitle = document.createElement("p");
    titletitle.setAttribute("style","width:325px;text-align:center;float:left;");
    scoretitle.appendChild(docuemnt.createTextNode("Models");
    var scoretitle = document.createElement("p");
    scoretitle.setAttribute("style","width:325px;text-align:center;");
    scoretitle.appendChild(docuemnt.createTextNode("Scores");
    var titlebar = document.createElement("span");
    titlebar.setAttribute("style","width:400px");
    titlebar.appendChild(titletitle);
    titlebar.appendChild(scoretitle);
    
    this.base.append(titlebar);
    
    // titles and scores lists
    this.titles = $("<div style='float:left; width:300px; display:block; overflow:hidden'></div>"); 
    this.scores = $("<div style='width:75px; display:block; overflow:hidden'></div>"); 
    
    this.base.append(this.titles);
    this.base.append(this.scores);
    
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
