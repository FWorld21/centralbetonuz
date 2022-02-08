document.addEventListener('DOMContentLoaded', () => {
	const burgerBtn = document.querySelector('.burger-btn');
	const body = document.querySelector('body');
	const burgerMenu = document.querySelector('.burger-menu');
	const burgerClose = document.querySelector('.burger-close');

	burgerBtn.addEventListener('click', () => {
		body.classList.add('overflow-hidden');
		burgerMenu.classList.remove('hidden');
	});

	burgerClose.addEventListener('click', () => {
		body.classList.remove('overflow-hidden');
		burgerMenu.classList.add('hidden');
	});
});
