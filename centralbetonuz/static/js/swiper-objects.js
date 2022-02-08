document.addEventListener('DOMContentLoaded', () => {
	const objectsSwiper = new Swiper('.objects', {
		// Parameters
		slidesPerView: 1,
		loop: true,
		// If we need pagination
		pagination: {
			el: '.swiper-pagination',
			clickable: true,
		},
	});
});
