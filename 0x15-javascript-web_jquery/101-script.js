$(document).ready(()=>{

	const list = $('ul.my_list');
	$('#add_item').click(()=>{
		list.append('<li>Item</li>');
	});
	$('#remove_item').click(()=>{
		$('ul.my_list:last').remove();
	});

	$('#clear_list').click(()=>{
		list.empty();
	});

});
