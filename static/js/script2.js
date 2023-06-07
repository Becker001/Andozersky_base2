const numberField = document.getElementById('numberField');
const increaseButton = document.getElementById('increaseButton');
const decreaseButton = document.getElementById('decreaseButton');

let number = 0; // начальное значение числа

// увеличиваем число на 1 при нажатии на кнопку "+"
increaseButton.addEventListener('click', () => {
  number++;
  numberField.value = number;
});

// уменьшаем число на 1 при нажатии на кнопку "-"
decreaseButton.addEventListener('click', () => {
  if (number > 0) { // чтобы число не стало отрицательным
    number--;
    numberField.value = number;
  }
});