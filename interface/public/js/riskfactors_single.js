/**
 * riskfactors_single
 * 
 * class to hold the search for new models
 **/
 
function riskfactor_single(master,CUI) {
    this.master = master;
    this.CUI = CUI;
    var _this = this;
    
    this.height = 40;
    
    this.button = $('<button >-</button>');
    this.remover = $('<div style="text-align:center;height:' + this.height.toString() + 'px;">');
    this.remover.append(this.button);
    
    // rf - name of risk factor CUI displayed w/link
    var text = '<div style= "text-align:center; height:' + this.height.toString() + 'px; overflow:visible;">';
    var riskname = toTitleCase(master.all_CUIs[CUI]['name1']);
    text +=    '    <a href="CUIquery.php?CUI=' + CUI + '" >'+riskname+'</a>'; // TODO link destination
    text +=    '</div>';
    this.rf = $(text);
    
    // input - display the correct type of input for the CUI
    var input = document.createElement("div");
    input.setAttribute("style","text-align:center; height:" + this.height.toString() + "px; overflow:visible;");
    // Sex CUI
    if (CUI == 'C28421') { 
        this.input1 = document.createElement("input");
        this.input1.setAttribute("type","radio");
        this.input1.setAttribute("value","male");
        this.input1.setAttribute("checked","checked");
        this.input1.setAttribute("name",CUI);
        this.input2 = document.createElement("input");
        this.input2.setAttribute("type","radio");
        this.input2.setAttribute("value","female");
        this.input2.setAttribute("checked","checked");
        this.input2.setAttribute("name",CUI);
        
        input.appendChild(this.input1);
        input.appendChild(document.createTextNode(" Male "));
        input.appendChild(this.input2);
        input.appendChild(document.createTextNode(" Female"));
    // floats
    } else if (master.all_CUIs[CUI]['datatype'].toLowerCase() == 'float') {
        this.input1 = document.createElement("input");
        this.input1.setAttribute("type","number");
        this.input1.setAttribute("style","width:50px;text-align:center;");
        
        input.appendChild(this.input1);
    // integers
    } else if (master.all_CUIs[CUI]['datatype'].toLowerCase() == 'int' || master.all_CUIs[CUI]['datatype'].toLowerCase() == 'integer') {
        this.input1 = document.createElement("input");
        this.input1.setAttribute("type","number");
        this.input1.setAttribute("style","width:50px;text-align:center;");
        
        
        input.appendChild(this.input1);
    } else /*if (master.all_CUIs[CUI]['datatype'].toLowerCase() == 'bool')*/ {
        this.input1 = document.createElement("input");
        this.input1.setAttribute("type","checkbox");
                
        input.appendChild(this.input1);
    }
    this.input = $(input);
    
    // units - correctly display the units of the CUI
    var units = document.createElement("div");
    units.setAttribute("style",'text-align:center; height:' + this.height.toString() + 'px;');
    var p = document.createElement("p");
    if ( (master.all_CUIs[CUI]['units'] != null) && (master.all_CUIs[CUI]['datatype'].toLowerCase() == "float") ) {
        p.appendChild(document.createTextNode(master.all_CUIs[CUI]['units']));
    }
    units.appendChild(p);
    this.units = $(units);
    
    // set the initial value of the risk factor if applicable
    var elem = this.input1//[0].getElementsByTagName("input")[0];
    if (elem == null) {
        console.log("no element");
    } else if (elem.type == "checkbox") {
        //this.value = elem.checked;
    } else if (elem.type == "number") {
        // handle blank numbers 
        if (elem.value == "") {
            // sets val to harmonic mean of default lower + 1 and default upper + 1
            var val = 0;
            if (master.all_CUIs[this.CUI]['CUI'] == "C0804405") {       // age
                val = 55;
            } else if (master.all_CUIs[this.CUI]['CUI'] == "C0488055") {          // sysBP
                val = 120;
            } else if (master.all_CUIs[this.CUI]['CUI'] == "C0488052") {          // diaBP
                val = 80;
            } else if (master.all_CUIs[this.CUI]['CUI'] == "C0364708") {          // totchol
                val = 180;
            } else if (master.all_CUIs[this.CUI]['CUI'] == "C0364221") {          // hdlchol
                val = 60;
            } else if (master.all_CUIs[this.CUI]['CUI'] == "C1542867") {          // bmi
                val = 23;
            } else {
                // sets val to geometric mean of default lower + 1 and upper + 1
                val = (((master.all_CUIs[this.CUI]['defaultlower'] + 1) * (master.all_CUIs[this.CUI]['defaultupper'] + 1)) ** 0.5);
            }
            elem.value = (Math.round(val * 10) / 10).toString();
            //this.value = Number(val);
        }
        this.value = Number(elem.value);
    } else if (elem.type == "radio") {
        //this.value = elem.checked; // note that this will return true if MALE is checked for sex
    } else {
        console.log("unknown type error", elem.type);
        //this.value = null;
    }
    
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
            // show remover
            $(dest.buttons).html(this.remover);
            // show rf
            $(dest.names).html(this.rf);
            // show input
            $(dest.values).html(this.input);
            // show units
            $(dest.unit_names).html(this.units);
        }
        else {
            // show remover
            $(prev.remover).after(this.remover);
            // show rf
            $(prev.rf).after(this.rf);
            // show input
            $(prev.input).after(this.input);
            // show units
            $(prev.units).after(this.units);
        }
        
        // add event listener to the button
        var _this = this;
        this.button.click(function() {
            _this.removefunc();
        });
        // add event listener to the input
        $(this.input1).click(function() {
            _this.changefunc();
        });
        if (typeof (this.input2) != undefined) {
            $(this.input2).click(function() {
                _this.changefunc();
            });
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
        this.remover.remove();
        this.rf.remove();
        this.input.remove();
        this.units.remove();
    }
    
    // function called on change of value
    this.changefunc = function() {
        this.master.master.fetchmodels();
        this.master.master.clearscores();
    }
    // function called on removal
    this.removefunc = function() {
        this.master.pop(this);
        this.master.master.fetchmodels();
        this.master.master.clearscores();
    }
    
    
    // provide the value of the CUI (defined differently for different kinds of risk factors)
    if (elem == null) {
        console.log("no input element in risk factor", this.CUI);
    } else if (elem.type == "checkbox") {
        this.getVal = function (numbfill = false) {
            var elem = this.input1;
            return elem.checked;
        }
    } else if (elem.type == "number") {
        this.getVal = function (numbfill = false) {
            var elem = this.input1;
            return Number(elem.value);
        }
    } else if (elem.type == "radio") {
        this.getVal = function (numbfill = false) {
            var elem = this.input1;//[0].getElementsByTagName("input")[0];
            return elem.checked;   // note that this will return true if MALE is checked for sex
        }
    } else {
        console.log("unknown type error in risk factor", this.CUI, elem.type);
    }
}
