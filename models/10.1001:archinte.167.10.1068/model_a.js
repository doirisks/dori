// code converted into model_by.py
// credit to original writer, but he/she is not identified
function DiabetesCalc()
{

	var getFormData = function(theForm)
	{
	    formData = new Object();
	    
	    theElems = theForm.elements;   
	     
	    for(var i=0;i<theElems.length;i++)
	    {
	        e = theElems[i];
	
	        switch(e.type)
	        {
	        case 'text':
	        case 'textarea':
	            formData[e.name] = e.value;
	            break;
	        case 'radio': // assumes at least one of the buttons is selected
	            if ( e.checked )
	                formData[e.name] = e.value;
	            break;
	            
	        case 'select':
	            formData[e.name] = e.options[e.selectedIndex];
	            break;
	
	        default:
	            break;
	        }
	    }
	    return formData;
	};
	
	
	var calcBmi = function(height, mass)
	{
		bmi = 703.0 * mass / (height * height);
		 
	    return bmi;   
	};
	
	
	var formDataValid = function(data)
	{
	    if ( (data['age'] > 64) || (data['age'] < 45))
	    {
	        $('#error_msg').text("Age must be between 45 and 64");
	        return false;
	    }	  
		
	    if ( (data['height'] > 84) || (data['height'] < 48))
	    {
	        $('#error_msg').text("Height must be between 48 and 84");
	        return false;
	    }
	    
	    if ( (data['weight'] > 300) || (data['weight'] < 80))
	    {
	        $('#error_msg').text("Weight must be between 80 and 300");
	        return false;
	    }

	    if ( (data['glucose'] > 125) || (data['glucose'] < 0))
	    {
	        $('#error_msg').text("Glucose level must be less than 126");
	        return false;
	    }	    
	
	    return true;
	};
	
	var minPts = 10;
	var maxPts = 25;

	var riskTab =
	{
	    10: 3, 
	    11: 4,
	    12: 4,
	    13: 5,
	    14: 6,
	    15: 7,
	    16: 9,
	    17: 11,
	    18: 13,
	    19: 15,
	    20: 18,
	    21: 21,
	    22: 25,
	    23: 29,
	    24: 33,
	    25: 35	    	
	};	
	
	this.doCalculation = function()
	{
	
	    var data = getFormData(document.forms.calcForm);
	
	    if ( formDataValid(data) )
	    {
	        $('#error_msg').text(''); // clear error text
	                
	         var bmi = calcBmi( data['height'], data['weight']);
	         $('#bmi_txt').text( Math.round( 10 * bmi)/10);	         
	        
	        // points system
	        
	        var points = 0;
	        
	        if ( data['glucose'] > 99 )
	        	points += 10;
	        
	        if ( bmi >= 25.0)
	        	points += 2;
	        
	        if ( bmi > 30.0)
	        	points += 3;
	        
	        if ( data['gender'] == 0)
	        {
		        if (data['hdl'] < 40.0) // men
		        	points += 5;	        	
	        }
	        else
	        {
		        if (data['hdl'] < 50.0) // women
		        	points += 5;	        	
	        }
	        
	        if ( data['parent'] == 1)
	        	points += 3;
	        
	        if (data['tri'] > 150)
	        	points += 3;
	        
	        if ( (data['sbp'] > 130) || (data['dbp'] > 85) || (data['trtbp'] == 1))
	        	points += 2;
	        
	        // Risk from table
	        var riskLessThan = false;
	        var riskGreaterThan = false;
	        
	        if (points < minPts)
	        {
	        	points = minPts;
	        	riskLessThan = true;
	        }
	 
	        if (points > maxPts)
	        {
	        	points = maxPts;
	        	riskGreaterThan = true;
	        }	        
	        
	        var riskPct = riskTab[points];
	        

	    	var riskText = '';
	    	if (riskLessThan)
	    		riskText += '<';
	    	if (riskGreaterThan)
	    		riskText += '>';	    	
	   	
	    	riskText += riskPct;
	    	riskText += "%";
	
	   
	        // text
	        $('#risk1_txt').text(riskText);

	        // And bar widths in the graph
	        var fullW = $('#graph_bkg').width();
	
	        var maxRisk = riskTab[maxPts];
	        
	        $('#risk1_bar').width(riskPct * fullW / maxRisk);          
			
		}
     
	};

};

theCalc = new DiabetesCalc();

function showCalc()
{
    $('#cover').css('opacity', '.5'); 	
    $('#cover').show();
    $('#calc').show();   
    theCalc.doCalculation();
}

function hideCalc()
{
    $('#calc').hide();
    $('#cover').hide();
}



