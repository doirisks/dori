/**
 * riskfactors_finder
 * 
 * class to hold the search for new models
 **/
function riskfactor_finder(master) {
    // identify the master
    this.master = master;
    
    // minimum length for autocomplete
    this.minAutoCompleteLength = 4;
    
    // identify self for use in lambda functions
    var _this = this;
    
    // options currently displayed
    
    // function to search for and possibly add a model
    this.get = function(CUI) {
        var CUIs = {};
        CUIs[CUI] = CUI;
        this.master.fetchCUIs(CUIs);
    }
    
    this.autocomplete = function() {
		var value = $(this.input).val();
		var typedwords = value.split();
		var keywords = [];
		// iterate through words entered
		for (var i in typedwords) {
		    var keyword = typedwords[i];
		    if (keyword.length >= this.minAutoCompleteLength) {  
		        keywords.push(keyword);
		    }
	    }
	    // send query with keywords, if any
	    if (keywords.length > 0) {
	        $.ajax({
                url : "autocomplete/cui.php", 
                data : {'words':keywords},
                master : this, 
                headers: {"Content-Type": "application/json"},
                success: function(reply) {
                    // store reference to the original sender
                    var master = this.master;
                    
                    // unpack reply
                    var data = JSON.parse(reply);
                    
                    // update the options div
                    master.update_options_div(data);
                }
	        });
	    }
	    // otherwise, report
	    else {
	        // TODO
    	    console.log("input too short for autocomplete");
	    }
    }
    
    this.update_options_div = function (data) {
        // iterate through responses, if any
        if (data.length > 0) {
            // TODO make it so that the whole list is not built every time
            var $options = $(this.optionsdiv);
            $options.html("");
            for (var i in data) {
                var CUI = data[i];
                var option = document.createElement("p");
                var button = document.createElement("button");
                button['CUI'] = CUI['CUI'];
                var _this = this;
                $(button).click(function(e) {
                    e.preventDefault();
                    var CUI = this['CUI'];
                    _this.get(CUI);
                });
                button.setAttribute("style","display:inline;");
                button.appendChild(document.createTextNode("+"));
                option.appendChild(button);
                option.appendChild(document.createTextNode(" " + toTitleCase(CUI['name1'])));
                
                // add the option to DOM
                $options.append(option);
                
                //console.log(CUI['CUI'], CUI['name1']);
            }
        }
        // otherwise, report
        else {
            $(master.optionsdiv).text("no risk factors indicated");
            // TODO add timeout so that this message disappears after a few seconds
            console.log("no risk factors indicated");
        }
    }
    
    // the base of the document
    this.base = document.createElement('div');
    this.base.setAttribute("style","text-align:center;");
    var title = document.createElement('p');
    var titletext = document.createElement('b');
    titletext.appendChild(document.createTextNode("Search for Risk Factors"));
    title.appendChild(titletext);
    this.base.appendChild(title);
    
    // button
    //this.button = document.createElement('button');
    //this.button.setAttribute("style","display:block; float:left;");
    //this.button.appendChild(document.createTextNode("Find"));
    //$(this.button).click(function(e) {
    //    e.preventDefault();
    //    _this.find();
    //});
    
    // input
    this.input = document.createElement("input");
    //this.button.setAttribute("style","display:block;");
    this.input.setAttribute("type","text");
    //$(this.button).submit(function(e) {
    //    e.preventDefault();
    //    _this.get();
    //});
    $(this.input).keyup(function () {    // autofill
        _this.autocomplete();
    });
    
    // the whole search form
    var searchform = document.createElement('div');
    //searchform.appendChild(this.button);
    searchform.appendChild(this.input);
    this.base.appendChild(searchform);
    
    // display results div
    this.optionsdiv = document.createElement('div');
    this.optionsdiv.setAttribute("style","text-align:center");
    this.base.appendChild(this.optionsdiv);
    
}
