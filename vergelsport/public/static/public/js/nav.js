// *******************
// NAV SCROLL FUNCTION
// *******************




if(screen.width > 900){
    $('.navSuperior').addClass("active");
    $('.logoNavSuperior').addClass("active");
    $('.navLateral').addClass("active");
    $('.menuNav').addClass("active");
}

$('#activeMenu').click(function () {
	if($('.navLateral').hasClass('active')){
		$('.navLateral, .menuPalo1, .menuPalo2, .menuPalo3').removeClass('active');
		$('html').css('overflow-y', 'scroll');
	}
	else{
		$('.navLateral, .menuPalo1, .menuPalo2, .menuPalo3').addClass('active');
		$('html').css('overflow-y', 'hidden');
	}
});