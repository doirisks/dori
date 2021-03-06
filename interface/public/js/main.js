/**
 * main.js
 *
 * js classes and procedures for the main demo interface
 */

// object defaultcalculatorstyles: 
defaultcalculatorstyles = {
    // div styles
    'div': {
        "padding" : "0px 0px 0px 0px",
    },
};

// function makeElem(tagname, style): returns an element with the desired styles as inline styles - overruling css
function makeElem(tagname, styles) {
    var elem = document.createElement(tagname);
    
    // TODO
    
}


// function toTitleCase(str) (courtesy of Greg Dean on stackoverflow): renders text in a title style
function toTitleCase(str)
{ //
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}

/**
 * whole_interface
 * 
 * class to write and maintain the main div of the doirisks interface
 **/

function whole_interface(own_div_id, init_riskfactors = []) {
    // the id of the div where the interface will be placed
    this.own_div_id = own_div_id;
    
    // the left side of the interface - models
    this.modellist  =  new model_list(this);
    this.modelfinder = new model_finder(this);
    // the right side of the interface - risk factors
    this.CUIlist  =  new riskfactor_list(this);
    this.CUIfinder = new riskfactor_finder(this);
    
    // the base text of the interface
    this.base = document.createElement("div");
    var left  = document.createElement("div");
    var centerline = document.createElement("div");
    var right = document.createElement("div");
    this.base.setAttribute("style","width:803px;overflow:hidden;border-style:solid;border-width:1px;");
    left.setAttribute("style", "width:400px;overflow:hidden;float:left;");
    centerline.setAttribute("style", "width:0px;height:1000px;border-left-width:1px;border-left-style:solid;float:left;");
    right.setAttribute("style","width:400px;overflow:hidden;");
    
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
    this.fetchCUIs = function (CUIs, vis = true) {
        this.CUIlist.fetchCUIs(CUIs, vis);
    }
    
    // fetch models from data
    this.fetchmodels = function () {
        var CUIs = this.getInputData();
        this.modellist.fetchmodels(CUIs);
    }
    
    // returns data from risk factor inputs
    this.getInputData = function() {
        return(this.CUIlist.getInputData());
    }
    
    // score visible models 
    this.scoremodels = function() {
        var CUIs = this.getInputData();
        this.modellist.scoremodels(CUIs);
    }
    
    // clear the visible scores
    this.clearscores = function() {
        this.modellist.clearscores();
    }
    
    this.base.appendChild(left);
    this.base.appendChild(centerline);
    this.base.appendChild(right);
    $('#'+own_div_id).append(this.base);
    
    // iterate through given risk factors and add them
    this.fetchCUIs(init_riskfactors);
}



// document.ready
$(document).ready( function () {
    the_interface = new whole_interface("main", riskfactors);
});
