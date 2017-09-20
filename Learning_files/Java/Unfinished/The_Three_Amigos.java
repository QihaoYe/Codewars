public class Dinglemouse
{
  public static int[] threeAmigos(final int[] numbers)
  {
    int n = numbers.length;
    int result[] = new int[]{0, 0, 0};
    for (int i=1;i<n-1;i++)
    {
      if(numbers[i-1]%2 == numbers[i]%2 && numbers[i]%2 == numbers[i+1]%2)
      {
        int minimum = Math.min(Math.min(numbers[i-1], numbers[i]), numbers[i+1]);
        int maximum = Math.max(Math.max(numbers[i-1], numbers[i]), numbers[i+1]);
        int mi = Math.min(Math.min(result[0], result[1]), result[2]);
        int ma = Math.max(Math.max(result[0], result[1]), result[2]);
        if(maximum-minimum < ma-mi || (ma == 0 && mi == 0))
        {
          result[0] = numbers[i-1];
          result[1] = numbers[i];
          result[2] = numbers[i+1];
        }
      }
    }
    if(result[0]+result[1]+result[2] == 0) return new int[]{};
    else return result;
  } 
}
