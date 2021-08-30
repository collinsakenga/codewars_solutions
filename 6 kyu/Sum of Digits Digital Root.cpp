int digital_root(int n)
{
  int b = n;
  int sum = 0;
  int count = 0;
  int num;
  while (b > 10) {
    b /= 10;
    count++;
  }
  int divide = 1;
  for (int i = 0; i < count; i++) {
    divide *= 10;
  }
  int save=n;
  while (divide > 0)
  {
    num = save/divide;
    sum += num;
    save = save % divide;
    divide /= 10;
  }
  int sum2 = sum;
  while (sum >= 10)
  {
    count = 0;
    divide = 1;
    save = sum;
    while (sum2 >= 10)
    {
      sum2 /= 10;
      count++;
    }
    sum2 = 0;
    for (int i = 0; i < count; i++) {
      divide *= 10;
    }
    while (divide > 0)
    {
      num = save / divide;
      sum2 += num;
      save = save % divide;
      divide /= 10;
    }
    sum = sum2;
  }
  return sum;
}