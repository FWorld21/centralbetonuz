document.addEventListener('DOMContentLoaded', () => {
	const newsSwiper = new Swiper('.news-swiper', {
		// Parameters
		slidesPerView: 1,
		spaceBetween: 10,
		breakpoints: {
			768: {
				slidesPerView: 1,
			},
			1024: {
				slidesPerView: 2,
				centeredSlides: true,
				spaceBetween: 130,
			},
			1280: {
				slidesPerView: 2,
				centeredSlides: false,
			},
		},

		// Pagination
		pagination: {
			el: '.swiper-pagination',
		},

		// Arrows
		navigation: {
			nextEl: '.news-button-next',
			prevEl: '.news-button-prev',
		},
	});

	const partnersSwiper = new Swiper('.partners', {
		// Parameters
		slidesPerView: 1,
		allowTouchMove: false,
		loop: true,
		spaceBetween: 20,
		autoplay: {
			delay: 3000,
		},
		breakpoints: {
			640: {
				slidesPerView: 3,
			},
			768: {
				slidesPerView: 4,
			},
			1024: {
				slidesPerView: 5,
			},
		},
	});

	const introSwiper = new Swiper('.intro', {
		// Parameters
		slidesPerView: 1,
		// allowTouchMove: false,
		loop: true,
		// autoplay: {
		// 	delay: 3000,
		// },
		// Pagination
		// pagination: {
		// 	el: '.swiper-pagination',
		// },
	});
});
