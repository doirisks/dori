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
    var titlespace = document.createElement('span');
    titlespace.setAttribute("style", "display:block; text-align:center; height:45px; overflow:visible; width:300px;");
    // link to outcome
    var outcomelink = document.createElement('a');
    outcomelink.appendChild(document.createTextNode(master.all_models[this.model]['outcometime'].toString() + 'Y Risk of '+master.all_models[this.model]['outcome']));
    outcomelink.setAttribute("href", "https://www.google.com/?#q="+ master.all_models[this.model]['outcometime'].toString() + ' year risk of '+master.all_models[this.model]['outcome']);
    // link to paper
    var paperlink = document.createElement('a');
    paperlink.appendChild(document.createTextNode(master.all_models[this.model]['authors'][0] + " et al's " + master.all_models[this.model]['yearofpub'] +" Paper"));
    paperlink.setAttribute("href", "https://www.google.com/?#q="+ master.all_models[this.model]['DOI']);
    
    titlespace.appendChild(outcomelink);
    titlespace.appendChild(document.createElement("br"));
    titlespace.appendChild(document.createTextNode('from '));
    titlespace.appendChild(paperlink);
    this.title = $(titlespace);
    
    
    // score display
    this.score = $('<span style= "display:block;text-align:center;height:45px;width:75px;"></span>');
    
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
    
    this.hide = function() {
        // adjust list pointers
        if (this.prev !== null) {
            this.prev.next = this.next;
        }
        if (this.next !== null) {
            this.next.prev = this.prev;
        }
        
        // remove html
        this.title.remove();
        this.score.remove();
    }
}
