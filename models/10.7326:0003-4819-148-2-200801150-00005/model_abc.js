
function getFormData(theForm)
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
}


//
// Coefficients
// 

var constVal = 22.949536;

var scaleVal = 0.876925

var coefs =
{
    gender: -0.202933, age: -0.156412, bmi: -0.033881, sbp: -0.05933, dbp: -0.128468, smoker: -0.190731, 
    parentalht: -0.166121, ageXdbp: 0.001624
};

function calcBmi(height, mass)
{
	bmi = 703.0814062 * mass / (height * height);
    return bmi;   
}


function calcRisk(data)
{    
    // Fill in derived values
    data['ageXdbp'] = (data['age'] * data['dbp']);
    
    // do computation
    var betaSum = constVal;
    for(var k in coefs)
    {
        var dBeta = coefs[k] * data[k];
        betaSum += dBeta;
    }

    var risk4 = 1.0 - Math.exp( -Math.exp(( Math.log(4) - betaSum) / scaleVal));
    var risk2 = 1.0 - Math.exp( -Math.exp(( Math.log(2) - betaSum) / scaleVal));
    var risk1 = 1.0 - Math.exp( -Math.exp(( Math.log(1) - betaSum) / scaleVal));    

    return {'1':risk1, '2': risk2, '4': risk4};

}


function formDataValid(data)
{
    if ( (data['age'] > 80) || (data['age'] < 20))
    {
        $('#error_msg').text("Age must be between 20 and 80");
        return false;
    }
    
    if ( (data['sbp'] > 140) || (data['sbp'] < 50))
    {
        $('#error_msg').text("Systolic pressure must be between 50 and 140");
        return false;
    }    

    if ( (data['dbp'] > 90) || (data['dbp'] < 30))
    {
        $('#error_msg').text("Diastolic pressure must be between 30 and 90");
        return false;
    }    
    
    if ( (data['height'] > 90) || (data['height'] < 45))
    {
        $('#error_msg').text("Height must be between 48 and 84");
        return false;
    }
    
    if ( (data['weight'] > 400) || (data['weight'] < 70))
    {
        $('#error_msg').text("Weight must be between 70 and 400");
        return false;
    }

    
    return true;
}

function doCalculation()
{

    var data = getFormData(document.forms.calcForm);

    if ( formDataValid(data) )
    {
        $('#error_msg').text(''); // clear error text
                
    	var bmi = calcBmi(data['height'], data['weight']);        
    	
    	data['bmi'] = bmi;
    	
    	
        var risks = calcRisk(data);

        // optimal risk
        data['bmi'] = 22.5;
        data['sbp'] = 110.5;
        data['dbp'] = 70.5;
        data['smoker'] = 0;
        data['parentalht'] = 0;
    
        var optRisks = calcRisk(data);

        // text
        $('#bmi_txt').text(Math.round( 10 * bmi)/10);
        
        $('#risk1_txt').text(Math.round( 100 * risks['1']) + "%");
        $('#comp_risk1_txt').text(Math.round( 100 * optRisks['1']) + "%");  

        $('#risk2_txt').text(Math.round( 100 * risks['2']) + "%");
        $('#comp_risk2_txt').text(Math.round( 100 * optRisks['2']) + "%");  
        
        $('#risk4_txt').text(Math.round( 100 * risks['4']) + "%");
        $('#comp_risk4_txt').text(Math.round( 100 * optRisks['4']) + "%");  
        
        // And bar widths in the graph
        var fullW = $('#graph_bkg').width();

        // NOTE: Bars peg at 100%
        var maxVal = 100;
        
        $('#risk1_bar').width( Math.round( 100 * risks['1']) * fullW / maxVal);          
        $('#comp_risk1_bar').width( Math.round( 100 * optRisks['1']) * fullW/ maxVal);       

        $('#risk2_bar').width(Math.round( 100 * risks['2']) * fullW / maxVal);          
        $('#comp_risk2_bar').width(Math.round( 100 * optRisks['2']) * fullW/ maxVal);  
        
        $('#risk4_bar').width( (Math.round( 100 * risks['4']) * fullW / maxVal));          
        $('#comp_risk4_bar').width (Math.round( 100 * optRisks['4']) * fullW/ maxVal);          
        
    }
}



function showCalc()
{
    $('#cover').css('opacity', '.5'); 	
    $('#cover').show();
    $('#calc').show();   
    doCalculation();    
}

function hideCalc()
{
    $('#calc').hide();
    $('#cover').hide();
}

