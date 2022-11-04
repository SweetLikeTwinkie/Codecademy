public class FizzBuzz
{
	public static void main(Stringp[] args)
	{
		for (int number = 1; number < 101; number++)
		{
			if (number % 3 == 0 || number % 5 == 0)
			{
				if (number % 3 == 0)
				{
					System.out.println("Fizz");
				}
				if (number % 5 == 0)
				{
					System.out.println("Buzz");
				}
				System.out.println();
			}
			else
			{
				System.out.println(number);
			}
		}
	}
}