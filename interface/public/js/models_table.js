/**
 * models_table
 * 
 * class to write and maintain the models table (active models)
 **/

function models_table(master) {
    this.master = master;
    var text = "        <div id = 'models'>\n";
    text    += '            <!-- available models are added here -->\n';
    text    += '        </div>\n';
    this.base = text;
}
