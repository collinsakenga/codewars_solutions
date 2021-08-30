bool eleven(const std::string input) 
{
    int even=0, odd=0;
    for (size_t i=0; i<input.size(); i++)
    {
      int num=input[i]-'0';
      if (i%2==0)
      {
        even+=num;
      }
      else 
      {
        odd+=num;
      }
    }
    return (even-odd)%11==0;
}