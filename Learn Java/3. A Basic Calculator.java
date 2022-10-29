public class Calculator
{
	public Calculator
	{

	}

	public int add(int a, int b)
	{
		return (a+b);
	}

	public int subtract(int a, int b)
	{
		return (a-b);
	}

	public int multiply(int a, int b)
	{
		return (a*b);
	}

	public int devide(int a, int b)
	{
		return (a/b);
	}

	public int modulo(int a, int b)
	{
		return (a%b);
	}

	public static void main(String[] args)
	{
		Calculator newCalculator = new Calculator();
		System.out.println(add(5, 7));
		System.out.println(subtract(45, 11));
	}
}