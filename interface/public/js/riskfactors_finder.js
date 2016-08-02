/**
 * riskfactors_finder
 * 
 * class to hold the search for new models
 **/
function riskfactor_finder(master) {
    // identify the master
    this.id = "newrf";
    this.master = master;
    
    // identify self for use in lambda functions
    var _this = this;
    
    // function to search for and possibly add a model
    this.find = function() {
        // TODO
    }
    
    // the base of the document
    this.base = document.createElement('div');
    var title = document.createElement('p');
    var titletext = document.createElement('b');
    titletext.appendChild(document.createTextNode("Search for Risk Factors"));
    title.appendChild(titletext);
    this.base.appendChild(title);
    
    // button
    this.button = document.createElement('button');
    this.button.setAttribute("style","float:left;");
    this.button.appendChild(document.createTextNode("Find"));
    $(this.button).click(function(e) {
        e.preventDefault();
        _this.find();
    });
    
    // input
    this.input = document.createElement("input");
    this.input.setAttribute("type","text");
    $(this.button).submit(function(e) {
        e.preventDefault();
        _this.find();
    });
    $(this.input).change(function () {    // autofill
    
        //TODO
    });
    
    // the whole search form
    var searchform = document.createElement('div');
    searchform.appendChild(this.button);
    searchform.appendChild(this.input);
    this.base.appendChild(searchform);
}
