/**
 * models_table
 * 
 * class to write and maintain the models table (active models)
 **/

function models_table(master) {
    this.base = text;
    this.master = master;
    var text = '<span id="modeltitle" style="width:400px"><span>';
    text    += '  <span style="width:300px;float:left">Models</span>';
    text    += '  <span style="width:75px">Scores</span>';
    text    += '</span>';
    text    += '<div id="allmodels" ></div>';
    this.base = text;
    
    this.titles = $("<div style='float:left; width:300px; display:block; overflow:hidden'></div>"); 
    this.scores = $("<div style='width:75px; display:block; overflow:hidden'></div>"); 
    
    // the most recent addition
    this.head = null;
    
    // makes a CUI visible in the table
    this.push = function (model_obj) {
        model_obj.show(this.head);
        this.head = model_obj;
    }
    
    // remove a CUI from the table
    this.pop = function (model_obj) {
        model_obj.remove();
        //TODO
    }
}
