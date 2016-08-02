/**
 * models_single
 * 
 * class to hold the search for new models
 **/
 
function model_single(master, model) {
    this.master = master;
    this.id = "model" + model;
    this.model = model;
    
    // model identification
    var text = '<div style= "text-align:center; height:45px; overflow:visible; width:350px;">';
    text +=    '    <a href="scorequery.php?id='+this.model+'" >' + master.all_models[this.model]['outcometime'].toString() + 'Y Risk of '+master.all_models[this.model]['outcome']+'</a>'; // TODO link destination
    text +=    '    <a href="scorequery.php?id='+master.all_models[this.model]['id']+'" ><br>from ' + master.all_models[this.model]['authors'][0] + " et al's " + master.all_models[this.model]['yearofpub'] +" Paper</a>"; // TODO link destination
    text +=    '</div>';
    this.title = $(text);
    
    this.score = $('<div style= "text-align:center; height:45px; width:50px"></div>');
    
    // previous and next in the table
    this.prev = null;
    this.next = null;
   
    this.show = function (dest, prev) {
        // adjust list pointers
        this.prev = prev;
        if (prev != null && prev.next != null) {
            this.next = prev.next;
        }
        if (prev != null) {
            prev.next = this;
        }
        
        // show content
        if (prev == null){
            // show title div
            $(dest.titles).html(this.title);
            // show score div
            $(dest.scores).html(this.score);
        }
        else {
            // show title div
            $(prev.title).after(this.title);
            // show score div
            $(prev.score).after(this.score);
        }
    }
    
    this.hide = function () {
        // adjust list pointers
        if (this.prev !== null) {
            this.prev.next = this.next;
        }
        if (this.next !== null) {
            this.next.prev = this.prev;
        }
        
        // removes its CUI from vis_CUIs
        //TODO
        
        // remove html
        $("#" + this.id).remove();
    }
}
