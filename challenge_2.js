const showFibonacciSequence = () => {
  const sequence = [1, 1];

  for (let index = 2; index < 30; index += 1) {
    sequence[index] = sequence[index - 2] + sequence[index - 1];
  }

  return sequence;
};

console.log(showFibonacciSequence());