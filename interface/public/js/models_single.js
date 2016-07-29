/**
 * models_single
 * 
 * class to hold the search for new models
 **/
 
function models_single(master, model) {
    var text = ""; //TODO
    this.text = text;
   
    // previous and next in the table
    this.prev = null;
    this.next = null;
    
    this.show = function (prev) {
        // adjust place in list
        this.prev = prev;
        if (prev != null && prev.next != null) {
            this.next = prev.next;
        }
        prev.next = this;
        
        // show in html
        $("#" + prev.id).after(this.content);
    }
}
