const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');


const slugify = (val)=>{
	return val.toString().toLowerCase().trim()
	.replace(/&/g,'-and-')//replace  & with '-and-'
	.replace(/[\s\W-]+/g,'-'); //replace spaces and non word chars with dashes with a single dash
};
// we are adding a listener to titleINput so when user write in this field we will generate the slug


titleInput.addEventListener('keyup',(e)=>{
	slugInput.setAttribute('value',slugify(titleInput.value));

});
