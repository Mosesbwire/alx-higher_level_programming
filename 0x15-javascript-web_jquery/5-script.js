const trigger = $('#add_item');
const ul = $('ul.my_list');

trigger.click(()=>{
	ul.append('<li>Item</li>');
});
