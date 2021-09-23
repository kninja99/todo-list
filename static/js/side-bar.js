const navSlide = () => {
  const burger = document.querySelector('.burger');
  const side_bar = document.querySelector('.side-bar');

  burger.addEventListener('click', () => {
    if (
      side_bar.classList[1] === 'side-bar-active' ||
      side_bar.classList[1] === 'side-bar-deactive'
    ) {
      side_bar.classList.toggle('side-bar-active');
      side_bar.classList.toggle('side-bar-deactive');
    } else {
      side_bar.classList.toggle('side-bar-active');
    }
    //burger.classList.toggle('burger-active ');
  });
};

navSlide();
