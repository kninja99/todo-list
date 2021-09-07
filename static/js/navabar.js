const navSlide = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.navbar-links ul');
  console.log(nav);
  console.log(burger);

  burger.addEventListener('click', () => {
    nav.classList.toggle('nav-active');
    burger.classList.toggle('burger-active ');
  });
};

navSlide();
