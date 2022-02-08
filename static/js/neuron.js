const neuron = document.querySelector('.neuron');

neuron.addEventListener('mousemove', startRotate);
neuron.addEventListener('mouseout', stopRotate);

function startRotate(event) {
  const neuronItem = this.querySelector('.neuron-item');
  const halfHeight = neuronItem.offsetHeight / 2;
  const halfWidth = neuronItem.offsetWidth / 2;

  neuronItem.style.transform =
    'rotateX(' +
    -(event.offsetY - halfHeight) / 100 +
    'deg) rotateY(' +
    (event.offsetX - halfWidth) / 100 +
    'deg)';
}

function stopRotate(event) {
  const neuronItem = this.querySelector('.neuron-item');
  neuronItem.style.transform = 'rotate(0)';
}
