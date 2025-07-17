function clear1(){
    document.getElementById("output-value").textContent = "";
    document.getElementById("history-value").textContent = "";
}
function backspace() {
    const output = document.getElementById("output-value");
    output.textContent = output.slice(0, -1);
}
function setscreenvalue(value) {
    const output = document.getElementById("output-value");
    const currentValue = output.textContent;
    
    if (
        (
               ["+", "-", "*", "/"].includes(value) && currentValue === "" 
             
        ) ||
        (
            [
                "+", "-", "*", "/"
            ].includes(value)&& [
                "+", "-", "*", "/"
            ].includes(currentValue.slice(-1))
            
        )
        )
    {       return;
    }
    output.textContent += value;
    
   

}
function calculateresult() {
    const output = document.getElementById("output-value");
    const history = document.getElementById("history-value");
    const expression = output.textContent.trim();
    if (expression === "") {
        output.textContent = "Please enter a vaild expression";
        
        return;
    }

    else {
        const result= eval(expression);
        history.textContent = expression;
        output.textContent = result;
    }
}


