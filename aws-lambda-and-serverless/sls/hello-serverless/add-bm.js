'use strict';

module.exports.add = async event => {
    let {num1, num2} = event;
    return num1 + num2;  
};