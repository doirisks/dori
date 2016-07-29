/**
 * riskfactors_single
 * 
 * class to hold the search for new models
 **/
 
function riskfactors_single(master,CUI) {
    this.master = master;
    this.CUI = CUI;
    this.id = CUI;
    //TODO this.datatype = master.;
    
    //TODO this.val = ;
    
    var text = '<div id="' + this.id + '">\n';
    // button - removal button
    var text = '<div style="text-align:center; height:30px;">';
    text +=    '    <button id = "remove' + CUI + '" onclick=the_interface.righttable.pop(master.all_CUIs["'+CUI+'"]["local_obj"]) >-</button>'; //TODO
    text +=    '</div>';
    this.button = $(text);
    
    // rf - name of risk factor CUI displayed w/link
    var text = '<div style= "text-align:center; height:30px; overflow:visible;">';
    var riskname = toTitleCase(master.all_CUIs[CUI]['name1']);
    text +=    '    <a href="CUIquery.php?CUI=' + CUI + '" >'+riskname+'</a>'; // TODO link destination
    text +=    '</div>';
    this.rf = $(text);
    
    // interpret the datatype and units
    var inputdata = "";
    var units = "";
    if (CUI == 'C28421') { // Sex
        inputdata = 'type="radio" value="male" checked> Male</input>  <input type="radio" name="'+CUI+'" value="female"> Female<p></p';
    } else if (master.all_CUIs[CUI]['datatype'].toLowerCase() == 'float') {
        inputdata = 'type="number" placeholder="Float" style="width:50px"';
        units += master.all_CUIs[CUI]['units'];
    } else if (master.all_CUIs[CUI]['datatype'].toLowerCase() == 'int' || master.all_CUIs[CUI]['datatype'].toLowerCase() == 'integer') {
        inputdata = 'type="number" placeholder="Integer" style="width:50px';
        units += master.all_CUIs[CUI]['units'];
    } else /*if (master.all_CUIs[CUI]['datatype'].toUpperCase() == 'BOOL')*/ {
        inputdata = 'type = "checkbox" ';
    } 
    
    // input
    var text = '<div style= "text-align:center; height:30px;">';
    text +=    '    <input name = "' + CUI + '" ' + inputdata + ' ></input> ';
    text +=    '</div>';
    this.input = $(text);
    
    // units
    var text = '<div style= "text-align:center; height:30px;">' + units + '</div>';
    this.units = $(text);
    
    // previous and next in the table
    this.prev = null;
    this.next = null;
   
    this.show = function (prev) {
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
            // show button
            $(master.righttable.buttons).html(this.button);
            // show rf
            $(master.righttable.names).html(this.rf);
            // show input
            $(master.righttable.values).html(this.input);
            // show units
            $(master.righttable.unit_names).html(this.units);
        }
        else {
            // show button
            $(prev.button).after(this.button);
            // show rf
            $(prev.rf).after(this.rf);
            // show input
            $(prev.input).after(this.input);
            // show units
            $(prev.units).after(this.units);
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
        else {
            // change head of table if appropriate
            master.righttable.head = this.prev;
        }
        
        // remove html
        $("#" + this.id).remove();
    }
    
    this.getVal = function () {
        //TODO
    }
}
