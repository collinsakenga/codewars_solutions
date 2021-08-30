bool is_square(int n)
{
  int count = 0;
  int sum;
  if (n<0)
  {
    return false;
  }
  else
  {
    while (true)
    {
      sum = count * count;
      if (sum==n)
      {
        return true;
      }
      if (sum>n)
      {
        return false;
      }
      count++;
    }
  }
}