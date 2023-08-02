const trigger = $('#toggle_header');
const header = $('Header');

trigger.click(()=> {

	header.toggleClass('green red');
})

