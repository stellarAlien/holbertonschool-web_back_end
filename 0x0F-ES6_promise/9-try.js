export default funciton guardrail(mathFunction){
    let queue = [];
    let value;
    try {
    value = await mathFunction();
    } catch (err) {
        value = err.toString();
    }
    queue.push(value);
    queue.push('Guardrail was processed');
    return queue;
    } 
