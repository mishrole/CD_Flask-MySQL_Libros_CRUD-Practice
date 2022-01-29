'use strict';

const Validate = (inputs) => {
    inputs.forEach(element => {
        if (element.value.length === 0) {
            element.nextElementSibling.classList.add('show');
        } else {
            element.nextElementSibling.classList.remove('invalid-feedback');
            element.nextElementSibling.innerHTML = 'Looks good!';
            element.nextElementSibling.classList.add('valid-feedback');
            element.nextElementSibling.classList.add('show');
        }
    });
}