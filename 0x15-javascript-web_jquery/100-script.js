if (document.readyState !== 'loading') init()
else document.addEventListener('DOMContentLoaded', init);

function init() {

	document.querySelector('header').style.color = '#FF0000';   
}
