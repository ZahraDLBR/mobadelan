jQuery(document).ready(function($) {

	$(".headroom").headroom({
		"tolerance": 20,
		"offset": 50,
		"classes": {
			"initial": "animated",
			"pinned": "slideDown",
			"unpinned": "slideUp"
		}
	});

});
function Confirm(form){
alert("ایجاد حساب کاربری با موفقیت انجام شد!"); 
form.submit();
}