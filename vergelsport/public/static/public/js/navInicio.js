// *******************
// NAV SCROLL FUNCTION
// *******************

$(window).scroll(function(){
	if(screen.width > 900){
		if ($(this).scrollTop() >= 50){
            $('.navSuperior').addClass("active");
            $('.logoNavSuperior').addClass("active");
            $('.navLateral').addClass("active");
             $('.menuNav').addClass("active");
		}
		else {
            $('.navSuperior').removeClass("active");
            $('.logoNavSuperior').removeClass("active");
            $('.navLateral').removeClass("active");
            $('.menuNav').removeClass("active");
		}
	}
});



/*
if ($(this).scrollTop() > 72 &&  $(this).scrollTop() < 110){
	$('.bottomNav, .mainNav').addClass("active1");
	$('.bottomNav, .mainNav').removeClass("active2");
	$('.centerNav, .minicon, .goToTop').removeClass("active");
}
else if ($(this).scrollTop() >= 110){
	$('.bottomNav, .mainNav').addClass("active2");
	$('.bottomNav, .mainNav').removeClass("active1");
	$('.centerNav, .mainNav, .minicon').addClass("active");
}
else {
	$('.bottomNav, .mainNav').removeClass("active1");
	$('.bottomNav, .mainNav').removeClass("active2");
	$('.centerNav, .mainNav, .minicon').removeClass("active");
}
*/